# Contributing to The Wolffia Project public site

Thank you for helping improve this project. This repository is currently a pre-launch public-site draft. Contributions are welcome, but scientific, food-safety, legal/regulatory, privacy, and public-facing claims require review before they are treated as approved.

## Ways to contribute

Useful contributions include:

- Fixing accessibility, responsive-layout, navigation, and browser issues
- Improving plain-language explanations without overstating evidence
- Checking citations and identifying stronger primary or official sources
- Reviewing Wolffia, water-spinach, food-safety, and cultivation claims
- Improving documentation, tests, and deployment instructions
- Proposing recipes, imagery, or community resources when permissions and sources are clear

Please do not add private pilot data, private locations, personal contact details, copyrighted media without permission, or unreviewed medical/nutrition claims.

## Development workflow

1. Create or choose an Issue describing the work.
2. Create a branch from `main` using a descriptive name such as `docs/source-review` or `fix/mobile-navigation`.
3. Make the smallest practical change that solves the issue.
4. Run the local checks:

   ```bash
   ./tests/check-site.sh
   ```

5. Preview the site locally:

   ```bash
   ./launch.sh
   ```

6. Open a pull request and complete the pull-request checklist.
7. Keep discussion and review attached to the Issue or pull request so decisions remain visible to collaborators.

## Review expectations

A passing automated check does not mean a change is scientifically, legally, medically, nutritionally, or food-safety approved. Changes in those areas should identify the source used and the date it was checked. Prefer primary literature, government sources, universities/extension services, and recognized standards bodies over unsourced summaries.

Time-sensitive regulatory claims—especially water-spinach rules—must be rechecked close to publication.

## Content and media

For new factual claims, record the source in `docs/source-register.md` when appropriate. For new imagery, record the creator, source, license/permission, required credit, and review status in `docs/image-register.md`.

Do not commit secrets, API keys, passwords, private email addresses, unpublished participant information, or private operational data.

## Accessibility

Changes should preserve keyboard access, skip links, meaningful heading structure, visible focus, useful alternative text, zoom usability, and reduced-motion support. Accessibility improvements are welcome even when they do not change the visual design.

## Project decisions still pending

The final public brand/name, logo approval, domain, contact destination, privacy wording, publication license, and several launch approvals are intentionally unresolved. Contributors should not silently settle these decisions in a pull request.
