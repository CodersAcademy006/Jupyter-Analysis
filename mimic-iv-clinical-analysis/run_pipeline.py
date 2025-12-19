import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import shap

# Import your modules
from src.features.aggregation import aggregate_features # Ensure this exists or use inline aggregation
from src.models.baseline import train_logistic_regression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.calibration import calibration_curve

# Columns known to cause target leakage in MIMIC-IV
LEAKAGE_COLS = [
    'dod', 'deathtime', 'discharge_location', 'hospital_expire_flag', 'los'
]

def plot_missingness_heatmap(df):
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False)
    plt.title('Missingness Heatmap')
    plt.show()

if __name__ == "__main__":
    # ---------------------------------------------------------
    # 1. DATA LOADING
    # ---------------------------------------------------------
    print("Loading MIMIC-IV Demo Data...")
    ICU_PATH = "mimic-iv-clinical-database-demo-2.2/icu/"
    HOSP_PATH = "mimic-iv-clinical-database-demo-2.2/hosp/"

    icustays = pd.read_csv(ICU_PATH + "icustays.csv.gz", compression="gzip")
    admissions = pd.read_csv(HOSP_PATH + "admissions.csv.gz", compression="gzip")
    # Limiting rows for demo speed, remove nrows for full run
    chartevents = pd.read_csv(ICU_PATH + "chartevents.csv.gz", compression="gzip", nrows=100000)

    # ---------------------------------------------------------
    # 2. FEATURE ENGINEERING (Strict 24h Window)
    # ---------------------------------------------------------
    print("Processing Features (24h Window)...")
    icu_adm = icustays.merge(admissions, on=["subject_id", "hadm_id"])
    chartevents["charttime"] = pd.to_datetime(chartevents["charttime"])
    icu_adm["intime"] = pd.to_datetime(icu_adm["intime"])
    
    merged = chartevents.merge(icu_adm, on=["subject_id", "hadm_id"])
    merged["hours_in"] = (merged["charttime"] - merged["intime"]).dt.total_seconds() / 3600
    
    # FILTER: strict 24h cutoff
    merged_24h = merged[merged["hours_in"] <= 24]
    
    # Debug: Check target distribution in raw 24h data
    if "hospital_expire_flag" in merged_24h.columns:
        print("hospital_expire_flag value counts (Raw 24h data):")
        print(merged_24h["hospital_expire_flag"].value_counts())

    # AGGREGATION
    # We aggregate 'hospital_expire_flag' with 'max' to preserve the target per stay
    agg_dict = {
        'valuenum': ['mean', 'max', 'min', 'std'],
        'hospital_expire_flag': 'max'
    }
    df_model = merged_24h.groupby('stay_id_x').agg(agg_dict)
    df_model.columns = ['_'.join(col).strip() for col in df_model.columns.values]

    # ---------------------------------------------------------
    # 3. PREPARATION & SPLITTING
    # ---------------------------------------------------------
    y = df_model['hospital_expire_flag_max']
    X = df_model.drop(columns=['hospital_expire_flag_max']).fillna(0) # Basic fill for NaNs from aggregation

    print('Final Target value counts (Per Stay):')
    print(y.value_counts())

    # STRATIFIED SPLIT (Crucial for small datasets)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    # ---------------------------------------------------------
    # 4. INSTITUTIONAL GRADE PREPROCESSING (No Leakage)
    # ---------------------------------------------------------
    print("Running Institutional Preprocessing Pipeline...")
    num_features = X.columns.tolist()
    
    # We fit the imputer ONLY on X_train to avoid look-ahead bias
    preprocessor = ColumnTransformer([
        ('num', SimpleImputer(strategy='median'), num_features)
    ])
    
    preprocessor.fit(X_train)
    X_train_clean = preprocessor.transform(X_train)
    X_test_clean = preprocessor.transform(X_test)
    
    # Note: ColumnTransformer returns numpy array, losing column names. 
    # For SHAP, we might want them back, but for the model it's fine.

    # ---------------------------------------------------------
    # 5. MODELING
    # ---------------------------------------------------------
    print("Training Model...")
    model, auroc, auprc = train_logistic_regression(X_train_clean, y_train)
    
    print("-" * 30)
    print(f'AUROC: {auroc:.4f}')
    print(f'AUPRC: {auprc:.4f}')
    print("-" * 30)

    # Feature Importances
    print('Feature Importances:')
    for name, coef in zip(num_features, model.coef_[0]):
        print(f'{name}: {coef:.4f}')

    # ---------------------------------------------------------
    # 6. ADVANCED VISUALIZATIONS
    # ---------------------------------------------------------
    print("Generating Visualizations...")

    # A. Calibration Curve
    y_prob = model.predict_proba(X_test_clean)[:, 1]
    fraction_of_positives, mean_predicted_value = calibration_curve(y_test, y_prob, n_bins=5) # Reduced bins for small data

    plt.figure(figsize=(8, 8))
    plt.plot(mean_predicted_value, fraction_of_positives, marker='o', label='Logistic Regression')
    plt.plot([0, 1], [0, 1], linestyle='--', color='gray', label='Perfectly Calibrated')
    plt.xlabel('Mean Predicted Probability')
    plt.ylabel('Fraction of Positives (Observed Risk)')
    plt.title('Calibration Curve (Reliability Diagram)')
    plt.legend()
    plt.grid(True)
    plt.savefig('calibration_curve.png') # Saving is safer than showing in some environments
    print("Saved: calibration_curve.png")
    # plt.show() 

    # B. SHAP Summary Plot
    # LinearExplainer is fast and exact for Logistic Regression
    explainer = shap.LinearExplainer(model, X_train_clean, feature_perturbation="interventional")
    shap_values = explainer.shap_values(X_test_clean)
    
    plt.figure(figsize=(10, 6))
    # converting X_test_clean back to DF for nice feature names in plot
    X_test_clean_df = pd.DataFrame(X_test_clean, columns=num_features)
    shap.summary_plot(shap_values, X_test_clean_df, plot_type="dot", show=False)
    plt.savefig('shap_summary.png', bbox_inches='tight')
    print("Saved: shap_summary.png")
    # plt.show()
    
    print("Pipeline Complete.")