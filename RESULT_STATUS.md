# Result-status audit

## Empirically reported in the manuscript
- Cohort counts and aggregate characteristics
- AUROC/AUPRC
- Sensitivity, specificity and F1
- Decision concordance, macro-F1 and normalized cost
- Action distributions
- Ablation results
- Aggregate robustness statistics
- Model-estimated transmission scenario values
- Expert explanation scores
- Reported confusion-matrix counts

## Not available from the manuscript
- Complete individual-level labels
- Exact infectiousness-labeling rule
- Held-out probability vectors
- Calibration-bin values
- Raw bootstrap replicates
- Complete temporal-window AUROC series
- Complete robustness-condition AUROC series
- Raw expert-level ratings

Do not generate these missing values from the aggregate statistics.
They must be recovered from the original analysis pipeline.
