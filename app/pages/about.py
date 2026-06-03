import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="About - Wine Quality",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# DATASET LOADING
# =====================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(
    current_dir,
    "..",
    "..",
    "dataset",
    "WineQT.csv"
)

try:
    df = pd.read_csv(csv_path)
    jumlah_data = df.shape[0]
    jumlah_fitur = df.shape[1] - 1

    if "quality" in df.columns:
        jumlah_kelas = df["quality"].nunique()
    else:
        jumlah_kelas = "-"
except Exception as e:
    # Fallback jika file dataset belum terbaca saat testing layout
    jumlah_data = 1143
    jumlah_fitur = 11
    jumlah_kelas = 6

# =====================================================
# STYLING (CSS KUSTOM AMAN)
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300&family=DM+Mono:wght@300;400&display=swap');

:root {
    --wine: #7a1e2e;
    --wine-dark: #55131f;
    --wine-light: #f6e9eb;
    --gold: #b8924a;
    --gold-light: #faf4e8;
    --teal: #1a7a6e;
    --teal-light: #e4f5f2;
    --text: #1a1a1a;
    --muted: #6b6b6b;
    --bg: #faf9f7;
    --border: rgba(0,0,0,0.08);
}

.stApp { 
    background: var(--bg); 
}

/* Mengatur font khusus elemen buatan kita, tanpa menabrak engine internal Streamlit */
.page-header, .eyebrow, .page-title, .divider, .section-label,
.method-cards, .method-card, .method-tag, .method-name, .method-body,
.info-table, .info-row, .info-key, .info-val, .dataset-stats, .ds-cell,
.ds-num, .ds-label, .ds-sub, .framework-block, .fw-step, .fw-num, .fw-name, .fw-sub,
.sidebar-title, .sidebar-sub, .team-title, .member, .member-name, .member-id, .source-link {
    font-family: 'DM Mono', monospace !important;
}

/* Sembunyikan menu bawaan & footer */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

/* Biarkan header transparan agar tombol panah tetap berfungsi secara fungsional */
header[data-testid="stHeader"] { 
    background: transparent !important; 
}
header[data-testid="stHeader"] button {
    color: var(--text) !important;
}

.st-emotion-cache-12bp31y {color: var(--teal) !important;} /* Override warna teks default Streamlit agar sesuai dengan tema */
.block-container {
    padding-top: 5rem !important; /* Diberi ruang pas agar tidak bertabrakan dengan panah */
    padding-bottom: 3rem !important;
    max-width: 1150px !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: var(--wine-dark) !important;
    border-right: none;
}

section[data-testid="stSidebar"] > div {
    padding: 2rem 1.5rem !important;
}

.sidebar-title, .sidebar-sub, .team-title, .member, .member-name, .member-id {
    color: white !important;
}

.sidebar-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.2rem;
    margin-bottom: 0;
}

.sidebar-sub {
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.6;
    margin-bottom: 2rem;
}

.team-title {
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.45;
    margin-bottom: 1rem;
}

.member {
    background: rgba(255,255,255,0.05);
    padding: 0.9rem;
    border-radius: 8px;
    margin-bottom: 0.7rem;
    border-left: 2px solid var(--gold);
}

.member-name { font-size: 0.9rem; }
.member-id { font-size: 0.7rem; opacity: 0.55; margin-top: 4px; }

/* Content Headings */
.page-header { margin-top: 1rem; margin-bottom: 3rem; }
.eyebrow {
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    color: var(--gold);
    margin-bottom: 1rem;
    text-transform: uppercase;
}

.page-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 5.5rem;
    line-height: 0.92;
    font-weight: 300;
    color: var(--text);
}

.page-title em {
    font-family: 'Cormorant Garamond', serif !important;
    color: var(--wine);
    font-style: italic;
}

.divider {
    width: 100%;
    height: 1px;
    background: var(--border);
    margin: 2rem 0;
}

.section-label {
    font-size: 0.65rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #999;
    margin-bottom: 1.25rem;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-label::before {
    content: '';
    display: inline-block;
    width: 16px;
    height: 1px;
    background: var(--gold);
    flex-shrink: 0;
}

/* Method Cards */
.method-cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 0.5rem;
}

.method-card {
    padding: 1.5rem;
    border-radius: 10px;
    border: 1px solid var(--border);
}

.method-card:nth-child(1) { background: var(--wine-light); }
.method-card:nth-child(2) { background: var(--teal-light); }

.method-tag {
    font-size: 0.6rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.method-card:nth-child(1) .method-tag { color: var(--wine); }
.method-card:nth-child(2) .method-tag { color: var(--teal); }

.method-name {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.5rem;
    font-weight: 400;
    line-height: 1.2;
    margin-bottom: 0.75rem;
}

.method-card:nth-child(1) .method-name { color: var(--wine-dark); }
.method-card:nth-child(2) .method-name { color: var(--teal); }
.method-body { font-size: 0.8rem; line-height: 1.85; color: var(--muted); }
.method-body strong { color: var(--text); font-weight: 400; }

/* Info Table */
.info-table {
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 1rem;
}

.info-row {
    display: grid;
    grid-template-columns: 140px 1fr;
}

.info-row + .info-row { border-top: 1px solid var(--border); }

.info-key {
    padding: 0.8rem 1rem;
    font-size: 0.65rem;
    letter-spacing: 0.08em;
    color: #999;
    background: #f5f4f0;
    border-right: 1px solid var(--border);
    display: flex;
    align-items: center;
}

.info-val {
    padding: 0.8rem 1rem;
    font-size: 0.8rem;
    color: var(--text);
    background: #fff;
    display: flex;
    align-items: center;
    line-height: 1.6;
}

/* Dataset Stats */
.dataset-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin-top: 1rem;
}

