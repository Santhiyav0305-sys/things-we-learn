# ML Cheat Sheet

## Problem types

| Task | Typical output | Examples |
|---|---|---|
| Regression | Continuous number | price, temperature |
| Classification | Class | spam/not spam |
| Clustering | Group/cluster ID | customer segments |
| Dimensionality reduction | Fewer features | PCA visualization |

## Basic workflow

```text
Define target
  ↓
Collect/inspect data
  ↓
Clean + feature engineering
  ↓
Train/validation/test split
  ↓
Baseline
  ↓
Train
  ↓
Evaluate
  ↓
Tune
  ↓
Error analysis
  ↓
Save + document
```

## Common metrics

Regression:
- MAE
- MSE
- RMSE
- R²

Classification:
- Accuracy
- Precision
- Recall
- F1
- ROC-AUC

Always select metrics based on the real problem and the cost of errors.
