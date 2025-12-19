# 🏛️ Applied Data Science Portfolio


[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)


## Quick Navigation

**Hiring for Specific Domains?** Jump directly to:
- [🏥 Healthcare Projects](Domain_Projects/Healthcare/) | [💰 Finance Projects](Domain_Projects/Finance/) | [🛒 Retail Projects](Domain_Projects/Retail_Ecommerce/)
- [⚡ Energy Projects](Domain_Projects/Energy_Sustainability/) | [🎓 Education Projects](Domain_Projects/Education/) | [💻 Technology Projects](Domain_Projects/Technology_Consumer/)

**Looking for ML Techniques?** Browse by capability:
- [📊 EDA](Core_ML_Projects/EDA/) | [📈 Regression](Core_ML_Projects/Regression/) | [💬 NLP](Core_ML_Projects/NLP_Projects/) | [🎯 Recommender Systems](Core_ML_Projects/Recommender_Systems/)

**Want Top Showcase Work?** See [Featured Projects](Featured%20Projects/)

---

## Executive Summary

This portfolio demonstrates advanced applied data science and machine learning solutions across finance, healthcare, retail, and technology domains. Projects are designed to meet institutional standards for reproducibility, auditability, and business impact—reflecting the rigor expected at leading firms such as JP Morgan.

**Portfolio Highlights:**
- 🏆 **Flagship Projects:** Institutional-grade modeling, forecasting, and NLP
- 🎯 **Domain Expertise:** Healthcare, Finance, Retail, Energy, Education, Technology
- 📊 **Comprehensive EDA:** Robust data exploration and visualization
- 🤖 **Machine & Deep Learning:** Regression, classification, time series, NLP, GNN
- 🏥 **Healthcare Analytics:** ICU mortality, sepsis early warning, risk modeling
- 💼 **Business Solutions:** Credit risk, e-commerce, quantitative trading, recommender systems
- 📚 **Professional Documentation:** Each project includes detailed methodology, KPIs, and business insights


## Repository Structure

```
Applied-Data-Science-Portfolio/
├── Featured Projects/              # 🏆 Top 3 showcase projects
│   ├── Diamond_Price_Prediction/
│   ├── Ethereum_LSTM_Forecasting/
│   └── Genshin_Sentiment_Analysis/
├── Domain_Projects/               # 🎯 Industry-specific projects
│   ├── Healthcare/                # Clinical analytics, ICU risk modeling
│   ├── Finance/                   # Quant trading, credit risk, AML
│   ├── Retail_Ecommerce/          # Customer analytics, logistics
│   ├── Education/                 # Study abroad, market analysis
│   ├── Energy_Sustainability/     # Solar efficiency, renewables
│   └── Technology_Consumer/       # Tech products, sports economics
├── Core ML Projects/              # 🤖 Foundational ML techniques
│   ├── EDA/                       # Exploratory Data Analysis
│   ├── Regression/                # Predictive modeling
│   ├── NLP_Projects/              # Natural Language Processing
│   ├── Recommender_Systems/       # Recommendation algorithms
│   └── Analysis_Projects/         # General analytical work
├── Archived/                      # 📦 Experimental & legacy work
└── Kaagle Fun Projects/           # 🎮 Learning & tutorials
```


## Flagship Projects

### 1. [Diamond Price Prediction](Featured%20Projects/Diamond_Price_Prediction/)
**Regression | ML | Feature Engineering**
- Predict diamond prices with ensemble ML (Random Forest, XGBoost)
- Advanced feature engineering, model selection, and business impact analysis
- R² ≈ 0.98, RMSE ≈ $550

### 2. [Ethereum Price Forecasting](Featured%20Projects/Ethereum_LSTM_Forecasting/)
**Deep Learning | Time Series | LSTM**
- Cryptocurrency price prediction using LSTM neural networks
- Time series preprocessing, architecture design, and forecasting evaluation
- TensorFlow/Keras, financial KPIs

### 3. [Genshin Impact Sentiment Analysis](Featured%20Projects/Genshin_Sentiment_Analysis/)
**NLP | Sentiment Analysis | SMOTE**
- Social media sentiment classification (85% accuracy)
- Imbalanced data handling (SMOTE), full NLP pipeline


## Core Technical Competencies

**Machine Learning & AI:**
- Supervised/unsupervised learning, ensemble methods, hyperparameter tuning
- Model validation, cross-validation, business metric optimization

**Deep Learning:**
- LSTM, GRU, neural network architecture, regularization, explainability (SHAP)

**Natural Language Processing:**
- Text preprocessing, TF-IDF, vectorization, sentiment analysis, SMOTE

**Data Engineering & Visualization:**
- ETL pipelines, feature engineering, matplotlib, seaborn, plotly, interactive dashboards

**Professional Practices:**
- Modular code, reproducibility, audit trails, compliance (anti-leakage protocols)
- Institutional reporting, business insights, actionable recommendations


## Project Organization

This portfolio is organized into three main sections:

