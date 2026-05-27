#!/usr/bin/env python3
"""
Your Life Under Rome — static site generator.

Single source of truth for the prose is 1_first_draft_roman_lives.md.
build.py parses that file into structured profiles, merges per-profile
metadata (images + sources + tags) from profiles_meta.py, and renders
static HTML into docs/ (which GitHub Pages serves directly).

Usage:
    python3 build.py              # full build into docs/
    python3 build.py --parse-check  # parse the draft and print a summary
"""

import html
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

import profiles_meta as M

ROOT = Path(__file__).resolve().parent
DRAFT = ROOT / "1_first_draft_roman_lives.md"
DOCS = ROOT / "docs"
TEMPLATES = ROOT / "templates"
PARA_IMG_SRC = ROOT / "paragraph_images"  # owner's drop folder for commissioned illustrations

SITE_TITLE = "Your Life Under Rome"
SITE_DOMAIN = "YourLifeUnderRome.com"

EN_DASH = "–"
EM_DASH = "—"


# --------------------------------------------------------------------------
# Parsing the draft markdown
# --------------------------------------------------------------------------

HEADER_RE = re.compile(r"^##\s+(\d+)\.\s+(.+?)\s+" + EM_DASH + r"\s+(.+)$")
ROLL_RE = re.compile(
    r"\*\*Roll:\s*(\d+)\s*[" + EN_DASH + r"\-]\s*(\d+)\s*\((\d+)\s*out of 1,000\)\*\*"
)
BORNDIED_RE = re.compile(
    r"\*\*Born:\*\*\s*(.+?)\s*\|\s*\*\*Died:\*\*\s*(.+)", re.UNICODE
)
WHATSHAPED_RE = re.compile(r"^\*\*What shaped this life:\*\*\s*(.+)$", re.UNICODE)


def slugify(name):
    """Latinish name -> ascii slug (strip Greek parenthetical, accents)."""
    name = re.sub(r"\(.*?\)", "", name)  # drop "(Καλασίρις)"
    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ascii", "ignore").decode("ascii")
    name = name.lower().strip()
    name = re.sub(r"[^a-z0-9]+", "-", name).strip("-")
    return name


def split_paragraphs(text):
    """Split a markdown chunk into paragraphs on blank lines."""
    parts = re.split(r"\n\s*\n", text.strip())
    return [p.strip() for p in parts if p.strip()]


def md_inline(text):
    """Escape HTML, then render the small inline markdown subset we use."""
    text = html.escape(text, quote=False)
    # bold then italic (bold uses **, italic uses single * not part of **)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    return text


def md_paragraphs_to_html(paragraphs):
    out = []
    for p in paragraphs:
        p = p.replace("\n", " ")
        out.append("<p>" + md_inline(p) + "</p>")
    return "\n".join(out)


def parse_draft(text):
    """Return (intro_dict, [profile_dicts], unrepresented_dict-ish)."""
    chunks = re.split(r"^---\s*$", text, flags=re.MULTILINE)
    chunks = [c.strip() for c in chunks if c.strip()]

    intro = {}
    profiles = []

    for chunk in chunks:
        lines = chunk.splitlines()
        first = next((l for l in lines if l.strip()), "")

        m = HEADER_RE.match(first.strip())
        if m:
            profiles.append(parse_profile(chunk, m))
            continue

        if first.strip().startswith("# "):  # the single top-level title chunk
            intro = parse_intro(chunk)
            continue
        # summary table + disclaimer chunks: ignored (data comes from profiles)

    return intro, profiles


def parse_intro(chunk):
    paras = split_paragraphs(chunk)
    tagline = ""
    howto = ""
    for p in paras:
        if p.startswith("# "):  # the title heading itself
            continue
        if p.startswith("*") and p.endswith("*") and not tagline:
            tagline = p.strip("*").strip()
        elif "How to read" in p:
            howto = p
    return {"tagline": tagline, "howto_html": md_paragraphs_to_html([howto]) if howto else ""}


