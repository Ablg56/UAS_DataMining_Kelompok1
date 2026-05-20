import streamlit as st

# =====================================================
# PAGE CONFIG (Wajib ada di file utama)
# =====================================================
st.set_page_config(
    page_title="Wine Quality Prediction",
    page_icon="🍷",
    layout="wide"
)

# Informasi kelompok di sidebar agar muncul di setiap halaman
with st.sidebar:
    st.success("Machine Learning Project")
    st.markdown("""
    ### 👨‍💻 Kelompok
    - **Abil Faroj Nur Yahya** (24051214072)
    - **Felix Kristanto** (24051214098)
    """)

# =====================================================
# HOME PAGE CONTENT
# =====================================================
st.title("🍷 Wine Quality Prediction System")

st.markdown("""
## 📌 Deskripsi Proyek

Project ini bertujuan untuk memprediksi kualitas wine menggunakan metode Machine Learning.

### Metode yang digunakan:
- **Classification** → Logistic Regression
- **Clustering** → K-Means

### Framework:
- CRISP-DM
""")

st.markdown("---")
st.subheader("🎯 Tujuan Project")
st.write("""
Membantu melakukan analisis kualitas wine berdasarkan karakteristik kimia wine menggunakan metode Data Mining.
""")

st.markdown("---")
st.info("💡 Gunakan menu navigasi otomatis di sidebar sebelah kiri untuk berpindah ke halaman analisis lainnya.")