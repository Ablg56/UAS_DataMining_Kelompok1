import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import os
import pandas as pd

st.set_page_config(
    page_title="Dataset Overview - Wine Quality",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Load Data ──────────────────────────────────────
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "..", "..", "dataset", "WineQT.csv")
df = pd.read_csv(csv_path)

# ── CSS ────────────────────────────────────────────
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

html, body, [class*="css"] { font-family: 'DM Mono', monospace; }

.stApp { background: var(--bg); }

#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header[data-testid="stAppHeader"] { display: none !important; }
header[data-testid="stHeader"] { 
    background: transparent !important; 
}
header[data-testid="stHeader"] button {
    color: var(--text) !important;
}
.st-emotion-cache-12bp31y {color: var(--teal) !important;} /* Override warna teks default Streamlit agar sesuai dengan tema */

[data-testid="collapsedControl"]  { display: none !important; }

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1150px !important;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: var(--wine-dark) !important;
    border-right: none;
}
section[data-testid="stSidebar"] > div { padding: 2rem 1.5rem !important; }


.sidebar-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.2rem;
    margin-bottom: 0;
    color: white !important;
}
.sidebar-sub {
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.6;
    margin-bottom: 2rem;
    color: white !important;
}
.team-title {
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    opacity: 0.45;
    margin-bottom: 1rem;
    color: white !important;
}
.member {
    background: rgba(255,255,255,0.05);
    padding: 0.9rem;
    border-radius: 8px;
    margin-bottom: 0.7rem;
    border-left: 2px solid var(--gold);
    color: white !important;
}
.member-name { font-size: 0.9rem; color: white !important; }
.member-id   { font-size: 0.7rem; opacity: 0.55; margin-top: 4px; color: white !important; }

/* ── Page Header ── */
.eyebrow {
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 1rem;
}
.page-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 5.5rem;
    line-height: 0.92;
    font-weight: 300;
    color: var(--text);
    margin-bottom: 2.5rem;
}
.page-title em {
    font-family: 'Cormorant Garamond', serif !important;
    color: var(--wine);
    font-style: italic;
}

/* ── Divider ── */
.divider { width: 100%; height: 1px; background: var(--border); margin: 2rem 0; }

/* ── Section Label ── */
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

/* ── Info stat strip ── */
.info-strip {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
    margin-bottom: 2rem;
}
.info-cell {
    padding: 1.2rem 1.4rem 1rem;
    border-right: 1px solid var(--border);
}
.info-cell:last-child { border-right: none; }
.info-cell:nth-child(1) { background: var(--wine-light); }
.info-cell:nth-child(2) { background: var(--gold-light); }
.info-cell:nth-child(3) { background: var(--teal-light); }

.info-num {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.8rem;
    font-weight: 300;
    line-height: 1;
    margin-bottom: 5px;
}
.info-cell:nth-child(1) .info-num { color: var(--wine); }
.info-cell:nth-child(2) .info-num { color: var(--gold); }
.info-cell:nth-child(3) .info-num { color: var(--teal); }

.info-label { font-size: 0.78rem; color: var(--text); }
.info-sub   { font-size: 0.65rem; color: var(--muted); margin-top: 2px; }

/* ── Streamlit dataframe & table override ── */
.stDataFrame, [data-testid="stDataFrame"] {
    border-radius: 10px !important;
    overflow: hidden !important;
    border: 1px solid var(--border) !important;
}

/* ── Chart container ── */
.chart-wrap {
    background: #fff;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.5rem;
    margin-top: 0.5rem;
}