def parse_profile(chunk, header_match):
    number = int(header_match.group(1))
    name_full = header_match.group(2).strip()
    role_full = header_match.group(3).strip()

    # name + optional greek parenthetical
    gm = re.match(r"^(.*?)\s*\((.+?)\)\s*$", name_full)
    if gm:
        name = gm.group(1).strip()
        name_native = gm.group(2).strip()
    else:
        name = name_full
        name_native = ""

    # role "Peasant Smallholder, Central Italy" -> role / place
    if "," in role_full:
        role, place = role_full.split(",", 1)
        role, place = role.strip(), place.strip()
    else:
        role, place = role_full, ""

    roll = ROLL_RE.search(chunk)
    if not roll:
        raise ValueError(f"No roll line in profile {number} ({name})")
    roll_min, roll_max, weight = (int(roll.group(i)) for i in (1, 2, 3))

    bd = BORNDIED_RE.search(chunk)
    born = bd.group(1).strip() if bd else ""
    died = bd.group(2).strip().rstrip("*").strip() if bd else ""

    # Body: paragraphs after the born/died line, minus the what-shaped trailer.
    body_start = chunk.find(bd.group(0)) + len(bd.group(0)) if bd else 0
    body = chunk[body_start:]
    paras = split_paragraphs(body)

    what_shaped = ""
    narrative_paras = []
    for p in paras:
        wm = WHATSHAPED_RE.match(p)
        if wm:
            what_shaped = wm.group(1).strip()
        else:
            narrative_paras.append(p)

    return {
        "number": number,
        "name": name,
        "name_native": name_native,
        "name_full": name_full,
        "role": role,
        "place": place,
        "role_full": role_full,
        "slug": slugify(name),
        "roll_min": roll_min,
        "roll_max": roll_max,
        "weight": weight,
        "born": born,
        "died": died,
        "narrative_html": md_paragraphs_to_html(narrative_paras),
        "narrative_paras": narrative_paras,
        "what_shaped": what_shaped,
    }


# --------------------------------------------------------------------------
# Rendering
# --------------------------------------------------------------------------

ROMAN_MAP = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
             (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
             (5, "V"), (4, "IV"), (1, "I")]


def roman(n):
    out = ""
    for v, s in ROMAN_MAP:
        while n >= v:
            out += s
            n -= v
    return out


def esc(s):
    return html.escape(str(s), quote=True)


def clean_artist(a):
    a = re.sub(r"\s+", " ", a or "").strip()
    if not a or "unknown" in a.lower() or "anonymous" in a.lower():
        return "Anonymous / unknown"
    return a


QUILL_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="1.6" aria-hidden="true"><path d="M20 4 C12 6 7 12 5 20 '
             'M20 4 C18 10 14 13 8 15 M5 20 l3 -1"/></svg>')

ORNAMENT_SVG = ('<svg viewBox="0 0 60 60" fill="none" stroke="currentColor" '
                'stroke-width="2" aria-hidden="true"><path d="M30 6 C22 18 8 18 8 30 '
                'C8 42 22 44 30 54 C38 44 52 42 52 30 C52 18 38 18 30 6 Z"/>'
                '<circle cx="30" cy="30" r="4" fill="currentColor" stroke="none"/></svg>')


def load_credits():
    path = DOCS / "data" / "image_credits.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def render_base(template, *, title, desc, rel, body, body_end=""):
    out = template
    for token, val in {
        "{{TITLE}}": esc(title), "{{DESC}}": esc(desc), "{{REL}}": rel,
        "{{BODY}}": body, "{{BODY_END}}": body_end,
    }.items():
        out = out.replace(token, val)
    return out


def credit_line(rel, rec):
    artist = clean_artist(rec.get("artist"))
    lic = rec.get("license") or "see source"
    licurl = rec.get("license_url") or ""
    src = rec.get("source_url") or ""
    lic_html = (f'<a href="{esc(licurl)}" target="_blank" rel="noopener">{esc(lic)}</a>'
                if licurl else esc(lic))
    src_html = (f'<a href="{esc(src)}" target="_blank" rel="noopener">Wikimedia&nbsp;Commons</a>'
                if src else "Wikimedia&nbsp;Commons")
    return f'<span class="credit">{esc(artist)} &middot; {lic_html} &middot; via {src_html}</span>'


