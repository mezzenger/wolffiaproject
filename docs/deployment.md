# Deployment guide

The site is static-first and ready for a Cloudflare Pages preview from the `public/` directory.

Recommended Pages settings:

- Framework preset: none
- Build command: none
- Build output directory: `public`
- Production branch: `main`, after review and approval

The repository still needs to be connected to the project owner’s GitHub and Cloudflare accounts. No account, domain, access control, or public deployment has been changed by this local build.

Before the first deployment:

1. Confirm the project name, domain, contact route, and publication approvals.
2. Review [launch-checklist.md](launch-checklist.md).
3. Confirm that only `public/` is configured as the Pages output directory. Internal `docs/` and `tests/` must remain outside the published output.
4. Add final canonical URLs, sitemap, social image, and robots policy after the domain is known.
5. Review the generated preview URL on desktop, mobile, keyboard navigation, and a screen reader.
6. Verify the public URL after deployment.
