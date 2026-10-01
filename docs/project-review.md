# Project review

Reviewed 2026-10-01. This is a source review of the local static draft; it is not a browser, device, assistive-technology, legal, or scientific review.

## Prioritized findings

### Before any public launch

1. **The site blocks search indexing.** `public/robots.txt` has `Disallow: /`, which is correct for a private preview but will keep a launched site out of search results. Change this only when publication is approved, and add a sitemap and canonical URLs after the domain is known.
2. **Project identity and positioning need one owner-approved decision.** The draft consistently uses “The Wolffia Project,” while the source brief includes competing naming/tagline direction and also says not to lock a final brand. Keep the working-name status until the owner confirms name, tagline, entity wording, and whether this pilot is Wolffia-only. Avoid publishing contradictory drafts as if they were settled facts.
3. **Privacy language overstates what a static site means.** The privacy page says the site does not collect information. A static frontend has no form or analytics, but the selected host may process request and security logs. Name the actual host and describe its practices before launch; do not promise zero collection without checking provider settings and terms.
4. **The contact and participation journeys currently end without a usable next step.** Community and Contact deliberately avoid invented contact details, which is appropriate for a local draft. Before publishing an invitation to volunteer, advise, host, or partner, add an approved contact route, a named message steward, response expectations, and a short privacy explanation.
5. **Water-spinach statements are time-sensitive.** The caution is clear and the page cites official sources, but the source register says legal material must be rechecked. Have a reviewer confirm the current federal, Virginia, and local position and the exact activities covered immediately before launch.
6. **No real project imagery is present.** The CSS hero is clearly labeled conceptual art. Use owner-cleared pilot photos when available. A suitable Commons Wolffia image and license are recorded in `image-register.md`; its image file still needs downloading and a visual/specimen review.

### High-value upgrades

- **Simplify the primary navigation.** Ten links compete for space in the desktop header. Keep the most-used destinations at top level and move utility links to the footer or a clearly labeled secondary menu. Preserve direct routes and active-page indication.
- **Make the home page more useful to a first-time visitor.** Add an approved one-sentence project status and a visible next step. Once the Recipe Atlas URL is approved, make Recipes lead to it; today this page is only a placeholder, so avoid presenting it as a live recipe library.
- **Clarify pilot status with real facts when approved.** The current page describes a proposed learning loop but has no host, timeline, measures, project lead, or results. A compact “status / what is being measured / what happens next” block would help partners assess the project without inventing details.
- **Review color contrast for small accent text.** The clay color `#d8795f` is used for small eyebrow text on a light background and is likely too low contrast at that size. Darken it or reserve it for larger text/decorative use, then verify the full palette against WCAG 2.2 AA.
- **Improve mobile menu behavior.** Add Escape-to-close, close after following a navigation link, and consider moving focus appropriately if the menu is intended to behave as a disclosure. Manually check keyboard, touch, zoom, and screen-reader behavior.
- **Keep page source maintainable.** Several pages compress the entire document onto long lines and repeat the same header/footer markup. Reformatting and using a small shared build-time template or static-site generator would make global edits safer; retain plain static output for Pages.

### Technical checks to schedule

- Current structural checker verifies required files, titles, headings, skip links, image `alt` attributes, script/style assets, and local links. It does not check fragment targets, `src` image paths, external-link health, metadata consistency, contrast, keyboard behavior, or actual responsive rendering.
- Before release, check internal fragment targets and image sources; validate external references, sitemap/canonical metadata, and deployed headers; review at narrow, desktop, and 200% zoom; and complete keyboard and screen-reader passes.
- `public/_headers` has a useful restrictive Content Security Policy. When adding locally hosted photos, keep `img-src 'self'`; any future form, embedded service, or analytics integration needs an explicit policy and privacy review.

## Image retrieval note

Wikimedia Commons lists **Nesnad** as the author of “Wolffia globosa Sep 16 2021 04PM.jpeg” and licenses it CC BY 4.0. The exact candidate and credit are in `image-register.md`. Downloading from `upload.wikimedia.org` failed here because the shell could not resolve external hosts. No remote URL was inserted into the site, so the existing local-only image policy remains valid.

## Overall assessment

The draft is a solid, cautious static foundation with clear safety boundaries, useful source notes, responsive CSS, and a lightweight deployment model. It is not ready for public launch while identity, claims review, contact ownership, privacy wording, image permissions, and publication approval remain unresolved.
