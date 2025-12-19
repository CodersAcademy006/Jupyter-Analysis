Optiver Realized Volatility Prediction
======================================

Executive summary
-----------------
Quantitative research project to forecast short-horizon realized volatility for equity order books (Kaggle Optiver). Combines feature extraction from limit order book and trade data with machine learning models to minimize RMSPE of volatility forecasts.

Business value
--------------
- Improves intraday risk sizing, market making spreads, and portfolio hedging decisions.
- Provides scalable feature pipeline for microstructure signals applicable across tickers.

Data and provenance
-------------------
- Source: Optiver Kaggle dataset (public). Parquet files in `book_train.parquet/` and `trade_train.parquet/`; labels in `train.csv`; sample submission in `sample_submission.csv`.
- Target: `target` column = realized volatility per `(stock_id, time_id)`.
- Data handling: large parquet files; keep outside version control; ensure local disk capacity.

Methodology
-----------
- Notebook `notebooks/Market_Microstructure_Analysis.ipynb` performs scanning, feature exploration, and baseline modeling.
- Feature ideas: order-book depth imbalances, realized spread, mid-price returns, volatility estimators, trade size imbalance, time-of-day effects.
- Models: gradient boosting (LightGBM/XGBoost/CatBoost) and potential deep tabular models; evaluate per-stock vs pooled models.
- Evaluation: RMSPE on holdout folds; consider grouped CV by `time_id` to avoid leakage.

Reproducibility and environment
-------------------------------
- Install dependencies from notebook preamble: `%pip install fastparquet nbformat>=4.2.0` plus chosen model libs.
- Set seeds for CV; document feature configs per experiment.
- For performance, consider Apache Arrow/Polars and caching intermediate parquet features.

How to run (notebook-driven)
----------------------------
1) Create/activate a virtual environment.
2) Ensure parquet files are available locally in the project root (or update paths in the notebook).
3) Open `notebooks/Market_Microstructure_Analysis.ipynb`; run the dependency cell, then feature extraction and modeling cells.
4) Export predictions to align with `sample_submission.csv` if submitting.

Project structure
-----------------
```
optiver-realized-volatility-prediction/
├── book_train.parquet/              # Limit order book snapshots
├── trade_train.parquet/             # Trades data
├── notebooks/
│   └── Market_Microstructure_Analysis.ipynb
├── train.csv                        # Labels
├── test.csv                         # Test metadata
└── sample_submission.csv
```

Operational notes
-----------------
- Use memory-efficient readers; process per stock to fit in RAM.
- Monitor data leakage (do not mix future `time_id` when training features for earlier windows).
- Track per-stock performance variance; consider hierarchical models if spread is wide.

Next steps
----------
- Build a reusable feature store and cached artifacts (per stock/time window).
- Add MLflow/W&B tracking and automated CV harness.
- Prototype deep sequence models (Transformers/TCNs) on order-book sequences for incremental uplift.
