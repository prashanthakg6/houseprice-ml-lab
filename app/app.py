import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load("../model.pkl")

with st.form("predict"):
    rent = st.number_input("Monthly Rent", value=15000)
    area = st.number_input("Square Feet", value=1000)
    
    locality_list = ["BTM Layout", "Attibele", "K R Puram", "Marathahalli", "Indiranagar", "Electronic City", "Yalahanka", "Malleshwaram", "Jayanagar", "Missing"]
    locality = st.selectbox("Locality", locality_list, index=0)
    bedrooms = st.number_input("Bedrooms", value=2, min_value=0, max_value=10, step=1)
    parking = st.text_input("Parking (Open/Covered/Missing)", "Open")
    bathrooms = st.number_input("Bathrooms", value=2, min_value=0, max_value=10, step=1)
    #facing = st.text_input("Facing (North/South/East/West/Missing)", "North")
    facinn=g_List = ["North", "South", "East", "West", "Missing"]
    facing = st.selectbox("Facing Direction", facinn, index=0)
    submitted = st.form_submit_button("Predict")

if submitted:
    X = pd.DataFrame([{
        "rent": rent,
        "area": area,
        "locality": locality if locality else "Missing",
        "BHK": bedrooms,
        "parking": parking if parking else "Missing",
        "bathrooms": bathrooms,
        "facing": facing if facing else "Missing"
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")
