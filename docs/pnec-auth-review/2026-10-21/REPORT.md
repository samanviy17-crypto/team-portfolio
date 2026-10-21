# PNEC account adaptation and upstream review — October 21, 2026

Branch: `team-capstone`; starting HEAD `04623ad77e526026ed456802bf1558a2ac5f91ce`. Local changes only; no commit, push, merge, deployment, GitHub issue/board edit or live-server operation.

## Outcome

The existing Flask authentication/profile/recovery routes support the required account flow locally. No backend source, schema, credential or resident-data change was necessary. Frontend reliability fixes retain the existing page structure, style organization, account endpoints, same-origin redirects and production-baseurl preparation.

## Changes made in this task

- `Beasts_FrontEnd/pages/register.html`: replace the large hand-maintained inline CSS body with the existing Sass import pattern; retain a small Jekyll-resolved background asset variable. Two static style attributes become classes. The login UI and form IDs remain.
- `Beasts_FrontEnd/_sass/beasts/inline/pages/_pages-register-1.sass` (new): own the login styles in indented Sass; remove historical CSS commentary and one redundant header rule; preserve necessary WordPress overrides and responsive styles. Address-search fallback now responds to the existing `hidden` attribute rather than requiring a class its JavaScript never sets.
- `Beasts_FrontEnd/pages/profile.html`: show retryable profile-load failure rather than treating every network/server error as logout; omit neighborhood updates when its list is unavailable/loading; validate supported avatar types/size and image decode failures, invalidate stale asynchronous reads, and preserve preview/apply/cancel/save behavior. Both badge-render paths share one renderer. Static presentation moves to named Sass classes; computed meter width/color remain dynamic. Neighborhood completion link targets the neighborhood selector.
- `Beasts_FrontEnd/_sass/beasts/inline/pages/_pages-profile-1.sass`: classes for avatar controls, summary/meter, badges and metadata; remove unused old URL-input, joined-text and small-spinner rules. Preserve spinner animation. Add narrow-screen card/form sizing and text wrapping without global overflow clipping.
- `Beasts_FrontEnd/assets/js/api/auth-api.js`: use existing bounded JSON transport for login, registration, logout and recovery; prefer Flask's specific `detail` over a generic message; preserve credentials for logout retry until server confirmation; optionally distinguish profile fetch failures from 401; safely handle malformed redirect URLs.
- `Beasts_FrontEnd/assets/js/pages/register-page.js`: attach the login submit listener before awaiting session lookup.
- `Beasts_FrontEnd/assets/js/pages/navbar.js` and `assets/js/ui/auth-ui.js`: redirect only after confirmed logout and explain a failed logout instead of reporting success.
- `Beasts_FrontEnd/scripts/test-account-regression.py` (new): isolated account/avatar/recovery, failure-state and responsive regression coverage with temporary SQLite, an ephemeral Flask server and captured mail. Does not modify the developer's database or use SMTP/providers.
- `Beasts_FrontEnd/scripts/test-request-worker.py`: add a regression for specific validation detail taking precedence over a generic message.
- This report and `upstream-comparison.json`: review evidence, not application features.

## CSS provenance and cleanup boundary

No matching Claude author marker was found in the audited account pages/partials. Generated authorship cannot be reliably inferred from a CSS rule. Cleanup therefore targets duplicated rendering, obsolete selectors and inline presentation, while retaining needed styles regardless of author. The upstream branch whose name contains `claude` was inspected rather than deleted or automatically merged. The existing migration organization is retained; no global theme or unrelated stylesheet was changed.

## Upstream comparison

Both inherited directories are ordinary subdirectories of the team repository, not independent Git repositories. Their effective configured remote is the parent `origin` (`samanviy17-crypto/team-portfolio`). No remote configuration or working branch was changed.

Fetched the documented upstreams into separate local review refs using `git fetch --no-tags`; no checkout, merge, reset or worktree overwrite:

| Upstream | Branch / fetched SHA | Finding |
|---|---|---|
| `whitelunarium/Beasts_FrontEnd` | `main`: `9b34469fa85964b3309052b87ae21e88e6bf0a76` | Inherited register page at HEAD matches upstream; local profile/auth adaptations extend the older upstream flow. |
| Same frontend | `claude/strange-johnson-175d40`: `024b4be8bf94beca2a536af499a78b64a05ccb96` | Ancestor of upstream main; no additional branch changes to integrate. |
| `whitelunarium/Beasts_Flask` | `main`: `e2dd4d3a77acea66380bddbe110743f059a26a95` | Older auth/profile behavior than the adapted local source. README labels the copy reference/handoff; GitHub archived flag is false. Neither proves this is the active production checkout. |

The local review refs are `pnec-review-frontend/main`, `pnec-review-frontend/claude-strange-johnson`, and `pnec-review-backend/main`. [File comparison](upstream-comparison.json) records fetched upstream versus local HEAD and the worktree at initial comparison; subsequent edits are described above.

Conflicts avoided: upstream auth strips password whitespace, forces remember-me, lacks local password recovery and uses weaker profile update validation; upstream client lacks session-storage token support and local bounded-request/profile persistence improvements. The upstream profile includes styles/features already adapted here. No required compatible upstream addition was identified, so no upstream source was merged. Production source identity remains an administrator question.

## Verification

