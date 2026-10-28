# M006 — Independent Curriculum Quality Audit

**Date:** 2026-10-28

**Repository:** `F:\python for poohx`

**Project:** `F:\python for poohx\python-quant-lab`

**Status:** `PASS` for completion of the bounded audit and in-scope repairs; human learner acceptance is `NOT_VERIFIED`.

## Scope and verified baseline

The local branch is `main` at `77ac529caf7553075ca3187012c24ad915541c2b`, matching `origin/main`. The project contains 150 core exercises across 10 levels (138 Python-submission exercises and 12 text-answer exercises), plus 23 exercises in the optional Data Analysis track. Nineteen CSV fixtures contain 6,796 data rows. These counts were checked against the current files.

The M006-start checksum manifest covered 396 existing files. There was no learner `progress.json`. No student implementation was found in the exercise starters. A pre-edit manifest covered 156 core/track Python modules; their AST function bodies still match that baseline (0 body changes), and all 156 parse successfully. No `PythonPhase1` path changed. No file is staged; no commit, push, merge, deploy, install or trading operation was performed. Existing dirty M005/M004 work was preserved. The 41 tracked cache files already dirty against `HEAD` at M006 start have unchanged hashes against the M006-start manifest.

## Review method and rubric

Every core exercise was inspected individually across its task specification, starter/instruction box (or text-answer companion), hint, reference solution, explanation/lesson and relevant fixed-case oracle. Every Data Analysis exercise was reviewed against its task, exercise module, reference implementation, hints/explanations, data assumptions and grader. The ledger records the reviewed paths and row-specific findings. This is qualitative AI review, not human review.

Each applicable dimension is scored **after repairs**: **2** = the requirement is met with no material defect remaining; **1** = usable with a documented limitation; **0** = materially incorrect, misleading or unreliable; **NA** = not applicable. Historical M005 columns and values are preserved. The review ledger appends M006 fields and the 23 DA rows without rewriting M005 evidence.

| Dimension | Core score | Notes |
|---|---:|---|
| Instruction clarity | 2/2 | Ambiguous task text identified and corrected. |
| Technical correctness | 2/2 | Public contracts, examples, references and independent cases agree after repairs. |
| Prerequisite correctness | 2/2 | Core sequencing and track prerequisites reviewed against the curriculum path. |
| Difficulty appropriateness | 2/2 | 47 tier labels corrected to actual task complexity; distribution is intentionally uneven. |
| Real-world relevance | 2/2 | Scenarios reviewed for meaningful Python/data work. |
| Syntax explanation | 2/2 | Mismatched examples aligned; all syntax examples are exercised by the instruction regression. |
| Hint usefulness | 2/2 | Exact-answer leakage and misleading variant-specific hints corrected. |
| Reference solution | 2/2 | Core reference cases pass; L09-E005 compounding logic corrected and independently checked. |
| Grader reliability | 2/2 | Core suite and negative-answer checks pass; missing validation boundaries were added. |
| Assessment integrity | 2/2 across the 10 final assessments | A/B tasks, reference solutions and oracles are distinct. Shared lessons, hints and starter instructions now direct learners to the active variant prompt. Other exercises: NA. |

Data Analysis scores are recorded in the ledger. All 23 DA exercises score 2/2 on applicable dimensions; assessment integrity is NA because the optional track has no A/B final assessment forms. Package prerequisites and the project `.venv` gap are recorded separately from code correctness.

## Findings and repairs

