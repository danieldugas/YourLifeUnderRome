#!/usr/bin/env python3
"""
Verify the inline reference links woven into the prose.

Extracts every [anchor](url) link from the draft (1_first_draft_roman_lives.md)
and from the hidden Cleopatra narrative in profiles_meta.py, dedupes them, and
for each checks:
  - the URL resolves (HTTP 200, following redirects), and
  - if the URL carries a #fragment, that anchor id actually exists in the page.

Run after editing the prose:  python3 check_links.py
Exit code is non-zero if anything failed, so it can gate a commit.
"""

import re
import subprocess
import sys
import urllib.parse
from pathlib import Path

import profiles_meta as M

ROOT = Path(__file__).resolve().parent
DRAFT = ROOT / "1_first_draft_roman_lives.md"

# Same link grammar build.py uses (URLs may hold one level of balanced parens).
LINK_RE = re.compile(r"\[([^\]]+?)\]\(((?:[^()\s]|\([^()]*\))+)\)")


def collect():
    """[(url, where)] for every inline link in the prose sources."""
    out = []
    for m in LINK_RE.finditer(DRAFT.read_text(encoding="utf-8")):
        out.append((m.group(2), "draft"))
    for para in M.SECRET.get("narrative", []):
        for m in LINK_RE.finditer(para):
            out.append((m.group(2), "cleopatra"))
    return out


def fetch(url):
    """(http_code, body) — curl follows redirects and handles TLS for us."""
    r = subprocess.run(
        ["curl", "-sSL", "--max-time", "30", "-A", "ylur-link-check/1.0",
         "-w", "\n__CODE__%{http_code}", url],
        capture_output=True, text=True)
    out = r.stdout
    i = out.rfind("\n__CODE__")
    if i < 0:
        return "ERR", out
    return out[i + len("\n__CODE__"):].strip(), out[:i]


def main():
    links = collect()
    where = {}
    for url, w in links:
        where.setdefault(url, set()).add(w)

    bad = []
    for url in sorted(where):
        base, _, frag = url.partition("#")
        code, body = fetch(base)
        ok = code == "200"
        anchor_ok = True
        if ok and frag:
            f = urllib.parse.unquote(frag)
            anchor_ok = any(s in body for s in (
                f'id="{f}"', f"id='{f}'", f'id="{frag}"'))
        if ok and anchor_ok:
            status = "OK"
        elif ok:
            status = "BAD-ANCHOR"
        else:
            status = f"HTTP {code}"
            bad.append((url, status))
            print(f"[{status:>10}] ({len(where[url])}x) {url}")
            continue
        if status != "OK":
            bad.append((url, status))
        print(f"[{status:>10}] ({len(where[url])}x) {url}")

    print(f"\n{len(where)} unique links — {len(where) - len(bad)} OK, {len(bad)} problem(s).")
    for url, status in bad:
        print(f"  PROBLEM [{status}] {url}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
