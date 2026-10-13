# PNEC Sprint 3 delivery — October 13, 2026

Branch: `team-capstone`. Starting commit: `386f042d73245ec51baa1949dc078f11ba63defe`.
AI-assisted code commits (local, not yet pushed):

- `b8bae2149da8b2ca87f9a2ac5cbb3191198e0759`: parameterized quiz evaluation and edge/regression tests.
- `e33fc38f6a633b24feb8991f17d8ccdd06d0c78b`: bounded JSON requests and synthetic browser verification.

## Actual implementation

`evaluate_preparedness(answers, questions, recommendation_limit)` replaces compact
scoring with an explicit bounded traversal. It calculates ready percentage from
question records, limits ordered missing-action recommendations, ignores unrelated
keys for scoring, and handles zero questions. The existing assessment wrapper and
API shape remain. API validation still requires all ten exact boolean keys.

`pnecJsonRequest` bounds fetch/body reading to 15 seconds, supplies typed HTTP and
offline/timeout errors, handles HTML/non-JSON errors safely, and cleans up timers.
Profile, current-user, neighborhood and community requests reuse it. Checklist's
existing versioned outbox and explicit retry are retained. No automatic write
retry, deployment or new teammate-owned algorithm was added.

Files changed by this delivery:

- `Beasts_Flask/app/services/preparedness_service.py`
- `Beasts_Flask/tests/test_preparedness.py`
- `Beasts_FrontEnd/assets/js/api/auth-api.js`
- `Beasts_FrontEnd/assets/js/api/preparedness-api.js`
- `Beasts_FrontEnd/scripts/test-request-worker.py` (new)
- `Beasts_FrontEnd/scripts/verify-sprint3.py` (new)
- This evidence directory: plans, network notes, traces, run records, logs, screenshots.

Existing modified/untracked Makefile, frontend README, preview script,
PREPAREDNESS.md, SCSS_MIGRATION.md and test-auth.py are unchanged byte-for-byte and
excluded from commits. No real database, credential, .env or resident data is
included. Tests use synthetic accounts and reports, mock external weather, and
block external browser services. No PR or repository merge was performed.

## Verification

See [test-records.json](test-records.json) for date, branch/SHA, scenario, expected,
actual, pass/fail and evidence; [run metadata](run-metadata.json) records source
hashes. Initial checks ran at the starting SHA plus working changes; source bytes
were subsequently committed unchanged. The final backend JUnit run identifies
all individual cases at the code commit. The initial Jekyll build completed while
code changes were being made; served request-worker bytes were checked against
the committed files. It is not presented as a pristine baseline build.

| Check | Actual result | Evidence |
| --- | --- | --- |
| Existing backend baseline | 120 passed, 0 failed | [log](logs/backend-baseline.txt) |
| Expanded backend before commit | 133 passed, 0 failed | [log](logs/backend-final.txt) |
| Final committed backend | 133 passed, 0 failed | [log](logs/backend-final-committed.txt), [per-case JUnit](logs/backend-cases.xml) |
| Quiz answer combinations | All 1,024 combinations asserted inside one passed backend test | test_parameterized_quiz_collection_limits_and_all_answer_combinations |
| Controlled-transport Chromium | 11 passed, 0 failed | [log](logs/request-worker.txt) |
| Focused real-API browser scenarios | 12 passed, 0 failed | [log](logs/sprint3-browser.txt), [scenario outputs](browser-cases.json) |
| Existing community browser workflow | Passed; script exit 0 | [log](logs/community-browser.txt) |
| Existing profile browser workflow | Passed, including isolated DB/server restart | [log](logs/profile-browser.txt) |
| Quiz algorithm traces | 0%, 50%, 100% and recommendations verified | [tables](QUIZ-TRACES.md), [log](logs/quiz-traces.txt) |
| Jekyll 3 build | Passed with 62 existing warnings/deprecations | [log](logs/build-baseline.txt) |
| Initial screenshot run | Failed after first three quiz cases: nonexistent selector | [retained failure](logs/sprint3-browser-initial-failure.txt) |
| Screenshot rerun | Selector corrected; all 12 scenarios passed | [rerun](logs/sprint3-browser.txt) |
| Baseline HTML 502 | SyntaxError reproduced, now covered by passing useful-error case | [reproduction](logs/request-baseline-reproduction.txt) |

