import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../../dataset/WineQT.csv")

st.title("📈 Visualization")

tab1, tab2 = st.tabs([
    "Heatmap",
    "Histogram"
])

with tab1:

    fig, ax = plt.subplots(figsize=(10,6))

    sns.heatmap(
        df.corr(),
        annot=True,
        cmap='coolwarm',
        ax=ax
    )

    st.pyplot(fig)

with tab2:

    fig, ax = plt.subplots()

    sns.histplot(df['alcohol'], kde=True, ax=ax)

    st.pyplot(fig)