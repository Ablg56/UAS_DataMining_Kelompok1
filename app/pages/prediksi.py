import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# =====================================================
# LOAD MODEL
# =====================================================

# Perbaikan path: mundur 1 kali saja untuk keluar dari folder 'pages'
import joblib

model = joblib.load(
    "../model/logistic_regression_model.pkl"
)
# =====================================================

st.title("🔮 Wine Quality Prediction")

st.write("""
Masukkan karakteristik wine untuk memprediksi kualitas wine.
""")

# =====================================================
# INPUT USER
# =====================================================

col1, col2 = st.columns(2)

with col1:

    fixed_acidity = st.slider(
        "Fixed Acidity",
        4.0, 16.0, 7.0
    )

    volatile_acidity = st.slider(
        "Volatile Acidity",
        0.1, 2.0, 0.5
    )

    citric_acid = st.slider(
        "Citric Acid",
        0.0, 1.0, 0.3
    )

    residual_sugar = st.slider(
        "Residual Sugar",
        0.5, 16.0, 2.5
    )

    chlorides = st.slider(
        "Chlorides",
        0.01, 0.7, 0.08
    )

    free_sulfur_dioxide = st.slider(
        "Free Sulfur Dioxide",
        1, 80, 15
    )

with col2:

    total_sulfur_dioxide = st.slider(
        "Total Sulfur Dioxide",
        5, 300, 50
    )

    density = st.slider(
        "Density",
        0.9900, 1.0050, 0.9960
    )

    ph = st.slider(
        "pH",
        2.5, 4.5, 3.3
    )

    sulphates = st.slider(
        "Sulphates",
        0.3, 2.0, 0.6
    )

    alcohol = st.slider(
        "Alcohol",
        8.0, 15.0, 10.0
    )

# =====================================================
# BUTTON PREDIKSI
# =====================================================

predict_btn = st.button(
    "🔮 Predict Quality",
    use_container_width=True
)

# =====================================================
# PREDIKSI
# =====================================================

if predict_btn:

    input_data = pd.DataFrame([{

        "fixed acidity": fixed_acidity,
        "volatile acidity": volatile_acidity,
        "citric acid": citric_acid,
        "residual sugar": residual_sugar,
        "chlorides": chlorides,
        "free sulfur dioxide": free_sulfur_dioxide,
        "total sulfur dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": ph,
        "sulphates": sulphates,
        "alcohol": alcohol

    }])

    # =================================================
    # PREDICT
    # =================================================

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(
        input_data
    )[0]

    # =================================================
    # HASIL
    # =================================================

    st.markdown("---")

    st.subheader("📊 Prediction Result")

    if prediction == 1:

        st.success("🍷 Good Quality Wine")

    else:

        st.error("⚠️ Bad Quality Wine")

    # =================================================
    # PROBABILITAS
    # =================================================

    prob_df = pd.DataFrame({

        "Class": ["Bad", "Good"],
        "Probability": probability

    })

    st.write("### Probabilitas")

    fig, ax = plt.subplots()

    ax.bar(
        prob_df["Class"],
        prob_df["Probability"]
    )

    ax.set_ylim(0, 1)

    for i, v in enumerate(prob_df["Probability"]):

        ax.text(
            i,
            v + 0.02,
            f"{v:.2f}",
            ha='center'
        )

    st.pyplot(fig)

    # =================================================
    # INPUT DATA
    # =================================================

    st.write("### Input Data")

    st.dataframe(input_data)