@media (max-width: 900px) {
    .page-title { font-size: 3.8rem; }
    .info-strip { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────
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

# ── Page Header ──────────────────────────────────
st.markdown("""
<div class="eyebrow">Dataset · CRISP-DM</div>
<div class="page-title">Dataset<br><em>Overview.</em></div>
""", unsafe_allow_html=True)

# ═════════════════════════════════════════════════
# 01 · INFORMASI DATASET
# ═════════════════════════════════════════════════
st.markdown('<div class="section-label">01 · Informasi Dataset</div>', unsafe_allow_html=True)

# Stat strip
missing_total = int(df.isnull().sum().sum())
st.markdown(f"""
<div class="info-strip">
    <div class="info-cell">
        <div class="info-num">{df.shape[0]}</div>
        <div class="info-label">Jumlah Data</div>
        <div class="info-sub">total rows</div>
    </div>
    <div class="info-cell">
        <div class="info-num">{df.shape[1]}</div>
        <div class="info-label">Jumlah Kolom</div>
        <div class="info-sub">features</div>
    </div>
    <div class="info-cell">
        <div class="info-num">{missing_total}</div>
        <div class="info-label">Missing Value</div>
        <div class="info-sub">total null cells</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Preview data
st.markdown('<div class="section-label" style="margin-top:1.5rem;">Preview Data</div>', unsafe_allow_html=True)
st.dataframe(df.head(), use_container_width=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ═════════════════════════════════════════════════
# 02 · STATISTIK DATASET
# ═════════════════════════════════════════════════
st.markdown('<div class="section-label">02 · Statistik Dataset</div>', unsafe_allow_html=True)
st.dataframe(df.describe(), use_container_width=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ═════════════════════════════════════════════════
# 03 · MISSING VALUE
# ═════════════════════════════════════════════════
st.markdown('<div class="section-label">03 · Missing Value</div>', unsafe_allow_html=True)

missing_df = df.isnull().sum().reset_index()
missing_df.columns = ["Feature", "Missing Count"]
st.dataframe(missing_df, use_container_width=True, hide_index=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ═════════════════════════════════════════════════
# 04 · VISUALISASI DATA
# ═════════════════════════════════════════════════
st.markdown('<div class="section-label">04 · Visualisasi Data</div>', unsafe_allow_html=True)

# Palette sesuai tema
palette_wine = ["#f6e9eb", "#e8c5cc", "#d49aa4", "#bf6e7c", "#a84254", "#7a1e2e", "#55131f"]

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("**Distribusi Kualitas Wine**")
    fig1, ax1 = plt.subplots(figsize=(5, 3.5))
    fig1.patch.set_facecolor('#ffffff')
    ax1.set_facecolor('#faf9f7')
    counts = df['quality'].value_counts().sort_index()
    bars = ax1.bar(counts.index, counts.values,
                   color=["#7a1e2e", "#b8924a", "#1a7a6e",
                           "#a84254", "#d49aa4", "#55131f"][:len(counts)],
                   width=0.6, edgecolor='none')
    ax1.set_xlabel("Quality Score", fontsize=9, color='#6b6b6b', fontfamily='monospace')
    ax1.set_ylabel("Jumlah Data", fontsize=9, color='#6b6b6b', fontfamily='monospace')
    ax1.tick_params(colors='#6b6b6b', labelsize=8)
    for spine in ax1.spines.values():
        spine.set_edgecolor(color='#eeeeee')
    ax1.yaxis.grid(True, color='#eeeeee', linewidth=0.8)
    ax1.set_axisbelow(True)
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close(fig1)

with col2:
    st.markdown("**Distribusi Kadar Alkohol**")
    fig2, ax2 = plt.subplots(figsize=(5, 3.5))
    fig2.patch.set_facecolor('#ffffff')
    ax2.set_facecolor('#faf9f7')
    ax2.hist(df['alcohol'], bins=20, color='#b8924a', edgecolor='none', alpha=0.85)
    ax2.set_xlabel("Alcohol (%)", fontsize=9, color='#6b6b6b', fontfamily='monospace')
    ax2.set_ylabel("Frekuensi", fontsize=9, color='#6b6b6b', fontfamily='monospace')
    ax2.tick_params(colors='#6b6b6b', labelsize=8)
    for spine in ax2.spines.values():
        spine.set_edgecolor(color='#eeeeee')
    ax2.yaxis.grid(True, color='#eeeeee', linewidth=0.8)
    ax2.set_axisbelow(True)
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close(fig2)

# Correlation heatmap
st.markdown("**Correlation Heatmap**", unsafe_allow_html=False)
fig3, ax3 = plt.subplots(figsize=(10, 4.5))
fig3.patch.set_facecolor('#ffffff')
cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
    "wine_teal", ["#1a7a6e", "#faf9f7", "#7a1e2e"]
)
sns.heatmap(
    df.corr(numeric_only=True),
    ax=ax3,
    cmap=cmap,
    annot=True,
    fmt=".1f",
    annot_kws={"size": 7, "color": "#1a1a1a"},
    linewidths=0.4,
    linecolor="#f0f0f0",
    cbar_kws={"shrink": 0.8}
)
ax3.tick_params(colors='#6b6b6b', labelsize=8)
plt.tight_layout()
st.pyplot(fig3)
plt.close(fig3)