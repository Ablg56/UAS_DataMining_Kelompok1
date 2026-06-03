import streamlit as st

st.set_page_config(
    page_title="Wine Quality",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# STYLING (CSS KUSTOM)
# =====================================================
st.markdown("""
<style>
/* 1. IMPORT FONTS VIA GOOGLE FONTS */
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300&family=DM+Mono:wght@300;400&display=swap');

/* 2. ROOT VARIABLE COLOR PALETTE */
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

/* Base background */
.stApp {
    background: var(--bg);
}

/* 3. AMANKAN SELEKTOR FONT (Hanya menyerang class kustom kita, tidak merusak tombol sistem) */
.hero, .eyebrow, .title, .desc, .pills, .pill, .divider, 
.overview-grid, .overview-title, .overview-text, .stats, .card, 
.card-label, .card-sub, .sidebar-title, .sidebar-sub, .team-title, 
.member, .member-name, .member-id {
    font-family: 'DM Mono', monospace !important;
}

/* Sembunyikan menu & footer bawaan, tapi amankan tombol sidebar */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }

/* Biarkan header transparan agar tombol panah tetap berfungsi dan kelihatan */
header[data-testid="stHeader"] { 
    background: transparent !important; 
}
header[data-testid="stHeader"] button {
    color: var(--text) !important; /* Warnanya disesuaikan agar kontras */
}

/* 4. LAYOUT SPACING */
.block-container {
    padding-top: 2rem !important; /* Ruang aman agar teks tidak tertabrak tombol panah */
    padding-bottom: 2rem !important;
    max-width: 1150px !important;
}

/* 5. SIDEBAR STYLING */
section[data-testid="stSidebar"] {
    background: var(--wine-dark) !important;
    border-right: none;
}

section[data-testid="stSidebar"] > div {
    padding: 2rem 1.5rem !important;
}

/* Styling teks di dalam elemen kustom sidebar kita */
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

/* 6. MAIN CONTENT HERO SECTION */
.hero { margin-top: 1rem; }

.eyebrow {
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    color: var(--gold);
    margin-bottom: 1rem;
}

.title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 5.5rem;
    line-height: 0.92;
    font-weight: 300;
    color: var(--text);
}

.title em {
    font-family: 'Cormorant Garamond', serif !important;
    color: var(--wine);
    font-style: italic;
}

.desc {
    margin-top: 2rem;
    max-width: 520px;
    line-height: 2;
    font-size: 0.9rem;
    color: var(--muted);
}

.pills { display: flex; gap: 10px; margin-top: 2rem; flex-wrap: wrap; }
.pill {
    background: var(--wine-light);
    color: var(--wine) !important;
    padding: 8px 14px;
    border-radius: 5px;
    font-size: 0.75rem;
    border: 1px solid rgba(122,30,46,0.12);
}
.st-emotion-cache-12bp31y {color: var(--teal) !important;} /* Override warna teks default Streamlit agar sesuai dengan tema */
.divider { width: 100%; height: 1px; background: var(--border); margin: 1.2rem 0; }

/* 7. GRID OVERVIEW */
.overview-grid {
    display: grid;
    grid-template-columns: 180px 1fr;
    gap: 2rem;
    align-items: start;
}

.overview-title {
    font-size: 0.7rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #999;
}

.overview-text { line-height: 2; color: var(--muted); font-size: 0.9rem; }

/* 8. GRID STATS / CARDS */
.stats { margin-top: 3rem; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
.card { padding: 1.6rem; border-radius: 10px; border: 1px solid var(--border); }
.card:nth-child(1) { background: var(--wine-light); }
.card:nth-child(2) { background: var(--gold-light); }
.card:nth-child(3) { background: var(--teal-light); }

.card-number {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 3.5rem;
    line-height: 1;
    margin-bottom: 0.5rem;
}
.card-label { font-size: 1rem; color: var(--text); }
.card-sub { font-size: 0.8rem; color: var(--muted); margin-top: 0.3rem; }

/* 9. RESPONSIVE DESIGN */
@media (max-width: 900px){
    .title { font-size: 3.8rem; }
    .overview-grid { grid-template-columns: 1fr; gap: 0.5rem; }
    .stats { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# KONTEN SIDEBAR
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
# KONTEN UTAMA
# =====================================================
st.markdown("""
<div class="hero">
    <div class="title">
        Prediksi Wine <br>
        <em>Menggunakan Machine Learning.</em>
    </div>
    <div class="desc">
        Memprediksi kualitas wine menggunakan machine learning
        berdasarkan karakteristik kimia seperti alkohol,
        keasaman, pH, dan parameter lainnya.
    </div>
    <div class="pills">
        <div class="pill">Logistic Regression</div>
        <div class="pill">K-Means Clustering</div>
    </div>
</div>

<div class="divider"></div>

<div class="overview-grid">
    <div class="overview-title">Project Overview</div>
    <div class="overview-text">
        Proyek ini bertujuan untuk menganalisis dan memprediksi
        kualitas wine menggunakan pendekatan machine learning
        berbasis klasifikasi dan clustering.
        Metode Logistic Regression digunakan untuk prediksi kualitas,
        sementara K-Means digunakan untuk segmentasi karakteristik wine.
    </div>
</div>

<div class="stats">
    <div class="card">
        <div class="card-number" style="color:#7a1e2e;">12</div>
        <div class="card-label">Features</div>
        <div class="card-sub">chemical properties</div>
    </div>
    <div class="card">
        <div class="card-number" style="color:#b8924a;">2</div>
        <div class="card-label">Method</div>
        <div class="card-sub">classification + clustering</div>
    </div>
    <div class="card">
        <div class="card-number" style="color:#1a7a6e;">CRISP-DM</div>
        <div class="card-label">Framework</div>
        <div class="card-sub">data mining</div>
    </div>
</div>
""", unsafe_allow_html=True)