def fig_commons(rel, rec, klass="hero-fig", with_why=True):
    src = rel + rec["local"]
    cap = rec.get("caption", "")
    why = rec.get("why", "")
    whyhtml = f'<span class="why">{esc(why)}</span>' if (with_why and why) else ""
    return (f'<figure class="{klass}"><img src="{esc(src)}" alt="{esc(cap)}" '
            f'loading="lazy"><figcaption>{esc(cap)}{whyhtml}'
            f'{credit_line(rel, rec)}</figcaption></figure>')


def fig_ai(img):
    prompt = img.get("prompt", "")
    cap = img.get("caption", "")
    alt = img.get("alt", cap)
    return (f'<!-- Illustration prompt: {prompt} -->\n'
            f'<figure><div class="ai-slot" role="img" aria-label="{esc(alt)}">'
            f'{QUILL_SVG}<span class="tag">Illustration to come</span></div>'
            f'<figcaption>{esc(cap)}<span class="why">Daily-life scene — a painted '
            f'illustration will live here.</span></figcaption></figure>')


def fig_para(rel, rec):
    """A per-paragraph thumbnail (gallery-sized) sitting above a narrative paragraph.

    rec is either a Commons credit record (from image_credits.json) or a local
    commissioned-illustration record (with is_local / credit_text)."""
    src = rel + rec["local"]
    cap = rec.get("caption", "")
    why = rec.get("why", "")
    whyhtml = f'<span class="why">{esc(why)}</span>' if why else ""
    if rec.get("is_local"):
        credit = (f'<span class="credit">{esc(rec.get("credit_text", "Commissioned illustration"))}'
                  f'</span>')
    else:
        credit = credit_line(rel, rec)
    return (f'<figure class="para-fig"><img src="{esc(src)}" alt="{esc(cap)}" loading="lazy">'
            f'<figcaption>{esc(cap)}{whyhtml}{credit}</figcaption></figure>')


def para_placeholder(label="Illustration to come"):
    """A gallery-sized placeholder above a paragraph when no image fits yet."""
    return (f'<figure class="para-fig"><div class="ai-slot para-slot" role="img" '
            f'aria-label="{esc(label)}">{QUILL_SVG}'
            f'<span class="tag">Illustration to come</span></div></figure>')


def copy_local(slug, entry):
    """Copy a commissioned illustration from paragraph_images/ into docs/images/<slug>/.

    Returns a credit-like record, or None if the source file is missing."""
    src = ROOT / entry["local"]
    if not src.exists():
        return None
    ext = src.suffix.lower() or ".png"
    key = "para-" + slugify(src.stem)
    rel_local = f"images/{slug}/{key}{ext}"
    dest = DOCS / rel_local
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)
    return {
        "local": rel_local,
        "caption": entry.get("caption", ""),
        "why": entry.get("why", ""),
        "credit_text": entry.get("credit", "Commissioned illustration"),
        "is_local": True,
    }


def resolve_para_image(rel, p, entry, credits, local_credits):
    """Map one `para` entry to its rendered figure, falling back to a placeholder."""
    if not entry:
        return para_placeholder()
    if "local" in entry:
        rec = local_credits.get((p["slug"], entry["local"]))
        return fig_para(rel, rec) if rec else para_placeholder()
    if "reuse" in entry:
        rec = credits.get(f'{p["slug"]}/{entry["reuse"]}')
        return fig_para(rel, rec) if rec else para_placeholder()
    if "theme" in entry:
        rec = credits.get(f'themes/{entry["theme"]}')
        return fig_para(rel, rec) if rec else para_placeholder()
    if "commons" in entry:
        rec = credits.get(f'{p["slug"]}/{entry["commons"]["key"]}')
        return fig_para(rel, rec) if rec else para_placeholder()
    return para_placeholder()


