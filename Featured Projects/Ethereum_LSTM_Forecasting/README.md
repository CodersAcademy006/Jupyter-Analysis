# Ethereum Price Forecasting with LSTM

**Author:** Data Science Portfolio  
**Date:** 2024  
**Tags:** Deep Learning, Time Series, LSTM, Cryptocurrency

## Executive Summary

This project uses Long Short-Term Memory (LSTM) neural networks to forecast Ethereum cryptocurrency prices. Using historical price data from April-June 2018, we developed a deep learning model capable of predicting future price movements based on temporal patterns.

## Problem Statement

Cryptocurrency markets are highly volatile and influenced by numerous factors. This project aims to:
- Predict Ethereum price movements using historical data
- Demonstrate time series forecasting with deep learning
- Evaluate LSTM effectiveness for financial forecasting

## Dataset

- **Source:** CoinMarketCap historical data
- **Period:** April 7, 2018 - June 6, 2018
- **Features:**
  - timeOpen, timeClose, timeHigh, timeLow
  - open, high, low, close prices
  - volume, marketCap
- **Target:** Close price prediction

## Methodology

1. **Data Preprocessing**
   - Date-time conversion and parsing
   - Feature scaling using MinMaxScaler
   - Sequence creation for time series

2. **Exploratory Analysis**
   - Price trend visualization
   - Volume analysis
   - Statistical properties (skewness, kurtosis)

3. **LSTM Architecture**
   - Input layer with sequence data
   - LSTM layers with dropout for regularization
   - Dense output layer for price prediction
   - L2 regularization to prevent overfitting

4. **Model Training**
   - Train-test split (temporal)
   - Early stopping
   - Learning rate optimization

5. **Evaluation**
   - RMSE (Root Mean Square Error)
   - MAE (Mean Absolute Error)
   - R² Score
   - Visual comparison of predictions vs actuals

## Key Findings

1. **LSTM captures temporal dependencies** in cryptocurrency prices
2. **High volatility periods** are more challenging to predict
3. **Volume and market cap** provide additional predictive signals
4. **Model performs better** on stable price movements than sudden spikes
5. **Regularization is crucial** to prevent overfitting on crypto data

## Technical Stack

- **Deep Learning:** TensorFlow, Keras
- **Data Processing:** pandas, numpy
- **Visualization:** matplotlib, seaborn, plotly
- **Preprocessing:** scikit-learn (MinMaxScaler)
- **Network Architecture:** Sequential LSTM with Dropout and L2 regularization

## Architecture Details

```python
Model: Sequential LSTM
- LSTM(128, return_sequences=True, regularizers=l2(0.01))
- Dropout(0.2)
- LSTM(64, return_sequences=False)
- Dropout(0.2)
- Dense(1)
```

## Results Summary

### Model Performance

- **Training Performance:** Model converges well on training data
- **Validation Performance:** RMSE varies based on market volatility
- **Prediction Accuracy:** Better on trend prediction than exact values

### Visualizations

The project includes comprehensive visualizations:
- Price trend over time
- Predicted vs actual prices
- Error distribution
- Feature correlations

## Challenges & Limitations

1. **Market Volatility:** Crypto markets are extremely volatile, making long-term predictions difficult
2. **External Factors:** News, regulations, and market sentiment not captured in price data alone
3. **Limited Historical Data:** Only 2 months of data limits pattern learning
4. **Overfitting Risk:** Small dataset requires careful regularization

## Conclusions

1. LSTM networks can learn temporal patterns in cryptocurrency prices
2. Short-term predictions (1-2 days) are more reliable than long-term
3. Additional features (sentiment, market indicators) would improve accuracy
4. Model serves as a foundation for more sophisticated trading strategies

## Future Work

- Incorporate sentiment analysis from social media
- Add technical indicators (RSI, MACD, Bollinger Bands)
- Implement attention mechanisms
- Multi-step ahead forecasting
- Ensemble with other models (ARIMA, Prophet)
- Real-time prediction pipeline
- Backtesting with trading strategy

## How to Run

```bash
# Navigate to project directory
cd "Featured Projects/Ethereum_LSTM_Forecasting"

# Ensure data is in data/ subdirectory
ls data/Ethereum_4_7_2018-6_6_2018_historical_data_coinmarketcap.csv

# Run notebook
jupyter notebook Ethereum_prediction_using_LSTM_model.ipynb
```

## Dependencies

See `requirements.txt` in repository root.

**Note:** Requires TensorFlow/Keras for LSTM implementation.

## Disclaimer

This project is for educational purposes only. Cryptocurrency trading carries significant risk. Do not use this model for actual trading decisions without thorough backtesting and risk management.