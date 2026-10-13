# PNEC Sprint 3 audit and implementation plan

Audit date: October 13, 2026 (America/Los_Angeles). Branch: `team-capstone`.
Starting commit: `386f042d73245ec51baa1949dc078f11ba63defe`.

The nine issues and 31 project cards were inspected before editing. No duplicates
were found among #26–34. Task owners were verified through repository collaborator
records: Samanvi `samanviy17-crypto`, Joan `joankmie`, Ainsley `Ainsleyalbert`.
Parent issues initially had no assignees; development cards were assigned and Todo.

## Scope and ownership

Samanvi-authorized, AI-assisted implementation: parameterized quiz evaluation,
quiz edge tests, bounded JSON requests for profile/current-user/community API,
network documentation, and isolated synthetic browser verification. These changes
must not be described as independently authored student Create work.

Joan/Ainsley: inspect and smoke-test existing shared code; prepare specific plans
and remaining TODOs. Do not implement their proposed personal procedures, produce
personal reflections/videos, close their tasks, or claim they participated.
Their participation or explicit approval is required before completing those
personal development tasks. Production deployment, unrelated branches, merges,
private databases, and actual external services are outside this delivery.

The existing modified Makefile, frontend README, local preview script, and
untracked PREPAREDNESS.md, SCSS_MIGRATION.md, and test-auth.py are preserved with
SHA-256 checks. They are excluded from focused commits. Existing production
credentials and resident database are never used for these checks.

## Implementation sequence

1. Record a backend baseline and build the existing frontend using installed
   Jekyll 3; identify defects rather than treating historic test claims as runs.
2. #29: `app/services/preparedness_service.py`: add `evaluate_preparedness` and
   keep `assessment` as the compatibility wrapper used by quiz_submit and
   household_dict. Traverse the question collection explicitly, limit ordered
   recommendations, and handle an empty collection without division by zero.
   Extend tests/test_preparedness.py for scores, invalid values/keys, unchanged
   saved answers, and every boolean combination; generate trace tables.
3. #30: `assets/js/api/auth-api.js`: reusable `pnecJsonRequest` with abort deadline,
   typed HTTP/offline errors, safe non-JSON errors, and deadline cleanup. Reuse it
   in current-user/neighborhood/profile requests and preparedness-api.js. Retain
   checklist's existing item/version outbox and explicit retry; do not auto-retry
   writes. Test failed profile saves preserve form values, checklist recovery and
   older acknowledgement handling, and actual profile persistence on restart.
4. Prepare teammate handoffs below; run existing tests without claiming new
   personal development or complete security/copyright verification.
5. Run final backend, request-worker Chromium, real-API browser and Jekyll checks;
   capture genuine tested UI states with synthetic data. Record failures as well
   as later passes, environment, expected/actual results and evidence paths.
6. Create focused local commits after tests; append verified progress to the nine
   issue descriptions, set parent assignments, and preserve unrelated cards.
   Keep tasks open if personal learning/evidence remains missing.
7. Request approval to push code and publish the prepared screenshot/log evidence
   bundle. Never insert nonexistent public image or commit links.

## Teammate implementation handoff

### Joan #31 — signup logic

Baseline: routes/preparedness.py `tasks`, `task_dict`, `task_signup`, `task_close`;
community-tools.js `tasks(parent)`; tests/test_preparedness.py
`test_shifts_capacity_duplicate_claim_cancel_and_close` and
`test_shift_neighborhood_and_date_validation`. Existing atomic conditional update
reserves capacity. Repeated signup is idempotent; duplicate IntegrityError returns
409. Client eligibility is advisory. Sequential tests do not prove concurrency.

Joan TODO:

- Write a truth table for authenticated AND open AND future AND has-space AND
  NOT already-signed-up; identify Boolean gates and trace alternative branches.
- Develop `eligibleShifts(shifts, userId, now)` and call it in `tasks(parent)`;
  document her new procedure/list contribution. Keep server protections intact.
