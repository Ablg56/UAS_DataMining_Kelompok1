import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import os

st.set_page_config(
    page_title="Visualization - Wine Quality",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Load Data ─────────────────────────────────────
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, "..", "..", "dataset", "WineQT.csv")
df = pd.read_csv(csv_path)

# ── CSS ───────────────────────────────────────────
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
[data-testid="collapsedControl"]  { display: none !important; }

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 1150px !important;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] { background: var(--wine-dark) !important; border-right: none; }
section[data-testid="stSidebar"] > div { padding: 2rem 1.5rem !important; }

            
header[data-testid="stHeader"] { 
    background: transparent !important; 
}
header[data-testid="stHeader"] button {
    color: var(--text) !important;
}
.st-emotion-cache-12bp31y {color: var(--teal) !important;} /* Override warna teks default Streamlit agar sesuai dengan tema */

.sidebar-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.2rem; margin-bottom: 0; color: white !important;
}
.sidebar-sub  { font-size: 0.7rem; letter-spacing: 0.18em; text-transform: uppercase; opacity: 0.6; margin-bottom: 2rem; }
.team-title   { font-size: 0.65rem; letter-spacing: 0.18em; text-transform: uppercase; opacity: 0.45; margin-bottom: 1rem; }
.member {
    background: rgba(255,255,255,0.05); padding: 0.9rem;
    border-radius: 8px; margin-bottom: 0.7rem; border-left: 2px solid var(--gold);
}
.member-name { font-size: 0.9rem; }
.member-id   { font-size: 0.7rem; opacity: 0.55; margin-top: 4px; }

/* ── Page header ── */
.eyebrow {
    font-size: 0.7rem; letter-spacing: 0.25em;
    text-transform: uppercase; color: var(--gold); margin-bottom: 1rem;
}
.page-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 5.5rem; line-height: 0.92; font-weight: 300;
    color: var(--text); margin-bottom: 2.5rem;
}
.page-title em {
    font-family: 'Cormorant Garamond', serif !important;
    color: var(--wine); font-style: italic;
}

.divider { width: 100%; height: 1px; background: var(--border); margin: 2rem 0; }

.section-label {
    font-size: 0.65rem; letter-spacing: 0.22em; text-transform: uppercase;
    color: #999; margin-bottom: 1.25rem;
    display: flex; align-items: center; gap: 10px;
}
.section-label::before {
    content: ''; display: inline-block; width: 16px;
    height: 1px; background: var(--gold); flex-shrink: 0;
}

/* ── Chart desc ── */
.chart-desc {
    font-size: 0.75rem; color: var(--muted);
    line-height: 1.8; max-width: 680px; margin-bottom: 1.25rem;
}

