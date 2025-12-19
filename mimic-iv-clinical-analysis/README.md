# MIMIC-IV ICU Mortality Prediction Pipeline

## Executive Summary
This repository implements an institutional-grade, end-to-end machine learning pipeline for ICU mortality prediction using the MIMIC-IV clinical database. The workflow is designed to meet the standards of quantitative research and risk modeling at top-tier financial and healthcare institutions.

## Key Features & Methodology

- **Robust ETL & Data Engineering:**
  - Automated extraction, transformation, and loading of high-dimensional, time-series clinical data.
  - Strict 24-hour filtering to ensure temporal validity and prevent look-ahead bias.
  - Explicit removal of target leakage variables (e.g., `deathtime`, `dod`, `discharge_location`, `hospital_expire_flag`, `los`).

- **Institutional-Grade Preprocessing:**
  - All imputation and feature engineering are performed using `sklearn` pipelines and `ColumnTransformer` objects.
  - Imputation statistics (e.g., medians) are fit exclusively on the training set and applied to the test set, eliminating data leakage.

- **Feature Aggregation & Engineering:**
  - Per-stay aggregation using `groupby('stay_id_x')` to preserve clinical granularity and avoid patient-level mixing.
  - Aggregation of vital signs and outcomes using advanced statistical metrics (mean, max, min, std).

- **Modeling & Validation:**
  - Binary classification via regularized Logistic Regression.
  - Stratified train/test split to maintain class balance and support robust out-of-sample validation.
  - AUROC and AUPRC metrics for discrimination and precision-recall assessment.

- **Advanced Model Diagnostics:**
  - **Calibration Curve (Reliability Diagram):** Quantitative assessment of probability calibration using `sklearn.calibration.calibration_curve`, with reference to the ideal diagonal.
  - **SHAP Beeswarm Plot:** Model explainability via SHAP values, leveraging `shap.LinearExplainer` for transparent feature attribution.

- **Professional Visualization:**
  - Missingness heatmaps, calibration curves, and SHAP summary plots for institutional reporting and auditability.

## Compliance & Best Practices
- All code adheres to strict anti-leakage protocols and is suitable for deployment in regulated environments (e.g., financial risk, clinical decision support).
- Modular structure (ETL, features, models, visualization) supports reproducibility, scalability, and audit trails.

## Usage
1. Place MIMIC-IV demo data in the appropriate `icu/` and `hosp/` folders.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the pipeline: `python run_pipeline.py`

## Contact
For institutional collaborations, audits, or technical inquiries, please contact the Lead Data Scientist.
# Scalable Multimodal ICU Pipeline: Sepsis Early Warning & Intervention Analysis

## Overview
This project demonstrates a scalable, reproducible pipeline for ICU data analysis, focusing on sepsis early warning and intervention efficacy. The architecture is modular and ready to scale to the full MIMIC-IV dataset.

## Objectives
- Robust ETL for irregular ICU time-series
- Causal inference for Vasopressor effect on AKI
- Predictive modeling (LSTM/GRU vs. Logistic Regression)
- Explainability with SHAP

## KPIs
- AUROC, AUPRC, Prediction Lead Time
- False Alarm Rate, Data Completeness Ratio

## Methodologies
- Descriptive patient flow, comorbidity networks
- Sliding window feature engineering
- Propensity Score Matching (PSM)
- Stratified K-Fold Cross Validation

## Visualizations
- Missingness Heatmap
- Sankey Diagram (Patient Flow)
- Spaghetti Plot (Vital Sign Trajectories)
- Love Plot (Covariate Balance)
- Calibration Curve
- SHAP Beeswarm Plot

## Repository Structure
```
src/
  etl/
    extract.py
    clean.py
    impute.py
  features/
    windowing.py
    aggregation.py
  models/
    baseline.py
    dynamic.py
    causal.py
    explain.py
  visualization/
    missingness.py
    sankey.py
    spaghetti.py
    love_plot.py
    calibration.py
    shap_plot.py
tests/
  test_features.py
  test_etl.py
  test_leakage.py
requirements.txt
README.md
LICENSE.txt
```

## Usage
1. Install dependencies: `pip install -r requirements.txt`
2. Run unit tests: `python -m unittest discover tests`
3. Use scripts in `src/` for ETL, feature engineering, modeling, and visualization.

## Notes
- Designed for scalability and reproducibility
- Modular code for easy extension
- Ready for deployment on full MIMIC-IV dataset
