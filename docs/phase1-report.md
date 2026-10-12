# Phase 1 implementation and verification

Repository: `https://github.com/mezzenger/wolffiaproject`

Starting branch and commit: `main` at `dffe311ffbc263c1db77bc6ffc59f93a3e4769bb`
Implementation branch: `feature/phase1-development-framework`

The starting working tree contained uncommitted recipe, content, style, documentation, and checker changes. They were preserved. The Phase 1 commit stages only its own files and selected documentation changes. As a result, the checked-out local tree has 39 HTML pages while a clean checkout of the commit has the 13 pages already tracked at the starting commit. The build and checks work in both cases; the separate recipe/content work remains for its owner to review and commit.

## Decision and changes

The existing static HTML/CSS/JS architecture remains. A Python standard-library build centralizes the primary header and common footer, copies only publishable files, and produces `dist/`. The recipe detail loading state gains a static heading and return link in output. The preview server rebuilds changed files. GitHub Actions validates source and output, then Pages uploads only `dist/` on a `main` push. See [architecture.md](architecture.md) for tradeoffs and structure, [deployment.md](deployment.md) for owner settings, and [phase2-roadmap.md](phase2-roadmap.md) for next work.

## Verification performed

- Baseline `./tests/check-site.sh`: passed, 39 local HTML pages.
- Final `./tests/check-all.sh`: passed, 39 local HTML pages and 48 output files; production links, fragments, assets, basic structure, project base path, and artifact policy passed.
- Clean starting-commit archive with Phase 1 tooling: `./tests/check-all.sh` passed, 13 HTML pages and 18 output files. This checks that the framework does not depend on the uncommitted recipe work.
- `LAUNCHER_NO_OPEN=1 ./launch.sh`: built the output and returned the local home page. A foreground preview session served the generated site for browser checks.
- Headless Chromium: home page desktop screenshot before and after build had identical SHA-256 hashes; the generated mobile home page rendered at 390 × 844; a recipe detail rendered its data after JavaScript load at `/recipes/wolffia-flatbread/` and `/wolffiaproject/recipes/wolffia-flatbread/`.

## Limits and approval boundary

The work did not include manual screen-reader, keyboard-only, 200% zoom, full contrast, touch target, or cross-browser review. The live GitHub Pages settings and output were not verified from this workspace. The project's publication, scientific, recipe, media, regulatory, privacy, and indexing approvals remain open. The draft `robots.txt` continues to block indexing. GitHub Pages does not use `_headers`; host-level headers and logging need separate review. A passing technical check does not authorize launch.
