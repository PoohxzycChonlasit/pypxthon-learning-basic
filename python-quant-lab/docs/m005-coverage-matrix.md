# M005 curriculum coverage and verification

This matrix distinguishes implemented material from material that has been
executed in the current isolated environment. It does not claim student
acceptance or score educational quality without an individual review.

Latest verified run on 2026-10-28: the core suite passed 22 tests in 178.440
seconds in a temporary copy; the standard-library foundation grader passed
5/5 and the reference/fixture tests passed 4/4 in temporary copies. The
package-dependent graders remain unrun because their dependencies are absent
from the isolated environment and installation has not been approved.
The project-local Python 3.12.10 `.venv` was checked and lacks `numpy`,
`pandas`, `matplotlib` and `plotly`; no packages were installed.

## Core curriculum and learning experience

| Area | Location | Automated evidence | Current finding |
|---|---|---|---|
| Stable curriculum | `curriculum.json`; 10 levels × 15 exercises | `tests/test_verify_lab.py` checks the catalog, assets, cases, prerequisites and assessment variants | 150 stable IDs retained |
| Student instructions | `exercises/level_XX/*.py`; `instructions/level_XX/*.md` for text answers | `tests/test_exercise_instructions.py` checks all 150 IDs, section presence, box width and execution of syntax examples | 138 Python boxes and 12 text-answer companions |
| Difficulty tiers | `curriculum.json` | Instruction test checks assigned tier mapping | Five relative tiers present; the assignment is structural and still needs an individual complexity review |
| Lessons, hints and Thai explanations | `lessons/`, `hints/`, `explanations/`, `solutions/` | Catalog test verifies files; solution tests execute reference behavior against fixed cases | Asset presence and reference behavior are machine-checked; hint usefulness and explanation quality are not individually scored |
| Grading and assessments | `tests/`, `tests/assessment/`, `practice.py` | Core regression checks reference solutions, unfinished starters, deliberate wrong answers, submission modes, progress and A/B assessment behavior | Automated correctness is covered by the regression suite; it does not establish mastery |
| First-use workflow | `practice.py`, `README.md` | Temporary-copy smoke test covers start/open/run/check/hint/solution/progress/next and text-answer companion flow | Windows VS Code CLI launch and file preservation passed in a temporary copy |

## Data Analysis coverage

The stable core remains runnable with the standard library. Deeper package
practice lives in the optional `tracks/data_analysis/` track so the existing
150 IDs and student starter files keep their current scope.

| Topic | Exercises and evidence | Status |
|---|---|---|
| Data/schema, CSV, JSON, SQLite and rejected-row reasons | DA01–DA05 in `foundations.py`; `grade_foundations.py` | Standard-library grader executed against reference implementation: 5/5 passed |
| NumPy arrays, selection, broadcasting and aggregation | DA06–DA09; `grade_numpy_pandas.py` | Implemented with grader; execution blocked because NumPy is absent from the isolated `.venv` and installation is not authorized |
| pandas Series/DataFrame, import, inspection, filtering, cleaning, joins and time-series features | DA10–DA17; `grade_numpy_pandas.py` | Implemented with grader; execution blocked because pandas and NumPy are absent from the isolated `.venv` |
| Business and OHLCV charts | DA18–DA19; `grade_visualization.py` | Implemented with deterministic data/label/artifact assertions; execution blocked because Matplotlib and pandas are absent from the isolated `.venv` |
| Business KPIs, net returns, costs, equity curve and drawdown | DA20–DA21; `grade_capstone.py` | Implemented with grader; execution blocked because pandas and NumPy are absent from the isolated `.venv` |
| CSV export and round trip | DA22; `grade_numpy_pandas.py` | Implemented with grader; execution blocked because pandas is absent from the isolated `.venv` |
| Interactive conversion chart | DA23; `grade_plotly_optional.py` | Optional extension implemented; execution blocked because Plotly and pandas are absent from the isolated `.venv` |

## Datasets and reproducibility