- Test empty opportunities, past/closed/full, duplicate, cancellation/re-signup,
  malformed IDs, and final-slot race with two independent database connections.
- Add a controlled concurrency test using isolated file SQLite or the actual
  intended database; assert exactly one new reservation and no count overflow.
- Explain debugging decisions in her own reflection and link her actual commits.

Acceptance: actual matrix and concurrency results, expected/actual counts, owned
procedure definition/call, meaningful parameters, bounded iteration, and review.
Until Joan participates and verifies these, keep #31 open/Todo.

### Joan #32 — copyright and security

Files: frontend pages/, assets/images/, LICENSE (if present), existing source
credits; backend routes/auth.py, services/auth_service.py, utils/auth_decorators.py,
app/config.py, Dockerfile, docker-compose.yml, nginx_for_flask_8425; frontend
api/auth-api.js and utils/errors.js. Existing auth tests are baseline coverage.

Joan TODO:

- Inventory each used external resource: creator, original URL, permission/license,
  attribution location, unresolved permission, and replacement/approval owner.
  README license statements alone do not license all embedded external assets.
- Inspect HTTPS termination and certificate configuration; verify actual deployed
  configuration only with authorized access. Local HTTP screenshots prove no TLS.
- Document public-key certificate/authentication/key establishment, symmetric TLS
  traffic encryption, password hashing, hosting, and authorization separately.
- Verify authentication/session and volunteer sensitive-data permission matrix
  using synthetic accounts. Map findings to a severity and fix/retest plan.

Acceptance: complete provenance decisions or explicit blockers, observed permission
matrix, reliable sources, and verified-versus-proposed configuration. No blanket
copyright/security certification; #32 remains open/Todo.

### Ainsley #33 — hazard filtering/data analysis

Files: community-tools.js `hazards(parent)` currently renders all authorized reports;
preparedness.py `hazards`, `hazard_dict`, `hazard_update`; service `scoped`;
models/operations.py `HazardReport`; test_preparedness.py
`test_hazard_routing_permissions_and_status`. Category/status/timestamp metadata
and server scoping exist. No hazard filter controls or summary percentages exist.

Ainsley TODO in separate iterations:

1. Personally implement `filterHazards(reports, filters)` for one filter and trace
   bounded list traversal; connect controls inside `hazards(parent)`.
2. Add type/neighborhood/status with AND semantics and optional filter behavior;
   preserve authorized-only input and timestamp display/timezone explanation.
3. Add count and percentage of authorized records with zero-denominator handling.
4. Test exact fixture IDs, none/one/many, combined filters, malformed input,
   three-of-five=60%, and large-data termination; compare loop bounds and write her
   own iteration/reflection record with commit/review evidence.

Acceptance: correct fixture results and summaries, clear empty state, finite
iteration, unchanged authorization, and Ainsley's personally verified increments.
Screenshot of report display cannot establish filtering completion. #33 open/Todo.

### Ainsley #34 — check-in privacy/cybersecurity

Files: preparedness.py `check_ins`, `checkin_dict`; service `scoped`;
utils/auth_decorators.py; models/operations.py `ResidentCheckIn`; config/nginx;
test_preparedness.py `test_checkins_neighborhood_privacy_and_removal` and auth tests.
Baseline scopes residents to their own record, coordinators to their neighborhood,
staff/admin to all. Writes derive neighborhood from the account, not client input.

Ainsley TODO:

- Write and execute the full role/ownership/neighborhood matrix, including no login,
  unassigned coordinator, other resident, other coordinator, staff and admin.
- Verify API reads/mutations directly, data minimization, and sanitized logs/errors.
- Inspect encryption in transit and at rest and key handling without copying
  secrets. SQLite file existence does not prove at-rest encryption.
- Document symmetric encryption versus hashing/encoding/access control; reproduce
  findings before proposing changes, and retest each authorized fix.

Acceptance: complete observed matrix, no private-data evidence exposure, findings
and fixes with retests, and accurate verified/unknown encryption inventory. Partial
smoke coverage is preparation only. #34 open/Todo.