def band_bar(roll_min, weight, color_cls):
    """A full 1..1000 track with this life's slice highlighted."""
    left = (roll_min - 1) / 10.0
    width = max(weight / 10.0, 0.8)
    return (f'<div class="mini-bar"><span class="{color_cls}" '
            f'style="margin-left:{left:.2f}%;width:{width:.2f}%"></span></div>')


# ---- merge parsed profiles with metadata ---------------------------------

def merge(profiles):
    for p in profiles:
        meta = M.META.get(p["slug"], {})
        p["era"] = meta.get("era", "")
        p["era_range"] = meta.get("era_range", "")
        p["region"] = meta.get("region", p["place"])
        p["tags"] = meta.get("tags", [])
        p["epitome"] = meta.get("epitome", "")
        p["images"] = meta.get("images", [])
        p["para"] = meta.get("para", [])
        p["sources"] = meta.get("sources", [])
        p["color"] = f"c{p['number']}"
        p["url"] = f"lives/{p['slug']}.html"
        p["era_full"] = (p["era"] + (f" · {p['era_range']}" if p["era_range"] else "")).strip(" ·")
    return profiles


# ---- index page ----------------------------------------------------------

def render_index(template, intro, profiles, credits):
    rel = ""
    tagline = intro.get("tagline", "")
    dice_rec = credits.get("dice/bone-dice")
    die_img = (f'<img class="die-photo" id="die-photo" src="{rel}{dice_rec["local"]}" '
               f'alt="Roman bone dice">' if dice_rec else "")

    # 1000-bar
    segs = []
    legend = []
    for p in profiles:
        w = p["weight"] / 10.0
        show = roman(p["number"]) if w > 3 else ""
        segs.append(
            f'<a class="{p["color"]}" style="width:{w:.2f}%" href="{p["url"]}" '
            f'title="{esc(p["name"])} — {esc(p["role"])} ({p["roll_min"]}–{p["roll_max"]}, '
            f'{p["weight"]}/1000)"><span class="seg-num">{show}</span></a>')
        legend.append(
            f'<span class="key"><span class="sw {p["color"]}"></span>'
            f'{roman(p["number"])}. {esc(p["name"])} ({p["weight"]})</span>')
    u = M.UNREPRESENTED
    uw = u["weight"] / 10.0
    segs.append(f'<span class="cun" style="width:{uw:.2f}%" '
                f'title="Unrepresented lives ({u["roll_min"]}–{u["roll_max"]}, {u["weight"]}/1000)">'
                f'<span class="seg-num"></span></span>')
    legend.append(f'<span class="key"><span class="sw cun"></span>'
                  f'Unrepresented ({u["weight"]})</span>')
    thousand = (f'<div class="thousand"><div class="thousand-bar">{"".join(segs)}</div>'
                f'<div class="thousand-legend">{"".join(legend)}</div></div>')

    # profile cards
    cards = []
    for p in profiles:
        thumb = ""
        first_commons = next((i for i in p["images"] if i.get("kind") == "commons"), None)
        if first_commons:
            rec = credits.get(f'{p["slug"]}/{first_commons["key"]}')
            if rec:
                thumb = f'<img src="{rel}{rec["local"]}" alt="{esc(p["name"])}" loading="lazy">'
        cards.append(
            f'<a class="life-card" href="{p["url"]}">'
            f'<div class="thumb">{thumb}</div>'
            f'<div class="body"><span class="cap">Caput {roman(p["number"])}</span>'
            f'<h3>{esc(p["name"])}</h3>'
            f'<p class="role">{esc(p["role"])}</p>'
            f'<p class="era">{esc(p["region"])} &middot; {esc(p["era_full"])}</p>'
            f'{band_bar(p["roll_min"], p["weight"], p["color"])}'
            f'<span class="mini-label">Roll {p["roll_min"]}–{p["roll_max"]} '
            f'&middot; {p["weight"]} / 1000</span></div></a>')

    body = f"""
<main class="wrap">
  <section class="hero">
    <div class="ornament">{ORNAMENT_SVG}</div>
    <h1 class="title">{SITE_TITLE}<span class="spqr">S · P · Q · R</span></h1>
    <p class="subtitle">{esc(tagline)}</p>
    <div class="hero-sep"></div>
  </section>

  <section class="read">
    <div class="rubric center">Sortes &middot; Cast the Lots</div>
    <div class="dice-panel" id="cast">
      <h2>Cast the Dice</h2>
      <p class="hint">A throw of 1 to 1000 — where would fortune have placed you?</p>
      <div class="die-stage">
        {die_img}
        <div class="die-readout" id="die-readout"><span id="die-num">?</span><span class="roman" id="die-roman"></span></div>
      </div>
      <button class="roll-btn" id="roll-btn" type="button">Cast the dice</button>
      <div class="dice-result empty" id="dice-result"></div>
    </div>
  </section>

  <section class="read">
    <div class="rubric">Incipit &middot; How to read this</div>
    {intro.get("howto_html", "")}
  </section>

  <section>
    <div class="rubric">The Roll of a Thousand Lives</div>
    {thousand}
  </section>

  <section id="the-lives">
    <div class="rubric">The Ten Lives</div>
    <div class="lives-grid">{"".join(cards)}</div>
    <p class="read" style="font-style:italic;color:var(--ink-soft)">
      The remaining {u["weight"]} of 1000 — {esc(u["text"])}</p>
  </section>
</main>
"""
    body_end = (f'<script src="{rel}js/lives-index.js"></script>\n'
                f'<script src="{rel}js/dice.js"></script>')
    return render_base(
        template,
        title=SITE_TITLE,
        desc=tagline or "A probabilistic portrait of life across the Roman world.",
        rel=rel, body=body, body_end=body_end)


