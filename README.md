# Wolffia Public Site

Static-first public-facing Wolffia and water-spinach food-resilience website.

Current version: **0.2.0** (prelaunch)

## Current status

This directory contains a lightweight static first draft with the required public pages in `public/`, shared styling, responsive navigation, a clearly labeled conceptual illustration, source notes, and internal launch registers outside the intended publish directory. The GitHub Pages workflow builds and uploads only verified `dist/`; the owner must confirm the Pages source setting and live artifact. The draft is publicly reachable but has not received publication or legal approval.

The source briefs are [MAIN public-facing.md](MAIN%20public-facing.md) and [Wolffia_Public_Website_CODEX_BRIEF.md](Wolffia_Public_Website_CODEX_BRIEF.md). The draft keeps project identity, contact details, pilot results, media permissions, and claims requiring review explicitly unresolved.

## Planned site

The brief calls for a static-first, mobile-friendly public education site suitable for Cloudflare Pages, with:

- Home
- Mission
- Why Aquatic Foods
- Wolffia
- Water Spinach
- Responsible Growing
- Pilot Project
- Recipes link/section
- Community
- Contact

The public message is deliberately cautious: responsible cultivation, food safety, pilot-scale learning, transparent results, culturally respectful recipes, and no unsupported nutrition or medical claims.

## Launch

Search for **Wolffia Public Site** in the desktop application menu, or run:

```bash
./launch.sh
```

The launcher builds and serves `dist/` locally at <http://127.0.0.1:4174>, rebuilds on source changes, and opens it in the browser. Set `LAUNCHER_NO_OPEN=1` for a terminal-only check.

Run the dependency-free site checks with:

```bash
./tests/check-all.sh
```

Install Python 3.10 or newer and Bash first. On CachyOS/Arch Linux use `sudo pacman -S python bash`; on Debian/Ubuntu use `sudo apt install python3 bash`. No Python packages, Node packages, Docker image, or lockfile are needed. The build uses only Python's standard library.

For a production artifact without starting the preview, run `python3 tools/build.py`. The generated `dist/` directory is ignored by Git. `./tests/check-all.sh` runs the original site checker, builds the artifact, and checks output links, assets, accessibility basics, and the GitHub Pages base path. See [docs/architecture.md](docs/architecture.md) for file roles and how to add a page.

## Related projects

- `../wolffia-pilot-internal/` - private operational data and reporting prototype
- `../wolffia-recipe-atlas/` - working static recipe site intended to be linked from this main site
- `../wolffia-tracker/` - newer, separate Flask tracker prototype

## Collaboration

This repository is prepared for branch-and-pull-request collaboration. Start with [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/collaboration.md](docs/collaboration.md). GitHub Actions already runs the dependency-free site checks on pushes and pull requests, and the repository includes issue and pull-request templates for accessibility, content/science/food-safety review, bugs, and improvements.

The project can begin collaborating before public launch. Final branding, publication approvals, domain, contact route, privacy wording, and licensing remain owner decisions.

## Deployment

GitHub Pages must use the repository workflow, which publishes only verified `dist/`. See [docs/deployment.md](docs/deployment.md) for the required Pages setting and verification steps. Cloudflare Pages remains an alternative.

## Missing before public launch

- Final project/brand name, logo approval, and public domain
- Approved copy and reviewed scientific/food-safety claims
- Pilot photos and cleared public-use media
- Recipe Atlas URL and navigation integration
- Contact destination and privacy language
- Accessibility, responsive, link, and browser testing
- Correct GitHub Pages publishing source and verify that only `dist/` is served
