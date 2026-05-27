# Your Life Under Rome

*A probabilistic portrait of who you would have been, had you been born somewhere in the
Roman world between 100 BC and 420 AD.*

Live at **[YourLifeUnderRome.com](https://YourLifeUnderRome.com)** (GitHub Pages, custom domain).

A static website built from ten richly-researched composite lives. Roll the dice (1–1000)
and fortune drops you into one of them — a peasant, a slave, a senator, a legionary, a
freedman tavern-keeper at Pompeii, a Christian clerk in Constantinople. Each life is a page
of its own, illustrated with **real museum artifacts** from Wikimedia Commons and linked to
further reading.

The site is plain static HTML/CSS/JS — no framework, no build dependencies beyond Python 3 —
designed to be served straight from GitHub Pages.

---

## How it fits together

| File / folder | Role |
|---|---|
| `1_first_draft_roman_lives.md` | **Source of truth for the prose.** `build.py` parses it. Edit the narrative here. |
| `profiles_meta.py` | Per-profile metadata: era/region tags, the curated image gallery, and sources. |
| `build.py` | Parses the draft + merges metadata → renders static HTML into `docs/`. |
| `fetch_images.py` | Downloads the curated Commons images and captures license/attribution. |
| `templates/base.html` | Shared page skeleton (header/footer/fonts). Page bodies are assembled in `build.py`. |
| `docs/` | **The website** (what GitHub Pages serves). Generated + static assets + images. |
| `style-previews/` | The four design probes (Marble, Fresco, Mosaic, Parchment). Kept for reference. |
| `IMAGE_PROMPTS.md` | Auto-generated prompts for the daily-life illustration slots (for a commissioned artist, or — last resort — image-gen). |

Inside `docs/`:

```
docs/
  index.html              landing page: hero, dice roller, the 1000-bar, the ten cards
  lives/<slug>.html       one page per life
  credits.html            colophon + full image attribution table + further reading
  css/style.css           Parchment / Manuscript theme (hand-authored)
  js/dice.js              the roller (fair 1–1000 via crypto, bone-dice animation)
  js/lives-index.js       generated roll→life index consumed by dice.js
  images/<slug>/*.jpg      real museum artifacts (downloaded; committed to the repo)
  data/image_credits.json  attribution captured from the Commons API
```

## Build it

```bash
python3 fetch_images.py     # one-time (and whenever you add Commons images): download artifacts
python3 build.py            # regenerate docs/  (run after editing the draft or metadata)
```

`build.py --parse-check` prints what it parsed from the draft without rendering — handy after
editing `1_first_draft_roman_lives.md`.

## Preview locally

```bash
python3 -m http.server -d docs 8000
# open http://127.0.0.1:8000/
```

## Deploy to GitHub Pages

1. Push everything (including `docs/`, which carries the images) to the GitHub repo
   (`github.com/danieldugas/YourLifeUnderRome`).
2. In **Settings → Pages**, set **Source: Deploy from a branch**, pick the publishing branch,
   folder **`/docs`**.
3. GitHub serves it as-is — there is no build step on their side. (A `.nojekyll` file is included
   so asset folders are served verbatim.)
4. **Custom domain.** `docs/CNAME` already contains `YourLifeUnderRome.com` (written by `build.py`).
   In **Settings → Pages → Custom domain**, enter `YourLifeUnderRome.com`. At the registrar, point
   the apex with GitHub's four `A` records (185.199.108–111.153) and add a `www` `CNAME` →
   `danieldugas.github.io`. Then enable **Enforce HTTPS**.

## Editing / extending

- **Change wording** of a life → edit `1_first_draft_roman_lives.md`, re-run `build.py`.
- **Adjust the odds** → edit the `**Roll: a–b (w out of 1,000)**` line in the draft.
- **Add another real image** → add a `{"kind": "commons", "file": "File:…", …}` entry to that
  profile in `profiles_meta.py`, run `fetch_images.py` then `build.py`.
- **Fill a daily-life illustration slot** → commission or draw an illustration from the matching
  prompt in `IMAGE_PROMPTS.md` (image-gen only as a last resort), save it to the path shown, wire it in.

## Sources & licensing

Every illustration is a real artifact or museum photograph, credited on the **Sources &
Credits** page with author, license, and a link back to its Wikimedia Commons page (a mix of
Public Domain, CC0, CC BY, and CC BY-SA — all retained under their original licenses). The
profiles themselves are **composites**: fictional individuals built from demographic models,
archaeology, papyri and the literary record. The source-linking is inspired by Bret Devereaux's
[ACOUP](https://acoup.blog/).