`data/generate_synthetic_datasets.py` uses fixed seeds and the standard
library. `tests/test_synthetic_datasets.py` verifies generated fixture
reproducibility, documented row counts and OHLCV invariants. The intentionally
dirty e-commerce fixture is separate from clean business and financial data;
all market-like data is synthetic, offline and has no exchange connection.
The documented set contains 19 CSV files and 6,796 data rows: the original
nine small fixtures (51 rows) plus ten generated datasets (6,745 rows).

## Quality-review boundary

The machine checks provide evidence for asset completeness, fixed-case
reference behavior, starter rejection, instruction structure and runnable
syntax examples. The requested individual 10-dimension educational rubric
(clarity, correctness, difficulty, prerequisites, relevance, syntax, hints,
solutions, grading and assessment integrity) has not been scored for all 150
exercises. The [per-exercise CSV ledger](m005-exercise-verification-ledger.csv)
marks manual review `NOT_VERIFIED`; no educational scores are inferred from
file existence or test passes.

Package-dependent graders are also not marked verified until they execute in
the project-local `.venv`. The exact approved-install command is documented in
the Data Analysis guide and main README.

## M006 independent curriculum quality audit

**Verified 2026-10-28.** This section supplements the M005 snapshot above; M005 statements remain historical. M006 audited all 150 core exercises and all 23 optional Data Analysis exercises individually, including each task, starter/instruction box, hint, reference solution and relevant oracle. The updated row-level evidence is in `docs/m005-exercise-verification-ledger.csv`; methods and findings are in `docs/m006-curriculum-quality-audit.md`.

| Area | M006 result | Evidence / boundary |
|---|---|---|
| Core curriculum | 150/150 AI reviewed; IDs, solution access, starter availability and metadata regressions pass | Core suite passed 27 tests. Human learner acceptance remains `NOT_VERIFIED`. |
| Rubric | Scores recorded for clarity, correctness, prerequisites, difficulty, relevance, syntax, hints, references, grading and assessment integrity | Scores are post-repair AI ratings: 2=meets, 1=usable limitation, 0=material failure, NA=not applicable. |
| Difficulty | 47 core tier assignments corrected; current counts are Tier 1: 27, Tier 2: 49, Tier 3: 43, Tier 4: 18, Tier 5: 13 | No equal-count constraint is imposed. Metadata/display consistency is checked by regression. |
| Core grading | Fixed reference cases and core CLI regressions pass | `py -3.12 -B -m unittest discover -s tests -p 'test_*.py' -v` — 27/27. This does not establish learner mastery. |
| First-use CLI | Start, open, unfinished check, hint, solution reveal, correct answer, progress persistence, assisted/independent status and starter preservation pass in temporary copies | The real checkout has no `progress.json`; smoke tests wrote progress only under temporary directories. The editor command was captured rather than launching a UI. |
| Data Analysis | 23/23 reviewed; six reference-backed grader suites pass, 43/43 tests in an isolated project copy | Python 3.11.9 already has NumPy 2.4.4, pandas 2.2.3, Matplotlib 3.10.8 and Plotly 6.3.1. No packages were installed. |
| Project virtual environment | `BLOCKED` for package graders until dependencies are installed | `.venv` is Python 3.12.10 and has none of the four packages. Global Python 3.12.10 has NumPy 2.5.1 and pandas 3.0.6. Package tests ran with existing global Python 3.11.9. Proposed command (not run): `.\.venv\Scripts\python.exe -m pip install -r requirements-optional.txt`. |
| Assessments | All ten final assessments have distinct A/B task prompts and reference behavior; shared lesson, hint and starter guidance follows the selected variant | L02–L10 B variants were rewritten within existing IDs, with distinct outputs and oracle cases. Regression asserts prompt/solution differences and hint/catalog alignment; learner mastery remains unverified. |
| Student work | No real `progress.json`; 156 starter-module function-body ASTs match the pre-audit baseline | No existing learner submission was found or overwritten. The working tree remains unstaged; cache hashes match the M006-start baseline. |
| Human acceptance | `NOT_VERIFIED` | No novice learner session was observed. |

**Environment discrepancy:** M003 reported NumPy/pandas in the ambient interpreter; M005 checked the project `.venv`. The current inventory confirms these are different environments. The exact M003 executable is not independently established, so this explanation is an evidence-backed inference.
