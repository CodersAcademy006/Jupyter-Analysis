# Home Credit Default Risk – EDA Highlights

## Top 5 Red Flags (from Cell 12 outputs)
- Missing EXT_SOURCE_1: applicants lacking this external score show higher default rates.
- Top 5% Credit-to-Income Ratio: heavy leverage cohort is riskier than the baseline.
- Top 10% Late-Payment Frequency: borrowers with frequent past lateness carry elevated risk.
- Age < 30 with current application: youngest applicants show higher default incidence.
- Retirement/Unemployment Flag & High Credit/Income (75p+): retired/unemployed markers combined with high leverage are especially risky.

## What’s Inside
- Integrity checks (365243 day anomalies, XNA/XAP codes) and target imbalance.
- External score correlations and missingness impact.
- Financial ratios (credit/income, annuity/income, credit/goods) split by default status.
- Behavioral history from previous applications, bureau, and installment payments.
- Demographic risk slices plus automated red-flag patterns and interaction feature ideas.
- Sankey diagram showing flow from previous application status (Approved/Refused) to current default outcome.

## How to Use
1. Open `home-credit-risk.ipynb` and run cells sequentially (imports first).
2. Execute the red-flag and summary cells to view the uplift tables and suspicious segments.
3. Use the Sankey cell to visualize the stickiness of past refusals into current defaults.

## Quick Value
This notebook is ready for portfolio demonstration: it surfaces actionable credit-risk signals without heavy preprocessing and highlights high-risk segments for modeling or policy review.
