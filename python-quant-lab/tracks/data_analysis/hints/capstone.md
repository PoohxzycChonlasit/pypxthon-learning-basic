# Hints — applied analysis

## DA20 — Business KPIs

1. Calculate revenue per transaction as quantity × unit price × (1 − discount rate).
2. Sum sessions and conversions separately; guard against a zero-session denominator.
3. Group revenue by customer segment and net inventory movement by SKU.

## DA21 — Offline financial metrics

1. Price changes from row `i` to `i+1` are forward returns; pair them with the supplied position for that interval.
2. Compute log returns from the positive price ratio and deduct fee per exposed position.
3. Build equity cumulatively, compare it with its running peak, and report drawdown as a nonpositive fraction.
