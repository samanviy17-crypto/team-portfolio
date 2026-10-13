# Executed quiz algorithm traces

October 13, 2026; branch team-capstone; starting SHA 386f042d73245ec51baa1949dc078f11ba63defe plus working changes.

AI-generated verification tables, not evidence of Samanvi’s timed practice or independent authorship. Each table uses the current question order and checks the procedure output.

## 0/10 ready

| Index | Question ID | Answer | Running ready count | Recommendations collected |
| --- | --- | --- | --- | --- |
| 0 | kit | False | 0 | kit |
| 1 | water | False | 0 | kit, water |
| 2 | food | False | 0 | kit, water, food |
| 3 | medications | False | 0 | kit, water, food |
| 4 | route | False | 0 | kit, water, food |
| 5 | meeting | False | 0 | kit, water, food |
| 6 | contacts | False | 0 | kit, water, food |
| 7 | alerts | False | 0 | kit, water, food |
| 8 | pets | False | 0 | kit, water, food |
| 9 | practice | False | 0 | kit, water, food |

Expected/actual score: **0% / 0% — PASS**.

Returned recommendations:
- Review and complete your emergency kit checklist.
- Review the water section of your kit.
- Review the food section of your kit.

## 5/10 ready

| Index | Question ID | Answer | Running ready count | Recommendations collected |
| --- | --- | --- | --- | --- |
| 0 | kit | True | 1 | none |
| 1 | water | True | 2 | none |
| 2 | food | True | 3 | none |
| 3 | medications | True | 4 | none |
| 4 | route | True | 5 | none |
| 5 | meeting | False | 5 | meeting |
| 6 | contacts | False | 5 | meeting, contacts |
| 7 | alerts | False | 5 | meeting, contacts, alerts |
| 8 | pets | False | 5 | meeting, contacts, alerts |
| 9 | practice | False | 5 | meeting, contacts, alerts |

Expected/actual score: **50% / 50% — PASS**.

Returned recommendations:
- Save a household meeting point below.
- Add a printed contact list to your kit.
- Review the preparedness resources and local alert links.

## 10/10 ready

| Index | Question ID | Answer | Running ready count | Recommendations collected |
| --- | --- | --- | --- | --- |
| 0 | kit | True | 1 | none |
| 1 | water | True | 2 | none |
| 2 | food | True | 3 | none |
| 3 | medications | True | 4 | none |
| 4 | route | True | 5 | none |
| 5 | meeting | True | 6 | none |
| 6 | contacts | True | 7 | none |
| 7 | alerts | True | 8 | none |
| 8 | pets | True | 9 | none |
| 9 | practice | True | 10 | none |

Expected/actual score: **100% / 100% — PASS**.

Returned recommendations:
- None; UI encourages reviewing and practicing the plan.

## Parameter and complexity explanation

`answers` determines readiness; `questions` determines which records are processed and the denominator; `recommendation_limit` controls the displayed action count. `assessment(answers)` calls the procedure with QUIZ, and quiz_submit/household_dict call assessment. The bounded loop initializes state, selects per boolean answer, appends limited actions, then returns a zero-safe percentage. Adding question records changes data rather than requiring copied variables and branches.

Input validation remains at the API boundary: exact quiz keys and booleans only. Invalid requests cannot overwrite previously saved answers. Unknown keys do not contribute to direct helper scoring. Empty questions yield 0% and no actions.

Personal Create selection, review/understanding, timed tracing practice, personal reflection, genuine analytics, PPR and video remain outstanding.
