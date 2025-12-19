import streamlit as st
import joblib
import pandas as pd
import numpy as np

# 1. Load the Trained Model
# (Make sure 'zillow_pricing_engine.pkl' is in the same folder)
@st.cache_resource
def load_model():
    return joblib.load('D:\Srijan\Jupyter-Analysis\Finance\04_Real_Estate_Pricing\notebooks\zillow_pricing_engine.pkl')

try:
    model = load_model()
except:
    st.error("⚠️ Model file not found. Please run the notebook first to generate 'zillow_pricing_engine.pkl'.")
    st.stop()

# 2. App Title & Context
st.set_page_config(page_title="Zillow AI pricer", layout="centered")
st.title("🏠 AI Real Estate Arbitrage Engine")
st.markdown("""
This system uses a **Stacked Ensemble (LightGBM + XGBoost)** to detect pricing errors in the real estate market.
**Goal:** Identify if a property is *Overvalued* or *Undervalued* by the market (Zestimate).
""")

st.sidebar.header("Property Details")

# 3. User Inputs (The "Dashboard" Feel)
def user_input_features():
    # We only expose the most important features we engineered
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        bathrooms = st.number_input("Bathrooms", min_value=1.0, max_value=10.0, value=2.0)
        bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
        sqft = st.number_input("Square Feet", min_value=500, max_value=10000, value=1500)
    
    with col2:
        pool = st.selectbox("Has Pool?", [0, 1])
        year_built = st.number_input("Year Built", min_value=1900, max_value=2016, value=1980)
        tax_value = st.number_input("Tax Assessed Value ($)", min_value=10000, value=300000)

    # Neighborhood Context (Simulated for Demo)
    # In a real app, this would look up the Zip Code average from a database
    avg_zip_sqft = 1800 
    
    # Feature Engineering on the fly (Same logic as Notebook)
    data = {
        'bathroomcnt': bathrooms,
        'bedroomcnt': bedrooms,
        'calculatedfinishedsquarefeet': sqft,
        'poolcnt': pool,
        'yearbuilt': year_built,
        'taxvaluedollarcnt': tax_value,
        'structuretaxvaluedollarcnt': tax_value * 0.6, # Est. structure is 60% of total
        'landtaxvaluedollarcnt': tax_value * 0.4,      # Est. land is 40% of total
        'lotsizesquarefeet': sqft * 3,                 # Est. lot is 3x house size
        'taxamount': tax_value * 0.012,                # Est. tax rate 1.2%
        'regionidzip': 96000                           # Dummy Zip
    }
    
    df = pd.DataFrame([data])
    
    # --- Re-Create Engineering ---
    df['structure_dollar_per_sqft'] = df['structuretaxvaluedollarcnt'] / df['calculatedfinishedsquarefeet']
    df['land_dollar_per_sqft'] = df['landtaxvaluedollarcnt'] / df['lotsizesquarefeet']
    df['bed_bath_ratio'] = df['bedroomcnt'] / (df['bathroomcnt'] + 0.001)
    df['age'] = 2016 - df['yearbuilt']
    df['tax_rate'] = df['taxamount'] / df['taxvaluedollarcnt']
    df['sqft_vs_zip_avg'] = df['calculatedfinishedsquarefeet'] / avg_zip_sqft
    
    return df

input_df = user_input_features()

# 4. Display Input Data
st.subheader("1. Analyzed Property Profile")
st.dataframe(input_df)

# 5. Prediction Logic
if st.button("🚀 Run Arbitrage Analysis"):
    # Align columns with training data (fill missing with 0 for demo safety)
    # Note: In production, we would load the exact column list from a config file
    model_cols = model.feature_names_in_ if hasattr(model, 'feature_names_in_') else input_df.columns
    
    # Ensure all columns exist (fill 0 for ones we didn't ask for in UI)
    for c in model_cols:
        if c not in input_df.columns:
            input_df[c] = 0
            
    # Reorder to match model
    input_df = input_df[model_cols]
    
    prediction = model.predict(input_df)[0]
    
    # 6. The Result Display
    st.subheader("2. AI Valuation Verdict")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Predicted Log Error", f"{prediction:.4f}")
    
    actual_price_est = input_df['taxvaluedollarcnt'][0]
    corrected_price = actual_price_est * (1 + prediction)
    
    col2.metric("Market Price (Zestimate)", f"${actual_price_est:,.0f}")
    col3.metric("AI 'Fair Value'", f"${corrected_price:,.0f}", delta=f"{prediction*100:.2f}%")
    
    if prediction > 0.02:
        st.success("✅ **Opportunity:** This property is UNDERVALUED by the market. Buy signal.")
    elif prediction < -0.02:
        st.error("🛑 **Risk:** This property is OVERVALUED. Do not buy.")
    else:
        st.info("⚖️ **Fairly Priced:** The market price is accurate.")