# ---- profile page --------------------------------------------------------

def render_profile(template, p, prev_p, next_p, credits, local_credits):
    rel = "../"
    commons = [i for i in p["images"] if i.get("kind") == "commons"]
    ais = [i for i in p["images"] if i.get("kind") == "ai"]

    # Per-paragraph image strip: one thumbnail (or placeholder) above each paragraph.
    prose_blocks = []
    para_meta = p["para"]
    for i, para in enumerate(p["narrative_paras"]):
        entry = para_meta[i] if i < len(para_meta) else None
        img_html = resolve_para_image(rel, p, entry, credits, local_credits)
        ptext = md_inline(para.replace("\n", " "))
        prose_blocks.append(f'<div class="para-block">{img_html}<p>{ptext}</p></div>')
    prose_html = "\n".join(prose_blocks)

    # hero = first commons image (fall back to first ai)
    hero_html = ""
    gallery_imgs = []
    if commons:
        hero_rec = credits.get(f'{p["slug"]}/{commons[0]["key"]}')
        if hero_rec:
            hero_html = fig_commons(rel, hero_rec, klass="hero-fig")
        gallery_source = commons[1:]
    else:
        gallery_source = []

    gallery = []
    for img in gallery_source:
        rec = credits.get(f'{p["slug"]}/{img["key"]}')
        if rec:
            gallery.append(fig_commons(rel, rec, klass="", with_why=True))
    for img in ais:
        gallery.append(fig_ai(img))
    gallery_html = (f'<div class="rubric">Scenes &amp; Artifacts</div>'
                    f'<div class="gallery">{"".join(gallery)}</div>') if gallery else ""

    tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in p["tags"])
    native = (f'<div class="native">{esc(p["name_native"])}</div>'
              if p["name_native"] else "")

    sources = "".join(
        f'<li><span>{f"""<a href="{esc(s["url"])}" target="_blank" rel="noopener">{esc(s["title"])}</a>"""}'
        f'{f"""<span class=note>{esc(s["note"])}</span>""" if s.get("note") else ""}</span></li>'
        for s in p["sources"])

    pager = '<nav class="pager">'
    if prev_p:
        pager += (f'<a class="prev" href="{prev_p["slug"]}.html">'
                  f'<span class="dir">&larr; Caput {roman(prev_p["number"])}</span><br>'
                  f'<span class="nm">{esc(prev_p["name"])}</span></a>')
    if next_p:
        pager += (f'<a class="next" href="{next_p["slug"]}.html">'
                  f'<span class="dir">Caput {roman(next_p["number"])} &rarr;</span><br>'
                  f'<span class="nm">{esc(next_p["name"])}</span></a>')
    pager += '</nav>'

    body = f"""
<main class="wrap"><article class="codex">
  <header class="profile-head">
    <div class="caput">Caput {roman(p["number"])} of X</div>
    <h1>{esc(p["name"])}</h1>
    {native}
    <p class="role">{esc(p["role"])} &middot; {esc(p["place"])}</p>
    <div class="tags">{tags}</div>
  </header>

  <div class="statband">
    <div class="s"><b>Born</b><span>{esc(p["born"])}</span></div>
    <div class="s"><b>Died</b><span>{esc(p["died"])}</span></div>
    <div class="s rollwrap"><b>If you rolled</b><span>{p["roll_min"]}–{p["roll_max"]} &middot; {p["weight"]} / 1000</span>
      {band_bar(p["roll_min"], p["weight"], p["color"])}</div>
  </div>

  {hero_html}

  <div class="rubric">The Life</div>
  <div class="prose">{prose_html}</div>

  {gallery_html}

  <section class="what-shaped">
    <h2>What shaped this life</h2>
    <p>{esc(p["what_shaped"])}</p>
  </section>

  <div class="rubric">Sources &amp; Further Reading</div>
  <div class="sources"><ul>{sources}</ul>
    <p style="font-style:italic;color:var(--ink-soft);font-size:15px">
      The images above are real museum artifacts and photographs, or commissioned illustrations;
      full attribution on the <a href="{rel}credits.html">credits page</a>.</p>
  </div>

  {pager}
  <p class="recast"><a class="roll-btn" href="{rel}index.html#cast" style="text-decoration:none">Cast the dice again</a></p>
  <p style="text-align:center"><a class="backlink" href="{rel}index.html#the-lives">&larr; All ten lives</a></p>
</article></main>
"""
    desc = p["epitome"] or f'{p["role"]} in {p["region"]}, {p["era_range"]}.'
    return render_base(
        template,
        title=f'{p["name"]} — {p["role"]} · {SITE_TITLE}',
        desc=desc, rel=rel, body=body)


