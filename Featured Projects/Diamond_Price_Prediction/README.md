# Diamond Price Prediction

**Author:** Data Science Portfolio  
**Date:** 2024  
**Tags:** Regression, Machine Learning, Feature Engineering

## Executive Summary

This project predicts diamond prices using machine learning regression models. Using a dataset of 53,940 diamonds with features including carat, cut, color, clarity, and physical dimensions, we developed and compared multiple regression models achieving an R² score of approximately 0.98.

## Problem Statement

Diamond pricing is complex and depends on multiple factors traditionally known as the "4 Cs": Carat, Cut, Color, and Clarity. This project aims to build a predictive model that can accurately estimate diamond prices based on these characteristics, enabling:
- Fair pricing assessment
- Market value prediction
- Investment decisions

## Dataset

- **Source:** Diamonds dataset
- **Size:** 53,940 samples
- **Features:** 10 columns
  - **Numerical:** carat, depth, table, price, x, y, z
  - **Categorical:** cut, color, clarity
- **Target Variable:** price (in USD)

## Methodology

1. **Data Cleaning and Preprocessing**
   - Removed dimensionless diamonds (x, y, z = 0)
   - Handled outliers
   - Feature engineering

2. **Exploratory Data Analysis**
   - Distribution analysis
   - Correlation studies
   - Feature relationships visualization

3. **Feature Engineering**
   - One-hot encoding for categorical variables
   - Feature scaling using StandardScaler
   - Dimensionality reduction consideration

4. **Model Development**
   - Linear Regression (baseline)
   - Decision Tree Regressor
   - Random Forest Regressor
   - XGBoost Regressor
   - K-Nearest Neighbors

5. **Model Evaluation**
   - Cross-validation
   - RMSE comparison
   - R² score analysis

## Key Findings

1. **Carat is the strongest predictor** of diamond price, showing strong positive correlation
2. **Cut quality significantly impacts** price, with Ideal cuts commanding premium prices
3. **Physical dimensions** (x, y, z) are highly correlated with carat and provide redundant information
4. **Ensemble methods** (Random Forest, XGBoost) outperform linear models
5. **Model achieves ~98% R²**, indicating excellent predictive power

## Results Summary

### Model Performance

| Model | R² Score | RMSE | Notes |
|-------|----------|------|-------|
| Linear Regression | 0.91 | ~$1,200 | Good baseline |
| Decision Tree | 0.95 | ~$900 | Prone to overfitting |
| Random Forest | 0.98 | ~$550 | Best performance |
| XGBoost | 0.98 | ~$560 | Comparable to RF |
| KNN | 0.93 | ~$1,000 | Computationally expensive |

*Note: Exact values may vary with random seeds*

## Technical Stack

- **Data Processing:** pandas, numpy
- **Visualization:** matplotlib, seaborn, plotly
- **Machine Learning:** scikit-learn, xgboost
- **Feature Engineering:** StandardScaler, OneHotEncoder

## Conclusions

1. Machine learning models can accurately predict diamond prices with high precision
2. Ensemble methods (Random Forest, XGBoost) provide the best performance
3. The 4 Cs remain the most important features, with carat being dominant
4. Model is production-ready for price estimation and valuation tasks

## Future Work

- Incorporate market trends and temporal data
- Add more features (brand, certification source)
- Develop price range predictions with confidence intervals
- Deploy as web service for real-time predictions
- A/B testing with actual market data

## How to Run

```bash
# Navigate to project directory
cd "Featured Projects/Diamond_Price_Prediction"

# Ensure data is in data/ subdirectory
ls data/diamonds.csv

# Run notebook
jupyter notebook Diamond_Price_Prediction.ipynb
```

## Dependencies

See `requirements.txt` in repository root.