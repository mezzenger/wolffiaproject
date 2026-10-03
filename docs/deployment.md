# Deployment guide

## Current GitHub Pages site

The live address is <https://mezzenger.github.io/wolffiaproject/>. The local preview serves `public/`. GitHub Pages is currently using its default branch/Jekyll build from the repository root, which puts the rendered README at `/` and the intended site at `/public/index.html`. The October 2 Pages build log confirms that Jekyll rendered `README.md` as `/index.html` and uploaded the `public/`, `docs/`, and `tests/` directories.

The workflow at `.github/workflows/deploy-pages.yml` uploads only `public/`.

To make the live root match the local preview:

1. Open repository **Settings → Pages → Build and deployment** and set **Source** to **GitHub Actions**. GitHub's branch source supports only the branch root or `/docs`, not `/public`.
2. Run **Actions → Deploy site to GitHub Pages** if the workflow did not start after the push. Confirm it succeeds and that its artifact path is `./public`.
3. Open <https://mezzenger.github.io/wolffiaproject/> in a fresh browser session. Its page title should be “The Wolffia Project | Food resilience from water, wisdom, and community”; `/mission.html` and `/styles.css` should load at the root.
4. Confirm <https://mezzenger.github.io/wolffiaproject/docs/project-review.html> and `/tests/check-site.py` are no longer served. The published artifact should contain only `public/`.

The website is still a draft. Complete [launch-checklist.md](launch-checklist.md) before treating this public URL as an approved launch. GitHub Pages does not apply Cloudflare's `public/_headers` configuration; review GitHub Pages security-header and privacy implications separately.

## Cloudflare Pages alternative

If the project moves to Cloudflare Pages, use no build command and `public` as the output directory. Do not point Cloudflare at the repository root. Update the public URL, canonical metadata, sitemap, and robots policy only after the domain and publication are approved.
