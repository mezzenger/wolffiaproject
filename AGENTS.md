# Repository instructions for coding agents

- Treat `public/` as authored website source and `dist/` as generated output. Never edit or commit `dist/`.
- Check `git status` before work. Preserve unrelated local changes and use a short-lived branch and pull request.
- Run `./tests/check-all.sh` after changing pages, assets, shared components, or deployment. This runs the original checker, builds output, and checks the actual artifact.
- Run `./launch.sh` for a local preview. The preview rebuilds when source files change.
- Edit `site/components/header.html` for primary navigation and `site/components/footer.html` for the common footer. `contact.html` retains its purpose-specific footer. Recipe section pages have their own navigation and styling.
- Keep internal links relative so the site works under GitHub Pages `/wolffiaproject/` and at a domain root.
- Record claims and media in `docs/source-register.md`, `docs/content-status.md`, and `docs/image-register.md`. Preserve `placeholder`, `needs-review`, `verified`, and `do-not-publish` boundaries. Do not turn a technically passing build into publication approval.
- Avoid private data, unsupported food or health claims, unreviewed regulatory statements, external scripts, and new backend dependencies.
- Manual keyboard, zoom, screen-reader, browser, and mobile review remains necessary; static checks do not establish WCAG conformance.
