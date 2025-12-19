# Core Machine Learning Projects

## Overview

This directory contains foundational machine learning projects demonstrating core data science techniques across various problem types. These projects showcase essential ML skills including exploratory data analysis, regression, classification, natural language processing, and recommendation systems.

---

## Project Categories

### 📊 [Exploratory Data Analysis (EDA)](EDA/)
**Focus:** Data Understanding | Visualization | Statistical Analysis

Projects focused on understanding data through visualization, statistical analysis, and pattern discovery.

**Projects:**
- **Car Performance Analysis:** Fuel efficiency, correlation analysis, comparative statistics
- **Walmart Sales Analysis:** Retail trends, time series patterns, revenue analysis
- **DebtPenny Analysis:** Financial debt trends, temporal analytics

**Skills Demonstrated:**
- Distribution analysis
- Correlation matrices
- Time series visualization
- Statistical summaries
- Data quality assessment
- Outlier detection
- Feature relationships

**Technologies:** pandas, NumPy, matplotlib, seaborn

---

### 📈 [Regression & Classification](Regression/)
**Focus:** Predictive Modeling | Supervised Learning

Machine learning projects focused on predicting continuous and categorical variables.

**Projects:**
- **Finance (Credit Risk Analysis):** Loan default prediction, risk factors
- **Loan Approval System:** Automated loan decisions with Random Forest
- **Diabetes Prediction:** Medical diagnosis with classification models

**Skills Demonstrated:**
- Feature selection and engineering
- Model training and validation
- Performance metrics (RMSE, R², MAE, Accuracy)
- Cross-validation
- Hyperparameter tuning
- Classification and regression techniques

**Techniques:**
- Logistic Regression
- Decision Trees
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Machines

**Technologies:** scikit-learn, pandas, NumPy

---

### 💬 [Natural Language Processing (NLP)](NLP_Projects/)
**Focus:** Text Analytics | Sentiment Analysis | Classification

NLP and text analytics projects demonstrating various text processing and analysis techniques.

**Projects:**
1. **Resume Screening NLP:** Automated candidate matching and classification
2. **SMS Spam Detection:** Binary classification for spam identification
3. **Language Classification:** Multi-language detection system
4. **Text Summarization:** Extractive summarization techniques
5. **US Election Sentiment Analysis:** Political tweet analysis and visualization
6. **WhatsApp Sentiment Analysis:** Chat conversation sentiment extraction

**Skills Demonstrated:**
- Text preprocessing (tokenization, stemming, lemmatization)
- Stop word removal
- TF-IDF vectorization
- Word embeddings
- Sentiment analysis
- Classification models
- Regular expressions
- Language detection

**Techniques:**
- Bag of Words (BoW)
- TF-IDF
- Naive Bayes
- Text classification
- Sentiment scoring
- Character n-grams

**Technologies:** NLTK, scikit-learn, pandas, regex

---

### 🎯 [Recommender Systems](Recommender_Systems/)
**Focus:** Recommendation Algorithms | Collaborative Filtering

Projects implementing recommendation algorithms and user-item interaction modeling.

**Projects:**
- **Book Recommendation System:** Content-based and collaborative filtering

**Skills Demonstrated:**
- Recommendation algorithms
- Similarity calculations (cosine, Euclidean)
- User-item interactions
- Rating predictions
- Cold start problem handling
- Matrix factorization concepts

**Techniques:**
- Content-based filtering
- Collaborative filtering
- Similarity metrics
- Matrix operations

**Technologies:** pandas, NumPy, scikit-learn

---

### 📉 [General Analysis Projects](Analysis_Projects/)
**Focus:** Domain-Agnostic Analytics | Insight Extraction

Diverse analytical projects demonstrating data exploration and insight extraction.

**Projects:**
1. **COVID-19 Vaccines Analysis:** Global vaccination trends, geographic analysis
2. **World Billionaires Analysis:** Wealth distribution, demographic patterns
3. **Google Search Analysis:** Search trends, pattern discovery

**Skills Demonstrated:**
- Statistical analysis
- Data visualization
- Trend identification
- Comparative analysis
- Geographic visualization
- Time series analysis

**Technologies:** pandas, matplotlib, seaborn, plotly

---

## Core ML Competencies

### Data Preprocessing
- Missing value imputation
- Outlier detection and handling
- Feature scaling and normalization
- Categorical encoding
- Data type conversion
- Data validation

### Feature Engineering
- Feature creation and transformation
- Dimensionality reduction
- Feature selection techniques
- Interaction features
- Temporal features
- Text feature extraction

### Model Development
- Algorithm selection
- Model training and evaluation
- Hyperparameter tuning
- Cross-validation strategies
- Ensemble methods
- Model interpretation

### Evaluation & Validation
- Performance metrics selection
- Train/test/validation splits
- K-fold cross-validation
- Bias-variance tradeoff
- Confusion matrices
- ROC/AUC analysis

### Visualization
- Statistical plots (histograms, box plots, scatter plots)
- Correlation heatmaps
- Feature importance plots
- Model performance visualization
- Interactive dashboards
- Business-friendly charts

---

## Technical Stack