.ds-cell {
    padding: 1.2rem 1.2rem 1rem;
    border-right: 1px solid var(--border);
}

.ds-cell:last-child { border-right: none; }
.ds-cell:nth-child(1) { background: var(--gold-light); }
.ds-cell:nth-child(2) { background: var(--wine-light); }
.ds-cell:nth-child(3) { background: var(--teal-light); }

.ds-num {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.4rem;
    font-weight: 300;
    line-height: 1;
    margin-bottom: 4px;
}

.ds-cell:nth-child(1) .ds-num { color: var(--gold); }
.ds-cell:nth-child(2) .ds-num { color: var(--wine); }
.ds-cell:nth-child(3) .ds-num { color: var(--teal); }
.ds-label { font-size: 0.72rem; color: var(--text); }
.ds-sub { font-size: 0.65rem; color: var(--muted); margin-top: 2px; }

/* Framework Blocks */
.framework-block {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
}

.fw-step {
    padding: 1.2rem 1.2rem 1rem;
    border-radius: 10px;
    border: 1px solid var(--border);
    background: #fff;
}

.fw-num {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2rem;
    font-weight: 300;
    color: var(--gold);
    line-height: 1;
    margin-bottom: 6px;
}

.fw-name { font-size: 0.8rem; color: var(--text); line-height: 1.5; }
.fw-sub { font-size: 0.65rem; color: var(--muted); margin-top: 4px; }

.source-link {
    display: inline-block;
    font-size: 0.72rem;
    color: var(--teal) !important;
    border-bottom: 1px solid rgba(26,122,110,0.3);
    padding-bottom: 1px;
    margin-top: 0.75rem;
    text-decoration: none;
}

/* Responsive */
@media (max-width: 900px) {
    .page-title { font-size: 3.8rem; }
    .method-cards, .framework-block, .dataset-stats { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR CONTENT
# =====================================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-title">wine.</div>
    <div class="sidebar-sub">quality prediction</div>

    <div class="team-title">Team</div>

    <div class="member">
        <div class="member-name">Abil Faroj Nur Yahya</div>
        <div class="member-id">24051214072</div>
    </div>

    <div class="member">
        <div class="member-name">Felix Kristanto</div>
        <div class="member-id">24051214098</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# MAIN CONTENT
# =====================================================
st.markdown(f"""
<div class="page-header">
    <div class="eyebrow">About Project</div>
    <div class="page-title">
        Project<br>
        <em>Overview.</em>
    </div>
</div>

<div class="divider"></div>

<div class="section-label">01 · Metode</div>
<div class="method-cards">
    <div class="method-card">
        <div class="method-tag">Classification</div>
        <div class="method-name">Logistic Regression</div>
        <div class="method-body">
            Memprediksi kualitas wine sebagai <strong>Good</strong> atau <strong>Bad</strong> berdasarkan karakteristik kimia wine.
        </div>
    </div>
    <div class="method-card">
        <div class="method-tag">Clustering</div>
        <div class="method-name">K-Means Clustering</div>
        <div class="method-body">
            Mengelompokkan tipe wine berdasarkan kemiripan karakteristik kimianya.
        </div>
    </div>
</div>

<div class="divider"></div>

<div class="section-label">02 · Dataset</div>
<div class="info-table">
    <div class="info-row">
        <div class="info-key">Dataset</div>
        <div class="info-val">Wine Quality Dataset</div>
    </div>
    <div class="info-row">
        <div class="info-key">Sumber</div>
        <div class="info-val">Kaggle — yasserh/wine-quality-dataset</div>
    </div>
</div>

<div class="dataset-stats">
    <div class="ds-cell">
        <div class="ds-num">{jumlah_data}</div>
        <div class="ds-label">Jumlah Data</div>
        <div class="ds-sub">total rows</div>
    </div>
    <div class="ds-cell">
        <div class="ds-num">{jumlah_fitur}</div>
        <div class="ds-label">Jumlah Fitur</div>
        <div class="ds-sub">chemical features</div>
    </div>
    <div class="ds-cell">
        <div class="ds-num">{jumlah_kelas}</div>
        <div class="ds-label">Kelas</div>
        <div class="ds-sub">quality labels</div>
    </div>
</div>

<a class="source-link" href="https://www.kaggle.com/datasets/yasserh/wine-quality-dataset" target="_blank">
    ↗ Lihat dataset di Kaggle
</a>

<div class="divider"></div>

<div class="section-label">03 · Framework</div>
<div class="framework-block">
    <div class="fw-step">
        <div class="fw-num">01</div>
        <div class="fw-name">Business Understanding</div>
        <div class="fw-sub">Memahami tujuan proyek</div>
    </div>
    <div class="fw-step">
        <div class="fw-num">02</div>
        <div class="fw-name">Data Understanding</div>
        <div class="fw-sub">Eksplorasi & analisis data</div>
    </div>
    <div class="fw-step">
        <div class="fw-num">03</div>
        <div class="fw-name">Data Preparation</div>
        <div class="fw-sub">Pembersihan & transformasi</div>
    </div>
    <div class="fw-step">
        <div class="fw-num">04</div>
        <div class="fw-name">Modeling</div>
        <div class="fw-sub">Logistic Regression + K-Means</div>
    </div>
    <div class="fw-step">
        <div class="fw-num">05</div>
        <div class="fw-name">Evaluation</div>
        <div class="fw-sub">Pengukuran performa model</div>
    </div>
    <div class="fw-step">
        <div class="fw-num">06</div>
        <div class="fw-name">Deployment</div>
        <div class="fw-sub">Streamlit web application</div>
    </div>
</div>
""", unsafe_allow_html=True)