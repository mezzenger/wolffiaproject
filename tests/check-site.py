#!/usr/bin/env python3
"""Small dependency-free checks for the static first draft."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1] / "public"
REQUIRED = ["index.html", "mission.html", "why-aquatic-foods.html", "wolffia.html",
            "water-spinach.html", "responsible-growing.html", "pilot-project.html",
            "recipes.html", "community.html", "contact.html", "sources.html",
            "accessibility.html", "privacy.html", "styles.css", "script.js"]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.title = False
        self.in_title = False
        self.h1 = 0
        self.main = 0
        self.lang = False
        self.skip = False
        self.hrefs = []
        self.images = []
        self.scripts = []
        self.styles = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if tag == "html" and attrs.get("lang"): self.lang = True
        if tag == "title": self.in_title = True
        if tag == "h1": self.h1 += 1
        if tag == "main": self.main += 1
        if tag == "a" and attrs.get("href"): self.hrefs.append(attrs["href"])
        if tag == "img": self.images.append(attrs)
        if tag == "script" and attrs.get("src"): self.scripts.append(attrs["src"])
        if tag == "link" and attrs.get("rel") == "stylesheet": self.styles.append(attrs.get("href", ""))
    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
        if tag in self.tags: self.tags.reverse(); self.tags.remove(tag); self.tags.reverse()
    def handle_data(self, data):
        if self.in_title and data.strip(): self.title = True

def fail(message):
    print(f"FAIL: {message}")
    return 1

errors = []
for name in REQUIRED:
    if not (ROOT / name).is_file(): errors.append(f"missing {name}")
for page in sorted(ROOT.glob("*.html")):
    parser = PageParser()
    parser.feed(page.read_text(encoding="utf-8"))
    if not parser.lang: errors.append(f"{page.name}: missing html lang")
    if not parser.title: errors.append(f"{page.name}: missing title")
    if parser.h1 != 1: errors.append(f"{page.name}: expected exactly one h1, found {parser.h1}")
    if parser.main != 1: errors.append(f"{page.name}: expected exactly one main")
    if "href=\"#main-content\"" not in page.read_text(encoding="utf-8"): errors.append(f"{page.name}: missing skip link")
    for image in parser.images:
        if "alt" not in image: errors.append(f"{page.name}: image missing alt attribute")
    for asset in parser.scripts + parser.styles:
        if asset and not urlparse(asset).scheme and not (ROOT / asset).is_file(): errors.append(f"{page.name}: missing asset {asset}")
    for href in parser.hrefs:
        if not href or href.startswith(("#", "mailto:", "tel:", "http://", "https://")): continue
        target = href.split("#", 1)[0]
        if target and not (ROOT / target).is_file(): errors.append(f"{page.name}: broken local link {href}")
    body = page.read_text(encoding="utf-8")
    if re.search(r"TODO|FIXME|\[VERIFY|lorem ipsum", body, re.I): errors.append(f"{page.name}: draft marker leaked into public HTML")

if errors:
    for error in errors: print(f"FAIL: {error}")
    sys.exit(1)
print(f"PASS: {len(list(ROOT.glob('*.html')))} HTML pages, local assets, skip links, headings, image alts, and local links checked")
