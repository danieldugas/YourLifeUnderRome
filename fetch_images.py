#!/usr/bin/env python3
"""
Download the curated Wikimedia Commons artifacts referenced in profiles_meta.py
and capture their license + attribution from the Commons API.

  python3 fetch_images.py            # fetch missing images
  python3 fetch_images.py --force    # re-fetch everything

Writes web-sized images to docs/images/<group>/<key>.<ext> and an attribution
map to docs/data/image_credits.json (consumed by build.py).
"""
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import profiles_meta as M

ROOT = Path(__file__).resolve().parent
IMG_DIR = ROOT / "docs" / "images"
DATA_DIR = ROOT / "docs" / "data"
CREDITS = DATA_DIR / "image_credits.json"

API = "https://commons.wikimedia.org/w/api.php"
UA = "YourLifeUnderRome/0.1 (educational static site; ddugas@flexion.ai)"
THUMB_WIDTH = 1400
FORCE = "--force" in sys.argv


def collect():
    """Yield (group, key, commons_file, caption, why) for every commons image."""
    for img in M.DICE_IMAGES:
        yield ("dice", img["key"], img["file"], img.get("caption", ""), img.get("why", ""))
    for slug, meta in M.META.items():
        for img in meta.get("images", []):
            if img.get("kind") == "commons":
                yield (slug, img["key"], img["file"], img.get("caption", ""), img.get("why", ""))


def strip_html(s):
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).strip()


def api_imageinfo(title):
    params = {
        "action": "query", "format": "json", "titles": title,
        "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata",
        "iiurlwidth": str(THUMB_WIDTH),
    }
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    pages = data.get("query", {}).get("pages", {})
    page = next(iter(pages.values()), {})
    if "missing" in page or "imageinfo" not in page:
        return None
    return page["imageinfo"][0]


def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        dest.write_bytes(r.read())


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    credits = {}
    if CREDITS.exists():
        credits = json.loads(CREDITS.read_text(encoding="utf-8"))

    ok = miss = skip = 0
    for group, key, cfile, caption, why in collect():
        ref = f"{group}/{key}"
        existing = credits.get(ref)
        if existing and not FORCE:
            local = ROOT / "docs" / existing.get("local", "")
            if existing.get("local") and local.exists():
                skip += 1
                print(f"  · skip   {ref}")
                continue

        try:
            info = api_imageinfo(cfile)
        except Exception as e:
            print(f"  ✗ ERROR  {ref}: API {e}")
            miss += 1
            continue
        if not info:
            print(f"  ✗ MISSING {ref}: {cfile}")
            miss += 1
            continue
        if not info.get("mime", "").startswith("image/"):
            print(f"  ✗ NOTIMG {ref}: {info.get('mime')}")
            miss += 1
            continue

        thumb = info.get("thumburl") or info.get("url")
        ext = Path(urllib.parse.urlparse(thumb).path).suffix.lower() or ".jpg"
        if ext not in (".jpg", ".jpeg", ".png", ".gif"):
            ext = ".jpg"
        out_dir = IMG_DIR / group
        out_dir.mkdir(parents=True, exist_ok=True)
        dest = out_dir / f"{key}{ext}"

        try:
            download(thumb, dest)
        except Exception as e:
            print(f"  ✗ DLFAIL {ref}: {e}")
            miss += 1
            continue

        ext_md = info.get("extmetadata", {})

        def md(field):
            return strip_html((ext_md.get(field) or {}).get("value", ""))

        record = {
            "commons_file": cfile,
            "local": str(dest.relative_to(ROOT / "docs")).replace("\\", "/"),
            "title": md("ObjectName") or cfile.replace("File:", "").rsplit(".", 1)[0],
            "artist": md("Artist"),
            "credit": md("Credit"),
            "license": md("LicenseShortName") or "see source",
            "license_url": (ext_md.get("LicenseUrl") or {}).get("value", ""),
            "source_url": info.get("descriptionurl", ""),
            "width": info.get("thumbwidth") or info.get("width"),
            "height": info.get("thumbheight") or info.get("height"),
            "mime": info.get("mime"),
            "caption": caption,
            "why": why,
        }
        credits[ref] = record
        ok += 1
        print(f"  ✓ {ref:<28} {record['license']:<16} {dest.name}")
        time.sleep(0.3)

    CREDITS.write_text(json.dumps(credits, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nDownloaded {ok}, skipped {skip}, failed/missing {miss}. "
          f"Credits -> {CREDITS.relative_to(ROOT)}")
    if miss:
        print("NOTE: failed entries get a placeholder slot in the build; fix the "
              "File: title in profiles_meta.py and re-run to replace.")


if __name__ == "__main__":
    main()
