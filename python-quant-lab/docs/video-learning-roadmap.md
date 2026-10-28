# Video Learning Roadmap

This roadmap connects study topics to existing Python Quant Lab material. It
orders learning and names a practice task; it is not a complete or official
video playlist. Earlier project materials did not identify video sources.
M006C verified selected links and retained `UNKNOWN` for unresolved entries.

## Verified local prerequisites

- [`PythonPhase1/`](../../PythonPhase1/) contains `basictest.py`, `input.py`,
  `operators.py`, `operators2.py` and `truefalse.py`. The local
  `ifelse_statement.py` file is empty. These are the observed files, not a
  complete or official syllabus.
- No `PythonPhase2/` directory or Phase 2 syllabus was found. Its contents and
  any video mapping remain `UNKNOWN`.
- The core course has ten levels and 150 exercises. The optional Data Analysis
  track starts with DA01–DA05, then lists NumPy, pandas and visualization work.
- External video references were `UNKNOWN` at the start of this reconciliation;
  see the topic rows and verification boundary below for the links now checked.

## Sequence and practice map

“Required” describes the course knowledge, not a requirement to watch a video.
All video viewing is optional; where video URLs are unknown, use the linked
local material and mark the video search as an open item.

| Topic | Prerequisites and when to study | Quant Lab support and next exercise | Course status | Video URL / timestamp |
|---|---|---|---|---|
| Python Phase 1 | No Python prerequisite. Study before Level 1 if the learner is new; skip or review if these basics are familiar. | Supports Level 1; try [L01-E001](../exercises/level_01/L01-E001.py). The local files demonstrate variables, input, operators and comparisons; the conditionals file is empty. | Python foundations are required; this external/local review is optional. | KongRuksiam, [เขียนโปรแกรมภาษา Python | สำหรับผู้เริ่มต้น [Phase1] (อัปเดตล่าสุด)](https://www.youtube.com/watch?v=HEqxgFyK77I); timestamp `UNKNOWN` |
| Python Phase 2 | Python Phase 1 or equivalent. Study after the beginner basics and before more involved Level 2–4 work. The local Phase 2 syllabus was not found. | Use the verified course bridge [L02-E010](../exercises/level_02/L02-E010.py); this is not claimed to be equivalent to an unknown Phase 2 syllabus. | External Phase 2 is optional and unverified. | `UNKNOWN / UNKNOWN` |
| Algorithms and pseudocode | Variables, conditions and simple lists; study before multi-step Level 2–5 tasks. | Supports Levels 2–5; try [L02-E010](../exercises/level_02/L02-E010.py), then design an [order processor](../tracks/engineering_thinking/exercises/ecommerce-order-processor.md). | Step-by-step algorithmic thinking is required in the core; a separate video is optional. | `UNKNOWN / UNKNOWN` |
| Git and GitHub | Basic files and terminal use; study before a multi-file project or AI delegation that returns a diff. | Supports Levels 5–10 and the [CSV analyzer worksheet](../tracks/engineering_thinking/exercises/csv-data-analyzer.md). No dedicated Git exercise exists in the core catalog. | Optional for the local core course; recommended for project work. | GitHub, [A brief introduction to Git for beginners](https://www.youtube.com/watch?v=r8jQ9hVA2qs); 5:52–8:29 (basic commands and Git/GitHub distinction) |
| SQL | Tables, rows and basic filtering; study after DA01–DA03 and before the SQLite exercise. | Supports optional Data Analysis DA04; see the [Data Analysis track](../tracks/data_analysis/README.md) and its [foundation exercises](../tracks/data_analysis/exercises/foundations.py). | Optional track topic; not required by the 150 core exercises. | freeCodeCamp.org, [SQL Tutorial for Beginners (and Technical Interview Questions Solved)](https://www.youtube.com/watch?v=-fW2X7fh7Yg); timestamp `UNKNOWN` |
| File I/O | Strings, paths and basic Python functions; study around Level 5 before handling local datasets. | Supports Level 5 and DA01–DA05; plan a [CSV analyzer](../tracks/engineering_thinking/exercises/csv-data-analyzer.md), then follow the [Data Analysis foundations](../tracks/data_analysis/exercises/foundations.py). | File handling is part of the core progression; an external video is optional. | Corey Schafer, [Python Tutorial: File Objects — Reading and Writing to Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM); timestamp `UNKNOWN` |
| Unit testing | Functions, conditions and exceptions; study after Level 4 and alongside Level 5 reliability work. | Supports Level 5 and later; write acceptance cases for the [order processor](../tracks/engineering_thinking/exercises/ecommerce-order-processor.md). There is no separate core exercise devoted only to authoring tests. | Testing concepts are part of the core learning path; an external video is optional. | pixegami, [How To Write Unit Tests in Python • Pytest Tutorial](https://www.youtube.com/watch?v=YbpKMIUjvK8); 04:14–11:24 (first test, assertions and exception checks) |
| NumPy | Python lists, indexing and arithmetic; study after DA01–DA05 and before array exercises. | Supports optional DA06–DA09; start at the [Data Analysis track](../tracks/data_analysis/README.md). | Optional package track. | Enthought, [Introduction to Numerical Computing with NumPy | SciPy 2019 Tutorial](https://www.youtube.com/watch?v=ZB7BZMhfPgk); timestamp `UNKNOWN` |
| pandas | Python records/collections; NumPy is useful preparation. Study after DA06–DA09. | Supports optional DA10–DA17; start at the [Data Analysis track](../tracks/data_analysis/README.md). | Optional package track. | Wes McKinney, [pandas in 10 minutes | Walkthrough](https://www.youtube.com/watch?v=_T8LGqJtuGc); timestamp `UNKNOWN` |
| Matplotlib | Basic tables and pandas DataFrames; study after the relevant inspection/cleaning work. | Supports optional DA18–DA19; continue from the [Data Analysis track](../tracks/data_analysis/README.md). | Optional package track. | Corey Schafer, [Matplotlib Tutorial (Part 1): Creating and Customizing Our First Plots](https://www.youtube.com/watch?v=UO98lJQ3QGI); timestamp `UNKNOWN` |
| Software Architecture | Functions, modules, requirements and error handling; study after Levels 4–5, before a multi-component project. | Supports Level 10 and the [offline Paper Trading Bot design](../tracks/engineering_thinking/exercises/offline-paper-trading-bot.md). | Optional companion topic; useful preparation, not a core-course gate. | `UNKNOWN / UNKNOWN` |
| AI Coding Workflows | Problem decomposition, contracts and tests; study after the first three [Engineering Thinking lessons](../tracks/engineering_thinking/README.md). | Supports work at any level; practice with the [offline Paper Trading Bot worksheet](../tracks/engineering_thinking/exercises/offline-paper-trading-bot.md). | Optional; students can complete the course without an AI coding tool. | OpenAI, [Getting started with Codex](https://www.youtube.com/watch?v=px7XlbYgk7I); 16:26–27:02 (prompting patterns) |
| Quant Research | Time-series handling, statistics and financial costs; study after Levels 6–8 and before Level 9. | Supports Levels 9–10; try [L09-E005](../exercises/level_09/L09-E005.py), then design the [Offline Quant Research Engine](../tracks/engineering_thinking/exercises/offline-quant-research-engine.md). | Quant research concepts are core at Levels 9–10; videos are optional. | `UNKNOWN / UNKNOWN` |

## Verification boundary

Exercise IDs and local track locations above were checked against the current
repository. On 2026-10-28, each linked video's title and identity were checked
against its YouTube result; the NumPy entry also appears in the [NumPy Learn
video list](https://numpy.org/learn/), and the pandas video is embedded on the
[pandas Getting Started page](https://pandas.pydata.org/getting_started.html).
Timestamps are included only where the video's chapter description supplied
them. Python Phase 2, algorithms, software architecture and quant research
remain `UNKNOWN`; no matching course or video was independently verified for
those rows. A video link does not establish equivalence with the local course
or an unavailable external syllabus.
