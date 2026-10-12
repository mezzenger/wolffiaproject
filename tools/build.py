#!/usr/bin/env python3
"""Build the public static artifact using only Python's standard library."""

from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "public"
OUTPUT = ROOT / "dist"
COMPONENTS = ROOT / "site" / "components"
PUBLISHABLE = {".html", ".css", ".js", ".json", ".svg", ".webp",
               ".png", ".jpg", ".jpeg", ".gif", ".ico", ".txt", ".woff2"}
SPECIAL = {"_headers"}
BLOCKED_MARKERS = ("do-not-publish", "[VERIFY BEFORE PUBLICATION]", "lorem ipsum")


def main():
    header = (COMPONENTS / "header.html").read_text(encoding="utf-8").strip()
    footer = (COMPONENTS / "footer.html").read_text(encoding="utf-8").strip()
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    count = 0
    for source in sorted(SOURCE.rglob("*")):
        if source.is_dir():
            continue
        if source.is_symlink():
            raise SystemExit(f"Refusing symlink in public source: {source}")
        if source.suffix.lower() not in PUBLISHABLE and source.name not in SPECIAL:
            raise SystemExit(f"Unexpected file in public source: {source}")
        destination = OUTPUT / source.relative_to(SOURCE)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.suffix == ".html":
            content = source.read_text(encoding="utf-8")
            if any(marker.lower() in content.lower() for marker in BLOCKED_MARKERS):
                raise SystemExit(f"Publication marker in {source}")
            if source.parent == SOURCE:
                content, headers = re.subn(r'<header class="site-header"[^>]*>.*?</header>',
                                           lambda _: header, content, count=1, flags=re.S)
                if headers != 1:
                    raise SystemExit(f"Expected one site header in {source}")
                # Contact has a purpose-specific privacy reminder in its footer.
                if source.name != "contact.html":
                    content, footers = re.subn(r'<footer class="site-footer"[^>]*>.*?</footer>',
                                               lambda _: footer, content, count=1, flags=re.S)
                    if footers != 1:
                        raise SystemExit(f"Expected one site footer in {source}")
            elif '<article id="recipeDetail" data-recipe-fallback>' in content:
                title = re.search(r'<title>(.*?)\s*\|', content, re.S)
                if not title:
                    raise SystemExit(f"Recipe detail lacks a title in {source}")
                fallback = (f'<article id="recipeDetail" data-recipe-fallback>'
                            f'<h1>{title.group(1).strip()}</h1>'
                            '<p>Loading recipe draft…</p>'
                            '<p><a href="../">Return to recipes</a></p></article>')
                content, count_replaced = re.subn(r'<article id="recipeDetail" data-recipe-fallback>.*?</article>',
                                                  lambda _: fallback, content, count=1, flags=re.S)
                if count_replaced != 1:
                    raise SystemExit(f"Unexpected recipe fallback in {source}")
            if source.parent != SOURCE and '<link rel="icon"' not in content:
                depth = len(source.relative_to(SOURCE).parts) - 1
                icon = '../' * depth + 'wolffia-public-site.svg'
                content = content.replace('</head>', f'<link rel="icon" href="{icon}" type="image/svg+xml" />\n  </head>', 1)
            destination.write_text(content, encoding="utf-8")
        else:
            shutil.copyfile(source, destination)
        count += 1
    print(f"Built {count} publishable files in {OUTPUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
