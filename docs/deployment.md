# Deployment guide

## Current GitHub Pages site

The intended address is <https://mezzenger.github.io/wolffiaproject/>. The local preview serves generated `dist/`. An October 2 Pages build used the default branch/Jekyll source from the repository root, rendering `README.md` at `/` and exposing `public/`, `docs/`, and `tests/`. The repository later added a Pages artifact workflow, but the owner must confirm **Settings → Pages → Source: GitHub Actions** and verify the live artifact. Do not assume the current live site matches the local preview without that check.

The workflow at `.github/workflows/deploy-pages.yml` runs `./tests/check-all.sh` and uploads only verified `dist/`. `dist/` is generated from the publishable files in `public/`; internal documentation, tests, and repository configuration are excluded. Do not deploy the repository root.

To make the live root match the local preview:

1. Open repository **Settings → Pages → Build and deployment** and set **Source** to **GitHub Actions**. GitHub's branch source supports only the branch root or `/docs`, not `/public`.
2. After an approved merge to `main`, confirm the workflow succeeds and its artifact path is `./dist`. Only a push to `main` triggers this workflow.
3. Open <https://mezzenger.github.io/wolffiaproject/> in a fresh browser session. Its page title should be “The Wolffia Project | Food resilience from water, wisdom, and community”; `/mission.html` and `/styles.css` should load at the root.
4. Confirm <https://mezzenger.github.io/wolffiaproject/docs/project-review.html> and `/tests/check-site.py` are no longer served. The published artifact should contain only the verified `dist/` output.

The website is still a draft. Complete [launch-checklist.md](launch-checklist.md) before treating this public URL as an approved launch. `robots.txt` currently blocks indexing; removing that block is a separate publication decision. GitHub Pages does not apply Cloudflare's `_headers` configuration, so those security headers cannot be assumed on Pages. Review hosting logs and privacy wording against the actual host. A workflow success is technical readiness, not content approval.

## Cloudflare Pages alternative

If the project moves to Cloudflare Pages, use `python3 tools/build.py` as the build command and `dist` as the output directory. Do not point Cloudflare at the repository root. Cloudflare can apply the copied `_headers` file. Update the public URL, canonical metadata, sitemap, and robots policy only after the domain and publication are approved.