| Category | Technologies |
|----------|-------------|
| **Data Processing** | pandas, NumPy |
| **Machine Learning** | scikit-learn (classification, regression, clustering) |
| **NLP** | NLTK, TextBlob, regex |
| **Visualization** | matplotlib, seaborn, plotly |
| **Statistical Analysis** | scipy, statsmodels |
| **Development** | Jupyter Notebook, Python 3.10+ |

---

## Getting Started

### Prerequisites
- Python 3.10+
- Jupyter Notebook
- pip package manager

### Installation

1. Navigate to Core ML Projects:
   ```bash
   cd Core_ML_Projects
   ```

2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn nltk
   ```

3. For NLP projects, download NLTK data:
   ```bash
   python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
   ```

4. Choose a category and project:
   ```bash
   cd EDA  # or Regression, NLP_Projects, etc.
   jupyter notebook
   ```

---

## Learning Path

### Beginner Level
1. **Start with EDA:** Understand data through visualization
2. **Simple Regression:** Linear models and metrics
3. **Basic Classification:** Logistic regression and decision trees

### Intermediate Level
4. **Advanced Regression:** Ensemble methods (Random Forest, XGBoost)
5. **NLP Basics:** Text preprocessing and sentiment analysis
6. **Classification Tuning:** Hyperparameter optimization

### Advanced Level
7. **Complex NLP:** Multi-class classification, advanced preprocessing
8. **Recommender Systems:** User-item interactions and filtering
9. **Feature Engineering:** Advanced techniques for better models

---

## Project Complexity Matrix

| Project Category | Difficulty | Time to Complete | Prerequisites |
|-----------------|------------|------------------|---------------|
| EDA | ⭐ Beginner | 2-4 hours | Python basics, pandas |
| Regression | ⭐⭐ Intermediate | 4-6 hours | ML fundamentals, scikit-learn |
| NLP Projects | ⭐⭐ Intermediate | 4-8 hours | Text processing, NLTK |
| Recommender Systems | ⭐⭐⭐ Advanced | 6-8 hours | Linear algebra, similarity metrics |
| Analysis Projects | ⭐ Beginner | 2-4 hours | pandas, visualization |

---

## Key Performance Indicators

### Model Performance
- **Classification:** Accuracy, Precision, Recall, F1-Score, ROC-AUC
- **Regression:** R², RMSE, MAE, MAPE
- **NLP:** Accuracy, Precision, Recall, Sentiment Scores
- **Recommender:** RMSE, Precision@K, Recall@K

### Data Quality
- Missing value percentage
- Outlier detection rate
- Feature correlation strength
- Data balance (for classification)

---

## Best Practices Demonstrated

### Code Quality
- ✅ Modular, reusable functions
- ✅ Clear variable naming
- ✅ Comprehensive comments
- ✅ Structured notebooks
- ✅ Reproducible results

### Analysis Workflow
- ✅ Data loading and inspection
- ✅ Exploratory analysis
- ✅ Preprocessing and feature engineering
- ✅ Model training and evaluation
- ✅ Visualization and insights
- ✅ Conclusions and recommendations

### Professional Standards
- ✅ Documentation in README files
- ✅ Business context for projects
- ✅ Clear methodology explanations
- ✅ Interpretation of results
- ✅ Actionable insights

---

## Common Use Cases

### EDA Projects
- Understanding new datasets
- Identifying data quality issues
- Discovering patterns and relationships
- Generating hypotheses for modeling

### Regression Projects
- Predicting continuous outcomes (prices, sales, quantities)
- Risk assessment (loan defaults, insurance claims)
- Forecasting (demand, revenue)

### Classification Projects
- Binary decisions (spam/not spam, fraud/legitimate)
- Multi-class categorization (product types, customer segments)
- Medical diagnosis
- Sentiment classification

### NLP Projects
- Text classification and categorization
- Sentiment analysis for reviews/feedback
- Information extraction
- Language detection
- Resume parsing and matching

### Recommender Systems
- Product recommendations
- Content suggestions
- Personalization engines
- Collaborative filtering applications

---

## Intended Audience

- **Data Science Students:** Learn core ML techniques through practical projects
- **Career Transitioners:** Build foundational portfolio for entry-level roles
- **Recruiters:** Evaluate fundamental data science skills
- **Educators:** Use as teaching examples or assignments
- **Self-Learners:** Study real-world ML implementations

---

## Integration with Domain Projects

These core ML skills are applied in domain-specific projects:
- **EDA** → All domain projects start with exploratory analysis
- **Regression/Classification** → Finance (credit risk), Healthcare (ICU mortality)
- **NLP** → Finance (sentiment), Retail (review analysis)
- **Feature Engineering** → Energy (solar efficiency), Finance (quantitative features)

See [Domain_Projects](../Domain_Projects/) for industry-specific applications.

---

## Contributing

To add a new core ML project:
1. Choose the appropriate category (EDA, Regression, NLP, etc.)
2. Follow the existing project structure
3. Include a clear README with methodology
4. Add sample data or data source instructions
5. Document key insights and learnings

---

## Contact

For questions about core ML projects, learning guidance, or collaboration opportunities, please refer to the main repository contact information.

---

**Building strong foundations for advanced data science careers**