- **Task/oracle consistency:** L01-E007 was underspecified and leaked its answer through lesson/hint text; L01-E013 documented a fee formula that contradicted negative-gross behavior; L02-E007 gave the wrong empty-input result; L02-E005 and L04-E005 lacked required invalid-input cases. These contracts, hints and independent grader cases were corrected.
- **Financial correctness:** L09-E005 summed simple returns instead of compounding them. The reference now compounds each period, and hand-computed oracle cases cover nonzero strategy/benchmark returns.
- **Instruction alignment:** 62 mismatched syntax examples were replaced with runnable examples for the concept actually used. L03-E005’s role, L05-E007’s task description, L10-E003’s function contract and L10-E012’s Thai text were also corrected.
- **Difficulty:** 47 core difficulty assignments were changed without replacing exercises. Counts are Tier 1: 27; Tier 2: 49; Tier 3: 43; Tier 4: 18; Tier 5: 13. The earlier exactly-equal distribution was a mechanical pattern, not an educational requirement.
- **Data Analysis validation:** DA01 now counts absent keys in the first-row schema; DA02 rejects blank/duplicate CSV headers; DA05 and DA13 reject non-finite values; DA19 validates finite OHLCV data; DA20/DA23 define zero-session outputs; and graders now cover relevant boundaries such as incompatible NumPy shapes, copy isolation, rolling gaps, unmatched joins and invalid costs. Exact rows and repairs are in the ledger.
- **Assessment independence:** L02–L10 E015 originally reused the same operation and solution AST across A/B. Their B forms now assess distinct tasks: sign aggregation, stable deduplication, two-value summary, structured code parsing, forward fill, median/range, return metrics, compounded returns, and validated paper selling. A/B prompts, reference solutions, and independent oracles remain under the existing IDs.
- **Assessment guidance alignment:** Shared objectives, pitfalls and starter boxes still described one task while A/B prompts differed; the single runtime hint list for L02–L10 described only B. Shared lesson text, hints and starter guidance are now variant-neutral, companion hint files match the CLI catalog, and a regression test checks all ten final assessments.

## Verification

- Core regression: `py -3.12 -B -m unittest discover -s tests -p 'test_*.py' -v` — **27 tests passed in 109.219 seconds**. This includes reference-case checks, M006 targeted repairs, CLI formats, wrong-answer rejection, assessment behavior and starter checks. It tests the shipped reference cases; it does not establish learner mastery.
- Instruction regression: `py -3.12 -m unittest tests.test_exercise_instructions -v` — **1 test passed**; all 150 IDs, instruction structure and runnable examples are checked.
- Data Analysis reference-backed grading, run from a temporary project copy with reference modules substituted only in that copy, Python 3.11.9: **43 tests passed across six suites** (foundations 9, foundation references 4, NumPy/pandas 20, visualization 3, capstone 5, optional Plotly 2). This validates references and graders, not the unfinished student starters.
- First-use smoke, temporary copies: **PASS** for Level 1 start, open-path dispatch, unfinished-answer rejection, hint, solution reveal, correct assisted answer, persisted attempts/status, independent correct answer and preservation of the edited starter. The editor dispatch was intercepted to avoid opening a UI; its target file path was verified. Assisted status was `PASSED_WITH_HELP` after 2 attempts; independent status was `PASSED_INDEPENDENTLY` after 1.
- `git diff --check` passes.

## Runtime and M003/M005 discrepancy

| Interpreter | Version | NumPy | pandas | Matplotlib | Plotly |
|---|---:|---:|---:|---:|---:|
| Global Python 3.12 | 3.12.10 | 2.5.1 | 3.0.6 | Missing | Missing |
| Global Python 3.11 | 3.11.9 | 2.4.4 | 2.2.3 | 3.10.8 | 6.3.1 |
| Project `.venv` | 3.12.10 | Missing | Missing | Missing | Missing |

M003’s statement that NumPy/pandas were available referred to the ambient Python environment; M005’s missing-package finding referred to the project `.venv`. Current interpreter inventory demonstrates that these environments differ. The exact M003 executable is not independently established from its stored summary, so this explanation is an inference. No packages were installed. Package-dependent graders ran with the already-available global Python 3.11.9 interpreter.

## Preservation and remaining limitations

The real project still has no `progress.json`. All mutating workflow tests wrote only to temporary copies. The 156 Python module function bodies are unchanged from the recorded pre-audit AST baseline. The working tree remains unstaged; pre-existing cache edits and M005/M004 files remain in place.

Human learner acceptance is **NOT_VERIFIED**. No novice session was observed. Package tests validate the references and graders in isolation; the project `.venv` still needs optional packages before a student selects it for DA06–DA23.

| Finding | Classification | Evidence |
|---|---|---|
| Core audit and targeted repairs | PASS | 150/150 core exercises reviewed; core regression passed 27/27. |
| Data Analysis reference-backed validation | PASS | 23/23 reviewed; 43/43 grader/reference tests passed in a temporary copy on Python 3.11.9. |
| A/B transfer independence and guidance across final assessments | PASS | All 10 A/B forms have distinct tasks and reference behavior. Shared lessons, hints and starter boxes are variant-neutral; regression checks assert task and solution differences plus hint/catalog alignment. |
| Package graders through project `.venv` | BLOCKED | NumPy, pandas, Matplotlib and Plotly are missing from that interpreter. The proposed install command above was not run. |
| Human learner acceptance | NOT_RUN | No novice session was conducted. |
| Exact M003 interpreter executable | UNKNOWN | Historical M003 summary did not establish the executable path; current interpreter checks explain the environment difference. |