- Existing full backend suite: **145 passed**, 7,208 existing warnings, 18.43 seconds. Database fixtures are isolated.
- Request-worker Chromium cases: **12 passed**, including the new detail-priority contract.
- Existing profile browser suite: passed against the normal preview and the final prefixed candidate; registration, cookies/bearer auth, validation/cancel, direct database checks, new-email login, reload/server-restart persistence, navigation and access checks.
- New account browser regression: seven scenario groups passed against the final prefixed candidate. Covers submit during pending session lookup, profile 502/retry, neighborhood 503/save preservation, corrupt/oversize/non-image avatar rejection, avatar cancel/save/reload, logout network failure/retry, captured-mail reset, rejected reused link and new-password login.
- Login/profile page-level overflow and avatar modal usability pass at 320, 390, 768 and 1280px in Chromium.
- Existing SCSS audit: 26 compiled CSS URLs, 245 prior inline Sass imports and 14 static-page stylesheets pass. The new register partial is also compiled by Jekyll.
- Final normal full frontend build passes with 62 inherited warnings; generated auth, navbar and registration scripts match the final source bytes.
- Pages-prefixed candidate build passes using `_config.yml` and `_config.pages.yml`. Final auth worker bytes were compared with the generated worker before final browser checks.
- `git diff --check` passes.

An initial new browser run caught reset-link errors being reduced to a generic message after transport consolidation. The specific-detail precedence fix and new request-worker assertion resolved it; the initial failure log is retained in the temporary evidence directory. No failing result was relabeled as a pass.

Browser tests block external services and use synthetic accounts. Weather/provider data is blocked or fixture-based; screenshots may show missing external logos/footer assets. They do not certify public EC2 routes, production SMTP, external asset uptime or complete cross-browser/accessibility behavior. Existing production 404/CORS blockers and deployment fixes remain separate.

## Evidence and preservation

Local logs, fetched source copies and controlled screenshots: `/tmp/pnec-auth-review-2026-10-21/`. Captures include `profile-320.png`, `profile-1280.png`, `login-320.png`, `login-1280.png`; they contain synthetic data and are not live deployment evidence. These temporary artifacts are not published links.

A before-task patch/hash snapshot permits checking preservation. All pre-existing changes outside the eight explicitly modified frontend/test files remain unchanged. Existing `.env` files and resident SQLite database are compared privately by hash; their contents are never printed. The main branch, deployment workflow, nginx template, backend source, teammate work and prior evidence are untouched by this task.

## Remaining limits

- Production backend revision/routes, CORS and public end-to-end account behavior still need the EC2 administrator; no production success is inferred from local tests.
- Real SMTP delivery remains unverified; browser recovery used the existing test-only captured outbox.
- Existing provider approvals, CPT student authorship and unrelated feature proposals remain unchanged.
- Review the scoped local diff before any separately approved commit/release. No permission to publish or deploy is implied here.


## Indented Sass follow-up — October 21, 2026

Converted **only** the login/profile partials from SCSS to actual indentation-based `.sass` syntax:

- `Beasts_FrontEnd/_sass/beasts/inline/pages/_pages-register-1.sass`
- `Beasts_FrontEnd/_sass/beasts/inline/pages/_pages-profile-1.sass`

The former `.scss` copies were removed so there is one source per partial. This is syntax conversion, not an extension-only rename: selectors, declarations, media queries, imports and keyframes now use indentation rather than block braces and terminating semicolons. Existing foundation imports can remain SCSS; the Sass importer supports mixed partial formats.

### Build support and references

- Verified installed Jekyll **3.9.5** and Ruby Sass **3.7.4** compile indented syntax, including both actual page partials and their foundation dependencies.
- Both pages already use extensionless imports through Jekyll's `scssify` filter. That filter compiles the small import expression; the importer reads `.sass` partials with indented syntax. The page imports therefore remain valid without changing auth markup, JavaScript or layout behavior.
- Updated only the affected profile paths in `scripts/scss-migration.json` and `scripts/SCSS_MIGRATION.md`.
- Updated `scripts/check_scss_sources.py` to recognize `.sass` and `.scss` partials, with quoted/unquoted imports and optional semicolons. It still checks the existing project migration inventory.
- Compared compiled CSS before/after conversion. Rules and values match after normalizing equivalent leading-zero numeric formatting and quote choices for font names/empty strings. No responsive rules, selectors or property values were intentionally changed.

### Follow-up results

- Prefixed Jekyll build: **passed** using `_config.yml,_config.pages.yml` with both `.sass` files present and former `.scss` files absent.
- Prefixed account browser suite: **passed**, including registration/login, pending session lookup, profile unavailable/retry, unavailable neighborhood preservation, avatar handling/save/cancel, failed logout/retry, captured-mail password recovery and reused-link rejection.
- Prefixed existing profile browser suite: **passed**, including persisted profile changes across reload/server restart, navigation and account restrictions.
- Request-worker checks: **12 passed**.
- Mixed Sass/SCSS audit: **passed**; 26 CSS URLs, 245 inventory inline imports and 14 static-page stylesheets.
- Actual login/profile captures at **320px and 1280px** were inspected; the preserved mobile/desktop account layouts match the pre-conversion design. Browser geometry checks also pass at **390px and 768px**, with no page-level horizontal overflow and usable avatar modal controls.
- Normal final Jekyll build: **passed**, with 62 inherited warnings. Both the seven-group account suite and the existing profile persistence/navigation suite also **passed against the normal preview**. All requested normal/prefixed browser runs completed successfully.

These captures use synthetic accounts with external browser services blocked; missing inherited remote logos/footer assets are a controlled-test limitation, not a new Sass regression. Evidence is local in `/tmp/pnec-sass-review-2026-10-21/`.

All completed auth/profile fixes are preserved. No backend, auth JavaScript, unrelated styles, database, environment, deployment configuration, branch or remote settings are changed in this follow-up. No commit, push, merge or deployment was performed.
