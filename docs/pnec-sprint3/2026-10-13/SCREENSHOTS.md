# Authentic local screenshot evidence

October 13, 2026; team-capstone. Captured with synthetic data and the code later committed as e33fc38. Failure screenshots are controlled local simulations, not production incidents. Shared-feature screenshots do not establish teammates’ personal authorship.

## quiz-interface.png

Ten-question quiz before answering, synthetic authenticated resident.

![Ten-question quiz before answering, synthetic authenticated resident.](screenshots/quiz-interface.png)

## quiz-0-of-10.png

Actual API result 0/10 = 0%, with returned recommendation text.

![Actual API result 0/10 = 0%, with returned recommendation text.](screenshots/quiz-0-of-10.png)

## quiz-5-of-10.png

Actual API result 5/10 = 50%, with returned recommendation text.

![Actual API result 5/10 = 50%, with returned recommendation text.](screenshots/quiz-5-of-10.png)

## quiz-10-of-10.png

Actual API result 10/10 = 100%, with returned recommendation text.

![Actual API result 10/10 = 100%, with returned recommendation text.](screenshots/quiz-10-of-10.png)

## checklist-persisted.png

Water remains checked after reload; isolated database value verified true.

![Water remains checked after reload; isolated database value verified true.](screenshots/checklist-persisted.png)

## checklist-server-error.png

Simulated HTML 502: useful error shown and unchecked water retained locally; not a production incident.

![Simulated HTML 502: useful error shown and unchecked water retained locally; not a production incident.](screenshots/checklist-server-error.png)

## checklist-offline-pending.png

Simulated disconnected preparedness API after reload; pending water=false survives.

![Simulated disconnected preparedness API after reload; pending water=false survives.](screenshots/checklist-offline-pending.png)

## checklist-recovered.png

Explicit Retry account save succeeds; isolated database now water=false.

![Explicit Retry account save succeeds; isolated database now water=false.](screenshots/checklist-recovered.png)

## profile-failed-save-draft.png

Simulated profile HTML 502 preserves the current form draft and re-enables Save.

![Simulated profile HTML 502 preserves the current form draft and re-enables Save.](screenshots/profile-failed-save-draft.png)

## volunteer-available.png

Existing shared volunteer UI: synthetic shift has 0/1 slots claimed.

![Existing shared volunteer UI: synthetic shift has 0/1 slots claimed.](screenshots/volunteer-available.png)

## volunteer-signed-up.png

Existing shared signup behavior: synthetic resident claims the single slot.

![Existing shared signup behavior: synthetic resident claims the single slot.](screenshots/volunteer-signed-up.png)

## volunteer-cancelled.png

Existing shared cancellation behavior restores availability; no new Joan implementation.

![Existing shared cancellation behavior restores availability; no new Joan implementation.](screenshots/volunteer-cancelled.png)

## hazard-existing-metadata.png

Existing shared report display contains neighborhood/category/status/timestamp; filter controls and summary analysis are not implemented.

![Existing shared report display contains neighborhood/category/status/timestamp; filter controls and summary analysis are not implemented.](screenshots/hazard-existing-metadata.png)

## checkin-other-resident-restricted.png

Existing authorization: another synthetic resident sees no check-ins; direct API returns an empty scoped list.

![Existing authorization: another synthetic resident sees no check-ins; direct API returns an empty scoped list.](screenshots/checkin-other-resident-restricted.png)

## checkin-login-required.png

Guest UI requires sign-in; separate direct unauthenticated API request returned 401.

![Guest UI requires sign-in; separate direct unauthenticated API request returned 401.](screenshots/checkin-login-required.png)

