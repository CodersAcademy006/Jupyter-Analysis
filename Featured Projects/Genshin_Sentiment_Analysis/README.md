# Genshin Impact Sentiment Analysis

**Author:** Data Science Portfolio  
**Date:** 2024  
**Tags:** NLP, Sentiment Analysis, Text Classification, SMOTE

## Executive Summary

This project analyzes sentiment in social media posts about the popular game Genshin Impact. Using natural language processing techniques and machine learning classification models, we classify user sentiments while addressing class imbalance through SMOTE oversampling, achieving approximately 85% accuracy.

## Problem Statement

Understanding community sentiment is crucial for:
- Game developers monitoring player feedback
- Community managers identifying concerns
- Marketing teams gauging campaign effectiveness
- Players understanding community opinions

This project aims to automatically classify sentiment (positive, negative, neutral) from social media text data.

## Dataset

- **Source:** Social media posts about Genshin Impact
- **Date:** March 30, 2024
- **Size:** Multiple entries with relevance filtering
- **Features:**
  - Text content (posts, comments)
  - Engagement metrics
  - Timestamps
- **Target:** Sentiment labels

## Methodology

1. **Data Preprocessing**
   - Text cleaning (special characters, punctuation)
   - HTML tag removal
   - Emoji removal
   - Number removal
   - Lowercasing
   - Stop word removal

2. **Text Processing**
   - Tokenization using RegexpTokenizer
   - Feature extraction with TF-IDF and CountVectorizer
   - N-gram analysis
   - Word cloud generation

3. **Handling Class Imbalance**
   - SMOTE (Synthetic Minority Over-sampling Technique)
   - Balancing sentiment classes
   - Validation of resampling quality

4. **Model Development**
   - Multinomial Naive Bayes (baseline)
   - Additional classification models
   - Feature importance analysis

5. **Evaluation**
   - Accuracy score
   - Classification report (precision, recall, F1)
   - Confusion matrix
   - Cross-validation

## Key Findings

1. **Class imbalance is significant** in sentiment data, requiring SMOTE
2. **TF-IDF features outperform** simple count vectors
3. **Common positive words** relate to game mechanics and enjoyment
4. **Negative sentiment** often mentions specific game issues
5. **Neutral posts** are hardest to classify accurately
6. **Text preprocessing is critical** for model performance

## Technical Stack

- **NLP Libraries:** nltk, wordcloud
- **Text Processing:** RegexpTokenizer, TfidfVectorizer, CountVectorizer
- **Machine Learning:** scikit-learn
- **Imbalanced Data:** imblearn (SMOTE)
- **Visualization:** matplotlib, seaborn
- **Data Processing:** pandas, numpy

## Text Processing Pipeline

```python
1. Remove HTML tags
2. Remove punctuation
3. Remove numbers
4. Remove emojis
5. Lowercase conversion
6. Stop word removal
7. Tokenization
8. Vectorization (TF-IDF)
```

## Results Summary

### Model Performance

| Metric | Score |
|--------|-------|
| Overall Accuracy | ~85% |
| Positive Sentiment (Precision) | ~87% |
| Negative Sentiment (Precision) | ~83% |
| Neutral Sentiment (Precision) | ~80% |

*Note: Exact values depend on train-test split and random state*

### Class Distribution

- Original data showed imbalance
- SMOTE successfully balanced classes
- Improved minority class detection

### Visualizations

The project includes:
- Word clouds for each sentiment
- Feature importance plots
- Confusion matrices
- Class distribution charts

## Challenges & Solutions

### Challenge 1: Class Imbalance
**Solution:** Implemented SMOTE to generate synthetic samples

### Challenge 2: Noisy Social Media Text
**Solution:** Comprehensive text cleaning pipeline

### Challenge 3: Emoji and Special Characters
**Solution:** Regex-based cleaning with Unicode handling

### Challenge 4: Context Understanding
**Solution:** N-gram features capture multi-word expressions

## Conclusions

1. Automated sentiment analysis is feasible for gaming communities
2. SMOTE effectively addresses class imbalance in text classification
3. Preprocessing quality directly impacts model accuracy
4. The model can be deployed for real-time sentiment monitoring
5. TF-IDF with Naive Bayes provides strong baseline performance

## Applications

- **Community Management:** Monitor sentiment trends
- **Product Development:** Identify pain points and popular features
- **Marketing:** Measure campaign effectiveness
- **Customer Support:** Prioritize negative sentiment responses

## Future Work

- Implement deep learning models (LSTM, BERT)
- Aspect-based sentiment analysis (specific game features)
- Multi-lingual sentiment analysis
- Real-time sentiment tracking dashboard
- Emotion classification (beyond positive/negative/neutral)
- Sarcasm detection
- Trend analysis over time
- Integration with social media APIs

## How to Run

```bash
# Navigate to project directory
cd "Featured Projects/Genshin_Sentiment_Analysis"

# Ensure data is in data/ subdirectory
ls data/GenshinImpact_30Maret2024_MostRelevant_non995.csv

# Run notebook
jupyter notebook sentiment-analysis-genshin-impact.ipynb
```

## Dependencies

See `requirements.txt` in repository root.

**Additional NLTK Downloads Required:**
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

## Ethical Considerations

- Data privacy: No personal information is stored or analyzed
- Bias awareness: Model may reflect biases in training data
- Responsible use: Should complement, not replace, human judgment
- Transparency: Classifications should be explainable to users