/* ── Tab override ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    border-bottom: 1px solid var(--border) !important;
    gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.68rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: #aaa !important;
    padding: 0.6rem 1.25rem !important;
    background: transparent !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
}
.stTabs [aria-selected="true"] {
    color: var(--wine) !important;
    border-bottom: 2px solid var(--wine) !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding-top: 1.5rem !important;
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
<div class="eyebrow">Visualization · Analysis</div>
<div class="page-title">Data<br><em>Visualization.</em></div>
""", unsafe_allow_html=True)

# ── Helper: styled figure ─────────────────────────
def styled_fig(w=10, h=5):
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#faf9f7')
    ax.tick_params(colors='#6b6b6b', labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#eeeeee')
    ax.yaxis.grid(True, color='#eeeeee', linewidth=0.7, linestyle='--')
    ax.set_axisbelow(True)
    return fig, ax

cmap_custom = matplotlib.colors.LinearSegmentedColormap.from_list(
    "wine_teal", ["#1a7a6e", "#faf9f7", "#7a1e2e"]
)

# ═════════════════════════════════════════════════
# TABS
# ═════════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    "Heatmap",
    "Histogram",
    "Distribusi Kualitas",
    "Boxplot",
])

# ── Tab 1 · Heatmap ───────────────────────────────
with tab1:
    st.markdown('<div class="section-label">Correlation Heatmap</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="chart-desc">
        Visualisasi korelasi antar fitur kimia wine. Warna merah menandakan
        korelasi positif kuat, warna teal menandakan korelasi negatif kuat.
    </p>
    """, unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#faf9f7')
    sns.heatmap(
        df.corr(numeric_only=True),
        annot=True,
        fmt=".1f",
        cmap=cmap_custom,
        ax=ax,
        annot_kws={"size": 7, "color": "#1a1a1a"},
        linewidths=0.4,
        linecolor="#f0f0f0",
        cbar_kws={"shrink": 0.8}
    )
    ax.tick_params(colors='#6b6b6b', labelsize=8)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# ── Tab 2 · Histogram ─────────────────────────────
with tab2:
    st.markdown('<div class="section-label">Histogram Fitur</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="chart-desc">
        Distribusi nilai tiap fitur kimia wine beserta kurva KDE.
    </p>
    """, unsafe_allow_html=True)

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    selected_col = st.selectbox(
        "Pilih fitur", numeric_cols,
        index=numeric_cols.index('alcohol') if 'alcohol' in numeric_cols else 0
    )

    fig, ax = styled_fig(8, 4)
    sns.histplot(
        df[selected_col], kde=True, ax=ax,
        color='#b8924a', edgecolor='none', alpha=0.8,
        line_kws={"color": "#7a1e2e", "linewidth": 1.5}
    )
    ax.set_xlabel(selected_col, fontsize=9, color='#6b6b6b', fontfamily='monospace')
    ax.set_ylabel("Frekuensi", fontsize=9, color='#6b6b6b', fontfamily='monospace')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# ── Tab 3 · Distribusi Kualitas ───────────────────
with tab3:
    st.markdown('<div class="section-label">Distribusi Kualitas Wine</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="chart-desc">
        Jumlah data per skor kualitas wine (3–8). Menunjukkan sebaran
        label target yang digunakan pada model klasifikasi.
    </p>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        counts = df['quality'].value_counts().sort_index()
        colors_bar = ["#f6e9eb","#e8c5cc","#d49aa4","#bf6e7c","#a84254","#7a1e2e"]
        fig, ax = styled_fig(5, 4)
        bars = ax.bar(counts.index, counts.values,
                      color=colors_bar[:len(counts)], width=0.6, edgecolor='none')
        ax.set_xlabel("Quality Score", fontsize=9, color='#6b6b6b', fontfamily='monospace')
        ax.set_ylabel("Jumlah", fontsize=9, color='#6b6b6b', fontfamily='monospace')
        for bar in bars:
            ax.text(bar.get_x() + bar.get_width()/2,
                    bar.get_height() + 8,
                    str(int(bar.get_height())),
                    ha='center', fontsize=8, color='#6b6b6b', fontfamily='monospace')
        plt.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

    with col_b:
        # Pie chart Good vs Bad (quality >= 6 = good)
        good = (df['quality'] >= 6).sum()
        bad  = len(df) - good
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        fig2.patch.set_facecolor('#ffffff')
        ax2.pie(
            [bad, good],
            labels=["Bad", "Good"],
            colors=["#7a1e2e", "#1a7a6e"],
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops={"edgecolor": "#ffffff", "linewidth": 2},
            textprops={"fontsize": 9, "color": "#1a1a1a", "fontfamily": "monospace"}
        )
        ax2.set_title("Good vs Bad Quality", fontsize=9,
                      color='#6b6b6b', fontfamily='monospace', pad=12)
        plt.tight_layout()
        st.pyplot(fig2)
        plt.close(fig2)

# ── Tab 4 · Boxplot ───────────────────────────────
with tab4:
    st.markdown('<div class="section-label">Boxplot per Kualitas</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="chart-desc">
        Distribusi nilai fitur kimia berdasarkan skor kualitas wine.
        Berguna untuk melihat perbedaan karakteristik antar kelas kualitas.
    </p>
    """, unsafe_allow_html=True)

    numeric_cols2 = [c for c in df.select_dtypes(include='number').columns if c != 'quality']
    box_col = st.selectbox(
        "Pilih fitur untuk boxplot", numeric_cols2,
        index=numeric_cols2.index('alcohol') if 'alcohol' in numeric_cols2 else 0,
        key="box_select"
    )

    fig, ax = styled_fig(9, 4.5)
    quality_order = sorted(df['quality'].unique())
    colors_box    = ["#f6e9eb","#e8c5cc","#d49aa4","#bf6e7c","#a84254","#7a1e2e"]
    palette       = {str(q): c for q, c in zip(quality_order, colors_box)}
    df_box        = df.copy()
    df_box['quality'] = df_box['quality'].astype(str)
    sns.boxplot(
        data=df_box, x='quality', y=box_col, ax=ax,
        hue='quality', palette=palette, legend=False,
        order=[str(q) for q in quality_order],
        linewidth=0.8,
        flierprops={"marker": "o", "markersize": 3,
                    "markerfacecolor": "#b8924a", "alpha": 0.5}
    )
    ax.set_xlabel("Quality Score", fontsize=9, color='#6b6b6b', fontfamily='monospace')
    ax.set_ylabel(box_col, fontsize=9, color='#6b6b6b', fontfamily='monospace')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)