### 🏆 Featured Projects
Top 3 showcase projects demonstrating advanced capabilities:
- **Diamond Price Prediction:** Ensemble ML with R² ≈ 0.98
- **Ethereum LSTM Forecasting:** Deep learning for cryptocurrency prediction
- **Genshin Sentiment Analysis:** NLP with SMOTE for imbalanced data (85% accuracy)

### 🎯 [Domain Projects](Domain_Projects/)
Industry-specific projects organized by business domain:

#### [Healthcare Analytics](Domain_Projects/Healthcare/)
- **MIMIC-IV Clinical Analysis:** ICU mortality prediction, sepsis early warning, causal inference

#### [Finance & Quantitative Analytics](Domain_Projects/Finance/)
- **Anti-Money Laundering:** Graph Neural Networks for Bitcoin fraud detection
- **High-Frequency Volatility:** Order book analysis with 1D-CNNs
- **Home Credit Default Risk:** Portfolio risk signals and red-flag analysis
- **Real Estate Pricing:** Arbitrage engine with ensemble stacking
- **Financial Sentiment:** FinBERT for alpha generation

#### [Retail & E-Commerce](Domain_Projects/Retail_Ecommerce/)
- **Olist E-Commerce:** Customer segmentation (RFM), logistics, NLP reviews

#### [Education Analytics](Domain_Projects/Education/)
- **Study Abroad Analysis:** Market trends, fee structure, program recommendations

#### [Energy & Sustainability](Domain_Projects/Energy_Sustainability/)
- **Solar Panel Efficiency:** PVGIS integration, physics-based modeling, anomaly detection

#### [Technology & Consumer](Domain_Projects/Technology_Consumer/)
- **Laptop Data Analysis:** Indian market, brand positioning, pricing strategy
- **Olympics Economics:** Performance vs GDP, investment ROI

### 🤖 [Core ML Projects](Core_ML_Projects/)
Foundational machine learning techniques:
- **EDA:** Car performance, Walmart sales, DebtPenny analysis
- **Regression:** Credit risk, loan approval, diabetes prediction
- **NLP:** Resume screening, spam detection, sentiment analysis, text summarization
- **Recommender Systems:** Book recommendation with collaborative filtering
- **General Analysis:** COVID-19 vaccines, billionaires, Google trends


## Getting Started

### Prerequisites
- Python 3.10 or higher
- pip package manager
- Jupyter Notebook

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/CodersAcademy006/Applied-Data-Science-Portfolio.git
   cd Applied-Data-Science-Portfolio
   ```
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download NLTK data (for NLP projects):
   ```bash
   python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
   ```

### Running Projects

#### For Domain-Specific Projects:
```bash
cd Domain_Projects/<domain_name>/<project_name>
jupyter notebook
```

#### For Core ML Projects:
```bash
cd Core_ML_Projects/<category>
jupyter notebook
```

#### For Featured Projects:
```bash
cd "Featured Projects"/<project_name>
jupyter notebook
```

### Navigation Guide

**For Industry-Specific Work:**
- Healthcare → `Domain_Projects/Healthcare/`
- Finance/Trading → `Domain_Projects/Finance/`
- Retail/E-commerce → `Domain_Projects/Retail_Ecommerce/`
- Energy/Sustainability → `Domain_Projects/Energy_Sustainability/`
- Education → `Domain_Projects/Education/`
- Consumer Tech → `Domain_Projects/Technology_Consumer/`

**For ML Technique Examples:**
- Data Exploration → `Core_ML_Projects/EDA/`
- Predictive Modeling → `Core_ML_Projects/Regression/`
- Text Analytics → `Core_ML_Projects/NLP_Projects/`
- Recommendations → `Core_ML_Projects/Recommender_Systems/`

**For Top Showcase Work:**
- Featured Projects → `Featured Projects/`


## Documentation & Auditability

Each project directory includes:
- **README.md:** Executive summary, methodology, KPIs, and business impact
- **Jupyter Notebook:** Complete analysis, code, and visualizations
- **data/**: Datasets (where applicable)

See [Featured Projects README](Featured%20Projects/README.md) for flagship project details.


## Intended Audience

- **Institutional Data Science Teams:** Evaluate technical depth, reproducibility, and business impact
- **Recruiters & Hiring Managers:** Assess advanced modeling, compliance, and reporting standards
- **Collaborators & Partners:** Explore scalable, production-ready solutions
- **Students & Learners:** Study real-world, enterprise-grade workflows


## Portfolio Statistics

- **Projects:** 20+
- **Lines of Code:** 12,000+
- **Datasets Analyzed:** 25+
- **ML/DL Models:** 20+
- **Professional Visualizations:** 120+


## Contributing

Contributions, issues, and feature requests are welcome. Please fork the repository, create a feature branch, and submit a pull request with a clear description of your enhancement or fix.


## Contact

**GitHub:** [@CodersAcademy006](https://github.com/CodersAcademy006)


## License

This repository is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

---


---

### ⭐ If you find this repository helpful, please consider giving it a star!

**Built with ❤️ using Python, Jupyter, and enterprise-grade data science**
