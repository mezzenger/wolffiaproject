# Collaboration workflow

This repository is intended to become the shared working home for the public-facing Wolffia Project website.

## Recommended repository model

- `main` is the reviewed, deployable branch.
- Work happens on short-lived branches.
- Changes reach `main` through pull requests.
- GitHub Issues track bugs, reviews, research questions, content decisions, and launch tasks.
- GitHub Actions runs the static-site check on pushes and pull requests.
- Cloudflare Pages should use `public/` as the output directory and create preview deployments for pull requests/branches when the Git integration is connected.

## Suggested first milestone: collaboration-ready

- [ ] Create the GitHub repository under the chosen owner or organization.
- [ ] Push the existing source to `main`.
- [ ] Protect `main` from direct changes where practical.
- [ ] Require the site-check workflow to pass before merge.
- [ ] Turn launch-checklist items into GitHub Issues.
- [ ] Assign reviewers for scientific/food-safety, accessibility, media, and project-owner approval as available.
- [ ] Connect Cloudflare Pages only after the repository owner approves the connection.

## Suggested labels

A small label set is easier to maintain than a large taxonomy:

- `accessibility`
- `bug`
- `content`
- `documentation`
- `food-safety`
- `good first issue`
- `media-permission`
- `needs-review`
- `privacy`
- `science`
- `deployment`

## Pull-request review

Pull requests should explain what changed, why, how it was tested, and whether any public-facing claim changed. A scientific or regulatory wording change should identify the supporting source and review status.

Preview deployments are for review; they are not equivalent to project approval or public launch.

## Public-launch boundary

Collaboration can begin before the project launches publicly. Connecting a private or access-controlled repository, reviewing pull requests, and using preview deployments does not require announcing a final domain or treating draft content as approved.
