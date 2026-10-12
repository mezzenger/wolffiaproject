# Architecture

## Decision

Phase 1 keeps the existing HTML, CSS, and JavaScript. The site already has working public routes, a project-specific visual system, and a dependency-free checker. Astro would offer component and content collections, but would add Node, a package lock, migration work across the existing pages and recipe atlas, and new build maintenance. A small Python standard-library build provides the immediate benefit of shared primary header and footer and a controlled deployment artifact without that cost. Revisit a generator if page volume or translation needs make this approach hard to maintain.

## Layout

| Path | Purpose |
| --- | --- |
| `public/` | Authored pages, shared CSS/JS, recipe data, and publishable assets. Relative links support the Pages project path. |
| `site/components/` | Canonical primary header and common footer, inserted into top-level pages at build time. Contact keeps its privacy-specific footer; recipe pages keep their distinct navigation. |
| `tools/build.py` | Copies an allowlisted set of files to `dist/`, substitutes shared chrome, adds a static heading to recipe detail loading states, and rejects publication markers and unexpected files. |
| `tools/dev.py`, `launch.sh` | Local preview at `127.0.0.1:4174`, rebuilding on source changes. |
| `tests/` | Existing source checker and production artifact checker. |
| `docs/` | Internal review, status, source, deployment, and collaboration records. Never deployed. |
| `dist/` | Generated deployment output, ignored by Git. GitHub Pages uploads this directory only. |

No database, application server, third-party runtime script, package manager, or dependency lock is needed. Python 3.10 or later and Bash are the only development requirements. The standard library is part of the Python installation; there are no separately resolved packages to lock. Chrome/Chromium is optional for visual checks.

## Extending the site

For a new simple page, copy a top-level page in `public/`, update its title, description, `data-page`, heading, and body. Add a navigation link to `site/components/header.html` only if it belongs in primary navigation; otherwise link from a relevant page or the footer. For a recipe route, follow the recipe atlas structure and register the content and licensing status before publication. Keep styles in `public/styles.css` or `public/recipe-styles.css`; use the existing CSS tokens. Keep images in `public/images/` and record rights in the image register. Run `./tests/check-all.sh`, preview locally, then open a pull request.

Future educational material can be placed under a reviewed public documents directory as accessible HTML and optional print/download assets. Content records can add title, description, author, review date, status, and sources when an actual publishing workflow needs them. No empty CMS schema is introduced now. Future topics include biology and cultivation research, responsible growing, pilot reports, training, tutorials, nutrition and recipes, references, updates, and participation. The current pages provide the entry points; new categories should be added only with reviewed content.

## Accessibility and publication boundaries

HTML remains semantic and CSS retains focus and reduced-motion rules. The production check covers structural basics, links, labels, and headings. Browser behavior, contrast, 200% zoom, touch targets, screen-reader announcements, and recipe JavaScript states need manual review before launch. `public/robots.txt` keeps indexing blocked pending approval. GitHub Pages ignores `_headers`; Cloudflare Pages can apply it. Hosting logs and privacy language need owner review. A successful build or deploy does not approve the draft copy or public launch.
