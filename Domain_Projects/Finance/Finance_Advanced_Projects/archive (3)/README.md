Financial Sentiment with FinBERT (Analyst & News)
=================================================

Executive summary
-----------------
Sentiment analysis pipeline on analyst ratings and news headlines using FinBERT. Provides labeled sentiment scores for downstream equity research features and risk signals.

Business value
--------------
- Enrich fundamental and quant models with sentiment factors.
- Identify shifts in analyst tone and news momentum for early signal detection.

Data and provenance
-------------------
- Analyst ratings: `analyst_ratings_processed.csv` (large, local-only).
- News/headlines sample: `aapl_sentiment_analysis.csv`, `raw_partner_headlines.csv`.
- Sensitivity: text data only; ensure licensing/usage rights for news content.

Methodology
-----------
- Notebook: `Financial_Sentiment_FinBERT.ipynb` loads processed ratings and applies FinBERT for sentiment scoring.
- Models: Hugging Face `ProsusAI/finbert`; tokenization and batching for efficiency.
- Outputs: sentiment scores per headline/rating; class distributions for QA.

Reproducibility and environment
-------------------------------
- Install from notebook preamble: `%pip install transformers datasets torch scikit-learn pandas`.
- Set random seeds for any train/val splits if fine-tuning.
- Large CSVs are not committed; ensure local paths are correct in the notebook.

How to run
----------
1) Create/activate a virtual environment.
2) Place data files under `archive (3)/` or update the notebook paths.
3) Open `Financial_Sentiment_FinBERT.ipynb` and run cells: install deps → load data → score with FinBERT → inspect outputs.

Project structure
-----------------
```
archive (3)/
├── analyst_ratings_processed.csv      # Processed analyst notes (large)
├── raw_analyst_ratings.csv            # Raw inputs
├── raw_partner_headlines.csv          # Headlines corpus
├── aapl_sentiment_analysis.csv        # Sample scored headlines
└── Financial_Sentiment_FinBERT.ipynb  # Scoring and EDA workflow
```

Operational notes
-----------------
- Respect rate limits and licensing for any external data pulls.
- Consider batching and GPU acceleration for large corpora.
- Validate label balance; apply threshold tuning if converting scores to discrete classes.

Next steps
----------
- Add MLflow/W&B logging for experiments and outputs.
- Fine-tune FinBERT on domain-specific labeled subset if available.
- Export features for integration into downstream predictive models.
