# Engineering Thinking and AI-Assisted Development

This compact companion track teaches how to understand and design a system
before asking a coding agent to implement a part of it. It complements the
150 core exercises; it does not replace or duplicate them. The worksheets
produce design artifacts, not another graded Python course.

## A repeatable workflow

1. **Decompose the problem:** name the user, goal, in-scope behavior and
   exclusions.
2. **Write requirements:** make each behavior observable and list assumptions
   that still need an owner decision.
3. **Define contracts and data:** state input, output, errors, record fields
   and invariants.
4. **Describe the algorithm:** write ordered steps or pseudocode before code.
5. **Choose boundaries:** decide which small modules or functions own each
   responsibility.
6. **Plan implementation and tests:** order the work and define normal,
   boundary and rejected-input cases.
7. **Delegate narrowly:** give an AI coding tool one bounded task with files,
   constraints and acceptance tests.
8. **Review the result:** inspect the diff, run tests, check assumptions and
   explain the implementation in your own words.

## Lessons

- [01 — Problem decomposition and requirements](lessons/01-problem-decomposition.md)
- [02 — Contracts, data models and algorithms](lessons/02-contracts-data-algorithms.md)
- [03 — Architecture, implementation planning and reliability](lessons/03-architecture-reliability.md)
- [04 — AI delegation, code review and verification](lessons/04-ai-delegation-review.md)

Each lesson includes a short type-along example. Type the example, predict its
output and change one input before continuing.

## Practical exercises

For each exercise, complete the design artifacts **before** asking an AI tool
for code. Then delegate one small step, review its diff and test it yourself.

- [Expense tracker](exercises/expense-tracker.md)
- [E-commerce order processor](exercises/ecommerce-order-processor.md)
- [CSV data analyzer](exercises/csv-data-analyzer.md)
- [Offline Quant Research Engine](exercises/offline-quant-research-engine.md)
- [Offline Paper Trading Bot](exercises/offline-paper-trading-bot.md)

## Completion check

For one exercise, keep a short record containing the requirements, input/output
contract, data model, pseudocode, implementation plan, at least three tests and
the review notes from one bounded AI delegation. You should be able to explain
what the agent changed and why each test is relevant.

All examples and system boundaries in this track are offline. No exchange,
broker, wallet, signing service or live-order endpoint is part of the work.