# ---- credits page --------------------------------------------------------

def render_credits(template, profiles, credits, local_list):
    rel = ""
    slug_to_name = {p["slug"]: p["name"] for p in profiles}
    slug_to_name["dice"] = "Site (dice)"
    slug_to_name["themes"] = "Recurring scenes"

    rows = []
    for ref, rec in credits.items():
        group = ref.split("/", 1)[0]
        who = slug_to_name.get(group, group)
        thumb = f'<img src="{rel}{rec["local"]}" alt="" loading="lazy">'
        title = rec.get("title", ref)
        artist = clean_artist(rec.get("artist"))
        lic = rec.get("license", "")
        licurl = rec.get("license_url", "")
        src = rec.get("source_url", "")
        lic_html = (f'<a href="{esc(licurl)}" target="_blank" rel="noopener">{esc(lic)}</a>'
                    if licurl else esc(lic))
        rows.append(
            f'<tr><td>{thumb}</td><td>{esc(title)}</td><td>{esc(who)}</td>'
            f'<td>{esc(artist)}</td><td>{lic_html}</td>'
            f'<td><a href="{esc(src)}" target="_blank" rel="noopener">Commons</a></td></tr>')

    # Commissioned / hand-picked illustrations (not from Commons).
    for who, rec in local_list:
        thumb = f'<img src="{rel}{rec["local"]}" alt="" loading="lazy">'
        rows.append(
            f'<tr><td>{thumb}</td><td>{esc(rec.get("caption", ""))}</td><td>{esc(who)}</td>'
            f'<td>{esc(rec.get("credit_text", "Commissioned illustration"))}</td>'
            f'<td>Commissioned</td><td>&mdash;</td></tr>')

    general = "".join(
        f'<li><span><a href="{esc(s["url"])}" target="_blank" rel="noopener">{esc(s["title"])}</a>'
        f'{f"""<span class=note>{esc(s["note"])}</span>""" if s.get("note") else ""}</span></li>'
        for s in M.GENERAL_SOURCES)

    body = f"""
<main class="wrap"><article class="codex">
  <header class="profile-head">
    <div class="caput">Colophon</div>
    <h1>Sources &amp; Credits</h1>
    <p class="role">On the evidence behind these lives</p>
  </header>

  <div class="prose read">
    <p>Every profile is a <strong>composite</strong> — a fictional individual assembled from
    demographic models, archaeology, papyri, inscriptions and the literary record. The dates,
    mortality rates, prices, distances and events are drawn from the historical evidence; the
    person is not.</p>
    <p>The illustrations are, wherever possible, <strong>real artifacts and museum photographs</strong>
    from Wikimedia Commons, each chosen because it connects directly to the life it accompanies, plus a
    few <strong>commissioned illustrations</strong>. They remain under the licenses of their creators,
    credited below. Scenes marked &ldquo;illustration to come&rdquo; are slots for period-style
    illustrations still to be painted.</p>
  </div>

  <div class="rubric">General Reading &amp; Inspiration</div>
  <div class="sources read"><ul>{general}</ul></div>

  <div class="rubric">Image Credits</div>
  <table class="credit-table">
    <thead><tr><th></th><th>Artifact</th><th>Life</th><th>Author</th><th>License</th><th>Source</th></tr></thead>
    <tbody>{"".join(rows)}</tbody>
  </table>

  <p style="text-align:center;margin-top:30px"><a class="backlink" href="{rel}index.html">&larr; Back to the dice</a></p>
</article></main>
"""
    return render_base(template, title=f"Sources & Credits · {SITE_TITLE}",
                       desc=f"Image attributions and further reading for {SITE_TITLE}.",
                       rel=rel, body=body)