**Environment status:** Data Analysis verification is `PASS` using the existing Python 3.11.9 environment. Running those package graders through the project `.venv` is `BLOCKED` until its optional dependencies are installed. The exact proposed command is below; it was not run:

```powershell
Set-Location -LiteralPath "F:\python for poohx\python-quant-lab"
.\.venv\Scripts\python.exe -m pip install -r requirements-optional.txt
```

## Exact next action

Run a first real learner session in PowerShell, then capture learner feedback:

```powershell
Set-Location -LiteralPath "F:\python for poohx\python-quant-lab"
py -3.12 -B practice.py start
py -3.12 -B practice.py open L01-E001
```

This report establishes AI review and automated behavior only; it does not claim real-user acceptance.

## M006C focused follow-up — 2026-10-28

This follow-up narrows the assessment evidence to L10-E015-B and preserves the
M006 audit as a historical record. The M006 A/B distinction and guidance checks
passed for the cases they covered; they did not exercise malformed quantity or
price values that fail conversion.

### Confirmed defect and repair

Before repair, `final_offline_bot_assessment` converted cash, position,
quantity and price in one `try` block. A `TypeError` or `ValueError` from an
order field returned zero balances, even when the original cash and position
were valid. The contract requires rejected events to preserve those balances.

The independent regression was first run against the old implementation:
`py -3.12 -B -m unittest discover -s tests -p test_l10_e015_accounting.py -v`
reported five failing subcases: invalid quantity string, invalid price string,
`None` quantity, `None` price and empty quantity. The valid sell and non-dict
cases passed. The implementation now parses account balances separately and
returns the parsed valid balances when order-field parsing or validation
rejects an event. The function signature and non-dict zero-balance behavior
remain unchanged; it performs no network or exchange operation.

The B assessment fixture retains its original positive and negative examples
and now contains 17 cases, including the original five plus 12 additional
explicitly expected malformed and non-finite order inputs. The independent
`tests/test_l10_e015_accounting.py` covers 15 rejected inputs, a successful
sell, and non-dict input. The expected outputs are specified in the tests and
fixture, independent of the reference implementation.

### Focused review and contract boundary

The variant B prompt, active-variant lesson output, starter instructions,
variant-neutral hints, explanation, reference solution, fixture selection,
grader and retry flow were checked together. The prompt still requires
rejected valid-account sell events to preserve balances; the B contract was
not loosened to make the reference pass. The existing Assessment A reference
and nearby Level 10 cash restoration/event-log exercises did not show the same
state-loss defect. No additional related repair was needed.

The prompt does not define how to represent malformed or non-finite
pre-existing cash/position state. The reference keeps its prior fallback for
values that cannot be converted; the explanation now records the unspecified
boundary without introducing new accounting rules. Human learner acceptance
remains `NOT_VERIFIED`.

### Verification performed for M006C

All mutating workflow tests ran against a temporary project copy with a sibling
`PythonPhase1` copy for documentation-link resolution. The live checkout had no
`progress.json`; baseline hashes were captured for 162 files under `answers/`
and `exercises/`.

- Independent regression: `py -3.12 -B -m unittest discover -s tests -p test_l10_e015_accounting.py -v` — **3 tests passed**, including 15 rejected-input subcases.
- Reference fixture and A/B checks: `py -3.12 -B -m unittest tests.test_verify_lab.LabIntegrity.test_all_reference_solutions_satisfy_all_cases tests.test_verify_lab.LabIntegrity.test_levels_two_through_ten_have_five_workflows_and_assessment_variants -v` — **2 tests passed**.
- Learner CLI A/B workflow: `py -3.12 -B -m unittest tests.test_verify_lab.LabIntegrity.test_cli_checks_each_added_format_and_each_assessment_variant -v` — **1 test passed** with the expanded B fixture.
- Full core suite: `py -3.12 -B -m unittest discover -s tests -p 'test_*.py' -v` — **35 tests passed in 135.546 seconds**.

### Video roadmap follow-up

Nine of 13 roadmap topics now have independently checked video titles and
URLs. Three timestamps are listed where video chapter descriptions supplied
them. Python Phase 2, algorithms, software architecture and quant research
remain `UNKNOWN`; no syllabus equivalence or human course acceptance is
claimed.
