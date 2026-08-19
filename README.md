# EduGuard-KG

Reproducibility repository for the manuscript **EduGuard-KG: temporal
knowledge graph-based decision support for school-based infectious
disease management**.

## Repository status

This repository contains the **aggregate results reported in the manuscript**
and a clearly labelled illustrative sample schema.

It does **not** contain the protected student-level school-health dataset.

## Reported aggregate result files

- `results/cohort_summary_reported.csv`
- `results/predictive_performance_reported.csv`
- `results/decision_performance_reported.csv`
- `results/action_distribution_reported.csv`
- `results/ablation_reported.csv`
- `results/robustness_summary_reported.csv`
- `results/transmission_scenario_reported.csv`
- `results/confusion_matrix_reported.csv`
- `results/explainability_reported.csv`
- `results/statistical_comparisons_reported.csv`

## Data

`data/sample_labels_illustrative.csv` is synthetic and is included only
to demonstrate the schema. It must not be used as the empirical study
dataset.

The individual-level dataset is not reproduced here because the manuscript
describes longitudinal school-health information concerning children.
Any release of individual-level data requires authorization from the
responsible data custodian and the applicable ethics/data-governance
approval.

## Important reproducibility limitations

The manuscript currently reports aggregate AUROC/AUPRC values and several
aggregate evaluation statistics. It does not provide:

1. the complete 109,816-row student-day dataset;
2. the complete deterministic rule used to generate the 12,723 positive
   infectiousness labels;
3. the held-out model probability vectors;
4. threshold-level ROC/PR coordinates;
5. bin-level calibration data;
6. window-level temporal stability values;
7. condition-level robustness values;
8. full bootstrap replicate outputs.

Therefore, these files should not be represented as a complete replication
package until the original experimental outputs are supplied.

## Reported headline values

EduGuard-KG:

- AUROC: 0.89 (95% CI 0.87--0.91)
- AUPRC: 0.48
- Sensitivity: 0.74
- Specificity: 0.81
- F1-score: 0.61
- Guideline concordance: 0.81 (95% CI 0.79--0.83)
- Macro-F1: 0.75
- Normalized decision cost: 0.70
- Model-estimated secondary infections: 2.4 per school day
- Explainability: plausibility 4.2/5; guideline consistency 4.4/5;
  usefulness 4.1/5; Fleiss' kappa 0.62

## Responsible-use note

The transmission results are parameterized scenario estimates and are not
observed infection counts or causal evidence of reduced transmission.
The system was evaluated retrospectively and should not be represented as
an autonomous clinical or administrative decision-maker.