# ---- lives-index.js (for the dice) ---------------------------------------

def write_lives_index(profiles):
    lives = [{
        "n": p["number"], "slug": p["slug"], "name": p["name"],
        "role": f'{p["role"]} · {p["place"]}', "era": p["era_full"],
        "min": p["roll_min"], "max": p["roll_max"], "url": p["url"],
    } for p in profiles]
    u = M.UNREPRESENTED
    js = ("/* generated by build.py — do not edit */\n"
          "window.LIVES = " + json.dumps(lives, ensure_ascii=False) + ";\n"
          "window.UNREP = " + json.dumps(
              {"min": u["roll_min"], "max": u["roll_max"], "text": u["text"]},
              ensure_ascii=False) + ";\n")
    (DOCS / "js" / "lives-index.js").write_text(js, encoding="utf-8")


def write_image_prompts(profiles):
    """Emit IMAGE_PROMPTS.md: ready-to-use prompts for the daily-life illustration slots."""
    lines = [
        "# Image prompts — daily-life illustrations",
        "",
        "Each profile has one *illustration* slot for a daily-life scene that no single museum "
        "artifact captures. Commission or draw it (and only as a last resort generate one) from the "
        "prompt below, save it to the shown path, then add a `commons`-style entry (or just "
        "reference the file) so the build drops it in. The shared style suffix keeps them consistent.",
        "",
        "_(All other images on the site are real museum artifacts — see the credits page.)_",
        "",
    ]
    for p in profiles:
        ais = [i for i in p["images"] if i.get("kind") == "ai"]
        if not ais:
            continue
        lines.append(f"## Caput {roman(p['number'])} — {p['name']} ({p['role']})")
        for img in ais:
            lines.append(f"- **Save to:** `docs/images/{p['slug']}/{img['key']}.jpg`")
            lines.append(f"- **Caption:** {img.get('caption','')}")
            lines.append(f"- **Prompt:**\n  > {img.get('prompt','')}")
            lines.append("")
    (ROOT / "IMAGE_PROMPTS.md").write_text("\n".join(lines), encoding="utf-8")


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