Do not sum scenario/flow counts into a single test total; they measure different
units and include repeated verification. Existing SQLAlchemy/datetime warnings
and `/api/announcements` 404 remain inherited limitations. Node is unavailable;
Chromium executes the modified JavaScript and browser regressions instead. Node
module test suites were not run or claimed passed. Production TLS, database
concurrency, SMTP, live chat/weather, real payments, complete role matrix and
organization acceptance were not verified.

## Screenshot evidence

[Captioned gallery](SCREENSHOTS.md), [machine-readable inventory](screenshots.json).
Fifteen genuine Chromium captures of tested states. The 502/offline states are
explicit local failure simulations. Shared volunteer/hazard/check-in captures
show baseline behavior, not Joan/Ainsley personal work. Hazard filter controls and
summary percentages do not exist and were not fabricated. Screenshots/logs are
committed locally for review; no publicly accessible new evidence URL exists
until publication is approved and succeeds.

## Issues and board

| Owner | Issue | Status after audit |
| --- | --- | --- |
| samanviy17-crypto | [#28 analysis/Create/retrospective](https://github.com/samanviy17-crypto/team-portfolio/issues/28) | In Progress |
| samanviy17-crypto | [#29 quiz](https://github.com/samanviy17-crypto/team-portfolio/issues/29) | In Progress |
| samanviy17-crypto | [#30 network](https://github.com/samanviy17-crypto/team-portfolio/issues/30) | In Progress |
| joankmie | [#26 analysis/Create/retrospective](https://github.com/samanviy17-crypto/team-portfolio/issues/26) | Backlog |
| joankmie | [#31 signup](https://github.com/samanviy17-crypto/team-portfolio/issues/31) | Todo |
| joankmie | [#32 copyright/security](https://github.com/samanviy17-crypto/team-portfolio/issues/32) | Todo |
| Ainsleyalbert | [#27 analysis/Create/retrospective](https://github.com/samanviy17-crypto/team-portfolio/issues/27) | Backlog |
| Ainsleyalbert | [#33 filtering](https://github.com/samanviy17-crypto/team-portfolio/issues/33) | Todo |
| Ainsleyalbert | [#34 check-in/security](https://github.com/samanviy17-crypto/team-portfolio/issues/34) | Todo |

Engineering changes for #29/#30 are locally verified. Those cards remain open
because student review/learning evidence, personal reflection, and publication
remain incomplete. Teammate cards remain open without new personal development.
All original descriptions/comments/flowcharts/links/checklist states are preserved;
new verified progress is appended, with no unrelated card edits or duplicates.

## Remaining human evidence and approvals

Samanvi: genuine AP Classroom Big Idea counts/link requested; independently review
and explain AI-assisted code, perform timed tracing practice, record personal
reflection, select eligible new Create work with the teacher, and personally
prepare video/PPR. Agent trace tables are verification, not personal practice.

Joan: personally complete signup procedure/truth table/concurrency verification and
resource-permission/security review; provide her own analytics/reflection/video/PPR.

Ainsley: personally complete incremental filters/summary calculations and full
check-in role/privacy/encryption review; provide her own analytics/reflection/video/PPR.

See [file-specific teammate plans](PLAN.md). No independent student artifacts or
assessment strengths/results were invented. Current College Board directions
were consulted; see [student handout](https://apcentral.collegeboard.org/media/pdf/ap-csp-student-task-directions.pdf)
and [collaboration/active contribution guidance](https://apcentral.collegeboard.org/courses/ap-computer-science-principles/course/faq/collaboration-limits-performance-tasks).

Approval is required by the user's Phase 9 before pushing local commits or
publishing the screenshot/log evidence bundle. Issue text and board updates are
explicitly authorized; they list local paths without pretending those paths are
already accessible on GitHub. No deployment is proposed.
