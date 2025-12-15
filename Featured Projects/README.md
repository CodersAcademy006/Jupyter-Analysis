# Featured Projects

This directory contains the top 3 showcase projects demonstrating advanced data science capabilities.

## Projects

### 1. Diamond Price Prediction
**Category:** Regression | **Difficulty:** Intermediate

Predicting diamond prices using multiple regression models including Random Forest, XGBoost, and Linear Regression. Features comprehensive EDA, feature engineering, and model comparison.

**Key Skills:**
- Feature engineering
- Model comparison and selection
- Regression modeling
- Data visualization

**Files:**
- `Diamond_Price_Prediction/Diamond_Price_Prediction.ipynb` - Main analysis
- `Diamond_Price_Prediction/data/diamonds.csv` - Dataset (53,940 diamonds)

---

### 2. Ethereum Price Forecasting with LSTM
**Category:** Time Series / Deep Learning | **Difficulty:** Advanced

Deep learning-based cryptocurrency price prediction using LSTM neural networks. Demonstrates time series preprocessing, LSTM architecture design, and forecasting evaluation.

**Key Skills:**
- LSTM neural networks
- Time series forecasting
- TensorFlow/Keras
- Financial data analysis

**Files:**
- `Ethereum_LSTM_Forecasting/Ethereum_prediction_using_LSTM_model.ipynb` - Main analysis
- `Ethereum_LSTM_Forecasting/data/` - Historical Ethereum data

---

### 3. Genshin Impact Sentiment Analysis
**Category:** NLP / Deep Learning | **Difficulty:** Advanced

Sentiment analysis on gaming community data using NLP techniques including text preprocessing, SMOTE for imbalanced data, and classification models.

**Key Skills:**
- Natural Language Processing
- Sentiment analysis
- Imbalanced data handling (SMOTE)
- Text preprocessing and cleaning

**Files:**
- `Genshin_Sentiment_Analysis/sentiment-analysis-genshin-impact.ipynb` - Main analysis
- `Genshin_Sentiment_Analysis/data/` - Social media data

---

## Running the Projects

1. Ensure all dependencies are installed:
   ```bash
   pip install -r ../requirements.txt
   ```

2. Navigate to the project directory:
   ```bash
   cd "Featured Projects/Diamond_Price_Prediction"
   ```

3. Launch Jupyter:
   ```bash
   jupyter notebook Diamond_Price_Prediction.ipynb
   ```

## Performance Metrics

| Project | Primary Metric | Performance |
|---------|---------------|-------------|
| Diamond Price Prediction | R² Score | ~0.98 |
| Ethereum LSTM | RMSE | Varies by timeframe |
| Genshin Sentiment | Accuracy | ~85% |

*Note: Exact metrics may vary with different random seeds and data splits.*