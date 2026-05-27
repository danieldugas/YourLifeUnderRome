# Building the first website — "Your Life Under Rome"

*A summary of the work that turned the ten-lives draft into a static, GitHub-served website.*

This continues from [`0_initial_prompt.md`](0_initial_prompt.md), the draft in
[`1_first_draft_roman_lives.md`](1_first_draft_roman_lives.md), and the website brief in
[`2_website_prompt.md`](2_website_prompt.md).

---

## What we set out to build

A static site (no backend, served from GitHub Pages) with an ancient-Rome aesthetic: a landing
page, a "roll the Roman dice" random generator (1–1000) that drops you into one of ten lives,
a page per life, real museum illustrations, and heavy source-linking in the spirit of Bret
Devereaux's [ACOUP](https://acoup.blog/).

## Decisions made along the way

1. **Visual style — chosen by comparison.** Rather than guess, I built four self-contained
   design probes with identical placeholder content — **Marble & Gold**, **Fresco / Pompeii**,
   **Mosaic & Stone**, **Parchment / Manuscript** — kept in [`style-previews/`](style-previews/).
   We picked **Parchment / Manuscript**: aged vellum, ink-brown body, red rubricated headings,
   gold versals, a ruled "codex" frame. (Body type is the readable EB Garamond; headings/rubrics
   are IM Fell English SC + Cinzel. One CSS variable switches the body face if we ever want pure
   IM Fell.)

2. **Illustrations — real artifacts first, AI for the gaps.** Per the brief, the priority is
   **actual museum pieces from Wikimedia Commons**, each chosen for a direct connection to the
   life it sits beside. Where no single artifact captures a daily-life scene (a family before
   the house, the slave barracks), there's an **AI-illustration slot** with a ready prompt.

3. **Prose stays in one editable place.** `build.py` parses
   `1_first_draft_roman_lives.md` directly as the source of truth — no re-typing, no drift. To
   change a life's wording or its odds, edit the draft and rebuild.

4. **Renamed to match the domain.** With the purchase of **YourLifeUnderRome.com**, the site
   title became **"Your Life Under Rome"** (the dice conceit — *your* life — fits better than
   "ten"). The "The Ten Lives" section still names the ten profiles. The title is a single
   `SITE_TITLE` constant in `build.py`.

## How it's put together

```
1_first_draft_roman_lives.md   prose: the ten lives (source of truth, hand-written)
profiles_meta.py               per-life era/tags + curated image gallery + sources
build.py                       parse draft + merge meta + render -> docs/
fetch_images.py                pull curated Commons images + license/attribution via the API
templates/base.html            shared page skeleton; page bodies assembled in build.py
docs/                          THE SITE (committed; GitHub Pages serves it)
  index.html  lives/<slug>.html  credits.html
  css/style.css  js/dice.js  js/lives-index.js (generated)
  images/<slug>/*  data/image_credits.json  CNAME  .nojekyll
style-previews/                the four design probes (kept for reference)
```

The build is dependency-free beyond **Python 3** — GitHub does no build step on its side.

## What's in the site now

- **Landing page:** hero with S·P·Q·R, the dice roller, the "how to read the odds" note, a
  **1000-segment weight bar** (each life's slice sized to its probability — the senator is a
  3/1000 sliver, on purpose), and the ten life-cards.
- **The dice:** a fair 1–1000 roll via `crypto.getRandomValues`, an animated bone-dice tumble,
  then it maps the roll to a life (or to the unrepresented 906–1000 band) and links you there.
  The die image is a real Roman bone die from Silchester.
- **Ten life pages:** numbered *Caput I–X*, with born/died, the roll band visualized, a hero
  artifact, the narrative, a "Scenes & Artifacts" gallery, a "What shaped this life" callout,
  per-life **Sources & Further Reading**, and prev/next navigation.
- **Credits page:** the composite-vs-real disclaimer, general reading, and a full image
  attribution table (author · license · link to Commons).

## Real images: 28 artifacts, all attributed

`fetch_images.py` queried the Commons API, verified each file, downloaded a web-sized copy, and
recorded license + author + source URL into `docs/data/image_credits.json`. Highlights where the
artifact and the life line up almost too well:

- **Helene** — a British Museum **Fayum mummy portrait, c. 160–180 AD** (her own generation).
- **Successus** — the **Thermopolium of Vetutius Placidus on the Via dell'Abbondanza**, the exact
  street named in his story; plus a Pompeii body-cast for how his death was preserved.
- **Gaius Vibius Celer** — the **cenotaph of Marcus Caelius**, the centurion of Legio XVIII lost
  at Teutoburg, and an iron cavalry mask recovered from the Kalkriese battlefield.
- **Boudiga** — the **Gorgon pediment from Bath** and a real **Bath curse tablet** about a theft,
  mirroring her own curse over stolen property.
- **Aurelius Diza** — a debased antoninianus of Gallienus (the inflation he was paid in) and the
  **tombstone of Aurelius Monimus**, echoing the Syrian name he gave his son.

Licenses are a mix of Public Domain, CC0, CC BY and CC BY-SA — all retained and credited.

## Verification

- Draft parses to **10 profiles**, weights summing to **905/1000** (95 unrepresented).
- Full build emits index + 10 pages + credits with **no unresolved template tokens**.
- Pages and assets all serve **HTTP 200** from `docs/` as site root.
- **All 86 external links** (per-life sources, general reading, and every image's Commons page)
  were link-checked live — **86/86 OK**.

## Deploy

`docs/CNAME` carries `YourLifeUnderRome.com`. Push to
`github.com/danieldugas/YourLifeUnderRome`, set **Pages → Deploy from a branch → /docs**, set the
custom domain, point DNS (GitHub apex `A` records + a `www` CNAME), enable HTTPS. Full steps in
[`README.md`](README.md).

## What's next

- **Fill the AI illustration slots** — one daily-life scene per life; prompts are ready in
  [`IMAGE_PROMPTS.md`](IMAGE_PROMPTS.md). Generate, drop into `docs/images/<slug>/`, rebuild.
- Optionally widen the real-artifact galleries (the manifest in `profiles_meta.py` makes adding a
  Commons image a one-line entry + `fetch_images.py`).
- Then it's launch-ready.