def parse_check(intro, profiles):
    print(f"Intro tagline: {intro.get('tagline','')[:70]}...")
    print(f"Parsed {len(profiles)} profiles")
    total = sum(p["weight"] for p in profiles)
    for p in profiles:
        print(f"  {p['number']:>2}. {p['slug']:<24} roll {p['roll_min']}-{p['roll_max']} "
              f"(w{p['weight']:>3})  {p['name']}")
    print(f"  total weight = {total}; unrepresented = {1000 - total}")


def main():
    text = DRAFT.read_text(encoding="utf-8")
    intro, profiles = parse_draft(text)
    profiles.sort(key=lambda p: p["number"])

    if "--parse-check" in sys.argv:
        parse_check(intro, profiles)
        return

    merge(profiles)
    credits = load_credits()
    base = (TEMPLATES / "base.html").read_text(encoding="utf-8")

    (DOCS / "lives").mkdir(parents=True, exist_ok=True)
    (DOCS / "js").mkdir(parents=True, exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS / "CNAME").write_text(SITE_DOMAIN + "\n", encoding="utf-8")  # GitHub Pages custom domain

    # Copy commissioned per-paragraph illustrations from paragraph_images/ into docs/.
    local_credits = {}   # (slug, source_path) -> record, used by resolve_para_image
    local_list = []      # [(life_name, record)] for the credits table
    for p in profiles:
        for entry in p["para"]:
            if isinstance(entry, dict) and "local" in entry:
                rec = copy_local(p["slug"], entry)
                if rec:
                    local_credits[(p["slug"], entry["local"])] = rec
                    local_list.append((p["name"], rec))
                else:
                    print(f"  WARNING: missing local illustration {entry['local']} "
                          f"({p['slug']}) — paragraph will show a placeholder")

    # index
    (DOCS / "index.html").write_text(
        render_index(base, intro, profiles, credits), encoding="utf-8")

    # profiles (X = total count, patched into the caput line)
    total = len(profiles)
    for i, p in enumerate(profiles):
        if p["para"] and len(p["para"]) != len(p["narrative_paras"]):
            print(f"  WARNING: {p['slug']} has {len(p['para'])} para entries but "
                  f"{len(p['narrative_paras'])} paragraphs — strip will misalign")
        prev_p = profiles[i - 1] if i > 0 else None
        next_p = profiles[i + 1] if i < total - 1 else None
        page = render_profile(base, p, prev_p, next_p, credits, local_credits)
        page = page.replace("of X</div>", f"of {roman(total)}</div>")
        (DOCS / "lives" / f'{p["slug"]}.html').write_text(page, encoding="utf-8")

    # credits
    (DOCS / "credits.html").write_text(
        render_credits(base, profiles, credits, local_list), encoding="utf-8")

    write_lives_index(profiles)
    write_image_prompts(profiles)

    print(f"Built {total} profiles + index + credits into {DOCS}")
    missing = [f'{p["slug"]}/{i["key"]}'
               for p in profiles for i in p["images"]
               if i.get("kind") == "commons" and f'{p["slug"]}/{i["key"]}' not in credits]
    # Paragraph-strip commons/theme images that didn't fetch (these fall back to placeholders).
    para_missing = []
    for p in profiles:
        for entry in p["para"]:
            if not isinstance(entry, dict):
                continue
            if "commons" in entry and f'{p["slug"]}/{entry["commons"]["key"]}' not in credits:
                para_missing.append(f'{p["slug"]}/{entry["commons"]["key"]}')
            elif "theme" in entry and f'themes/{entry["theme"]}' not in credits:
                para_missing.append(f'themes/{entry["theme"]}')
    if missing:
        print("  WARNING: missing image credits (run fetch_images.py):", missing)
    if para_missing:
        print("  NOTE: paragraph images not yet fetched (showing placeholders):",
              sorted(set(para_missing)))


if __name__ == "__main__":
    main()
