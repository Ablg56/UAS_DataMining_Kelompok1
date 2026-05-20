import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../../dataset/WineQT.csv")

st.title("📊 Dataset Overview")

st.subheader("Informasi Dataset")

st.write(df.head())

st.write("Jumlah Data:", df.shape[0])
st.write("Jumlah Kolom:", df.shape[1])

st.subheader("Statistik Dataset")

st.dataframe(df.describe())

st.subheader("Missing Value")

st.write(df.isnull().sum())

fig, ax = plt.subplots()

sns.countplot(x='quality', data=df, ax=ax)

st.pyplot(fig)