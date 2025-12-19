
# Solar Panel Efficiency Analysis

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/) [![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/) [![pandas](https://img.shields.io/badge/pandas-1.5+-yellow.svg)](https://pandas.pydata.org/) [![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2+-f89f1b.svg)](https://scikit-learn.org/) [![matplotlib](https://img.shields.io/badge/matplotlib-3.5+-blueviolet.svg)](https://matplotlib.org/)

---

**[▶️ Open the Notebook](Solar_Panel_Efficiency_Analysis.ipynb)**

---


## Executive Summary
This project delivers an end-to-end, industry-grade analysis pipeline for evaluating solar panel efficiency using real-world meteorological and operational data. The workflow integrates data acquisition from the PVGIS API, robust preprocessing, advanced feature engineering, and predictive modeling to assess and forecast solar panel performance under varying environmental conditions.


## Key Features
- **Automated Data Acquisition:** Pulls hourly solar irradiance and weather data for Bangalore, India, via the PVGIS API.
- **Data Engineering:** Cleans, parses, and structures time-series data; handles missing values and outliers.
- **Physics-Based Modeling:** Calculates module temperature, panel efficiency (with temperature and degradation effects), and DC power output using industry-standard formulas.
- **Performance Degradation:** Models annual degradation and soiling losses, simulating real-world operational decline.
- **Predictive Analytics:** Implements linear regression and gradient boosting to forecast power output, with rigorous train/test splits and performance metrics (MAE, R²).
- **Anomaly Detection:** Uses Isolation Forest to flag operational anomalies in power output.
- **Feature Importance:** Quantifies drivers of efficiency and power output for actionable insights.


## Methodology
1. **Data Collection:**
   - PVGIS API for hourly GHI, temperature, wind speed (2020, Bangalore).
2. **Preprocessing:**
   - Cleans CSV, extracts valid rows, parses timestamps, and ensures correct data types.
3. **Physics-Based Calculations:**
   - **Module Temperature:**
     $$
     T_{module} = T_{ambient} + \frac{NOCT - 20}{800} \times GHI
     $$
   - **Panel Efficiency (with temperature):**
     $$
     \eta = \eta_{STC} \times \left[1 + \gamma (T_{module} - T_{STC})\right]
     $$
   - **DC Power Output:**
     $$
     P_{DC} = GHI \times Area \times \eta
     $$
   - **Degradation:**
     $$
     Degradation\ Factor = 1 - (Annual\ Rate) \times \frac{Days}{365}
     $$
   - **Soiling Loss:**
     $$
     Soiling\ Factor = 1 - Max\ Loss \times \frac{Days\ Since\ Clean}{Interval}
     $$
4. **Observed Power & Efficiency:**
   - Simulates observed DC power with noise, calculates observed efficiency and performance ratio.
5. **Analysis & Modeling:**
   - Filters for daytime, engineers time features, splits data chronologically.
   - Trains linear regression and gradient boosting models; evaluates with MAE and R².
   - Estimates annual degradation from performance ratio trend.
   - Detects anomalies and visualizes results.


## Results

**Model Performance:**

- **Gradient Boosting ($R^2 = 0.94$, MAE = 8.2 W)** outperformed Linear Regression (**$R^2 = 0.82$, MAE = 15.6 W**) in predicting observed DC power on the test set.
- **Feature Importance:** GHI and module temperature were the dominant drivers of power output, as quantified by model feature importances.

**Operational Insights:**

- Quantified the impact of temperature, soiling, and degradation on panel efficiency using physics-based models.
- Detected and visualized operational anomalies (e.g., outliers, underperformance) using Isolation Forest.

---

## Visual Analysis

<p align="center">
   <img src="assets/power_curve.png" alt="Power Curve" width="500"/><br>
   <em>Observed DC Power for a Sample Day</em>
</p>

<p align="center">
   <img src="assets/anomaly_detection.png" alt="Anomaly Detection" width="500"/><br>
   <em>Predicted vs. Observed Power with Anomalies Highlighted</em>
</p>

<p align="center">
   <img src="assets/efficiency_vs_temp.png" alt="Efficiency vs Temperature" width="500"/><br>
   <em>Efficiency vs. Module Temperature Scatter</em>
</p>


## Usage
1. Install dependencies (see first notebook cell).
2. Run all cells in order for a full analysis pipeline.
3. Outputs include processed datasets and visualizations for reporting.


## File Structure
- `Solar_Panel_Efficiency_Analysis.ipynb` — Main analysis notebook
- `solar_panel_efficiency_analysis_dataset.csv` — Final processed dataset (generated)
- `assets/` — Visualizations (add screenshots here for best presentation)


## Author
- Data analysis and notebook by Srijan Upadhyay


---
For questions or suggestions, please open an issue or contact the author.
