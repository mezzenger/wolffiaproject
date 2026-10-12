#!/usr/bin/env python3
"""Validate the exact artifact uploaded to GitHub Pages."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "dist"
BASE = "https://mezzenger.github.io/wolffiaproject/"
REQUIRED = {"index.html", "mission.html", "why-aquatic-foods.html", "wolffia.html",
            "water-spinach.html", "responsible-growing.html", "pilot-project.html",
            "recipes.html", "community.html", "contact.html", "sources.html",
            "accessibility.html", "privacy.html", "robots.txt"}
ALLOWED = {".html", ".css", ".js", ".json", ".svg", ".webp", ".png",
           ".jpg", ".jpeg", ".gif", ".ico", ".txt", ".woff2"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = False
        self.title = False
        self.in_title = False
        self.main = 0
        self.h1 = 0
        self.ids = set()
        self.links = []
        self.images = []
        self.labels = set()
        self.inputs = []
        self.label_depth = 0
        self.nav = []
        self.skip = []

    def handle_starttag(self, tag, pairs):
        a = dict(pairs)
        if tag == "html": self.lang = bool(a.get("lang"))
        if tag == "title": self.in_title = True
        if tag == "main": self.main += 1
        if tag == "h1": self.h1 += 1
        if a.get("id"): self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
            if "skip" in a.get("class", ""): self.skip.append(a["href"])
        if tag in ("script", "img") and a.get("src"): self.links.append(a["src"])
        if tag == "img": self.images.append(a)
        if tag == "link" and a.get("href"): self.links.append(a["href"])
        if tag == "label":
            self.label_depth += 1
            if a.get("for"): self.labels.add(a["for"])
        if tag in ("input", "select", "textarea"): self.inputs.append((a, self.label_depth > 0))
        if tag == "nav": self.nav.append(a)

    def handle_endtag(self, tag):
        if tag == "title": self.in_title = False
        if tag == "label": self.label_depth -= 1

    def handle_data(self, data):
        if self.in_title and data.strip(): self.title = True


errors = []
files = {str(p.relative_to(SITE)): p for p in SITE.rglob("*") if p.is_file()}
for missing in sorted(REQUIRED - files.keys()): errors.append(f"missing required output: {missing}")
for name, file in files.items():
    if file.is_symlink(): errors.append(f"symlink in output: {name}")
    if file.suffix.lower() not in ALLOWED and file.name != "_headers":
        errors.append(f"unexpected output file: {name}")
    if name.startswith(("docs/", "tests/", ".github/")) or name in ("README.md", "AGENTS.md"):
        errors.append(f"internal file in output: {name}")
    if file.suffix != ".html": continue
    page = Page()
    page.feed(file.read_text(encoding="utf-8"))
    if not page.lang: errors.append(f"{name}: missing language")
    if not page.title: errors.append(f"{name}: missing title")
    if page.main != 1: errors.append(f"{name}: expected one main, got {page.main}")
    if page.h1 != 1: errors.append(f"{name}: expected one h1, got {page.h1}")
    if not page.skip: errors.append(f"{name}: missing skip link")
    if not page.nav: errors.append(f"{name}: missing navigation")
    for image in page.images:
        if "alt" not in image: errors.append(f"{name}: image missing alt")
    for control, wrapped in page.inputs:
        if control.get("type") in ("hidden", "submit", "button"): continue
        if not (wrapped or control.get("aria-label") or control.get("aria-labelledby") or
                control.get("id") in page.labels):
            errors.append(f"{name}: control lacks accessible label: {control.get('name', '?')}")
    for link in page.links:
        parsed = urlparse(link)
        if parsed.scheme or parsed.netloc or link.startswith(("mailto:", "tel:")): continue
        if parsed.path.startswith("/"):
            errors.append(f"{name}: root-relative URL breaks project base path: {link}")
            continue
        absolute = urljoin(urljoin(BASE, name), link)
        target = urlparse(absolute)
        if not target.path.startswith("/wolffiaproject/"):
            errors.append(f"{name}: link escapes Pages base: {link}")
            continue
        relative = unquote(target.path.removeprefix("/wolffiaproject/"))
        if not relative or relative.endswith("/"): relative += "index.html"
        if relative not in files:
            errors.append(f"{name}: broken local URL {link}")
        elif target.fragment and relative.endswith(".html"):
            destination = Page()
            destination.feed(files[relative].read_text(encoding="utf-8"))
            if unquote(target.fragment) not in destination.ids:
                errors.append(f"{name}: missing fragment {link}")
    for link in page.skip:
        if link.startswith("#") and link[1:] not in page.ids:
            errors.append(f"{name}: skip target missing: {link}")

for css in SITE.rglob("*.css"):
    for url in re.findall(r"url\(['\"]?([^)'\"]+)", css.read_text(encoding="utf-8")):
        if url.startswith(("data:", "http:", "https:")): continue
        if not (css.parent / url.split("#")[0]).is_file():
            errors.append(f"{css.relative_to(SITE)}: missing CSS asset {url}")

if (SITE / "robots.txt").is_file() and "Disallow: /" not in (SITE / "robots.txt").read_text():
    errors.append("draft robots.txt must block indexing")
if (SITE / "recipes/recipes.js").is_file() and not (SITE / "recipe-data/recipes.json").is_file():
    errors.append("recipe data required by recipe script is missing")

if errors:
    for error in errors: print(f"FAIL: {error}")
    sys.exit(1)
print(f"PASS: {len(list(SITE.rglob('*.html')))} production HTML pages, links, fragments, assets, base path, and artifact policy")
