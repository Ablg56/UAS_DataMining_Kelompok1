import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import os
import shap

st.set_page_config(
    page_title="Prediction - Wine Quality",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Load Models ───────────────────────────────────
current_dir = os.path.dirname(os.path.abspath(__file__))

model_cls = joblib.load(os.path.join(current_dir, "..", "..", "model", "logistic_regression_model.pkl"))

try:
    model_clu = joblib.load(os.path.join(current_dir, "..", "..", "model", "kmean_model.pkl"))
except Exception:
    model_clu = None

scaler = joblib.load(os.path.join(current_dir, "..", "..", "model", "wine_scaler.pkl"))
pca    = joblib.load(os.path.join(current_dir, "..", "..", "model", "wine_pca.pkl"))

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

.stApp {
    background: var(--bg);
}

.eyebrow, .page-title, .divider, .section-label, .slider-group-label,
.result-strip, .result-card, .result-tag, .result-value, .result-sub,
.prob-wrap, .prob-label-row, .prob-bar-bg, .prob-bar-fill,
.input-table, .input-row, .input-key, .input-val,
.sidebar-title, .sidebar-sub, .team-title, .member, .member-name, .member-id {
    font-family: 'DM Mono', monospace !important;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}

header[data-testid="stHeader"] button {
    color: var(--text) !important;
}

div[data-testid="stLayoutWrapper"] {
    color: var(--text) !important;
}

.st-emotion-cache-12bp31y {
    color: var(--text) !important;
}

.block-container {
    padding-top: 5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1150px !important;
}

section[data-testid="stSidebar"] {
    background: var(--wine-dark) !important;
    border-right: none;
}

section[data-testid="stSidebar"] > div {
    padding: 2rem 1.5rem !important;
}

.sidebar-title,
.sidebar-sub,
.team-title,
.member,
.member-name,
.member-id {
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

.member-name {
    font-size: 0.9rem;
}

.member-id {
    font-size: 0.7rem;
    opacity: 0.55;
    margin-top: 4px;
}

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

.slider-group-label {
    font-size: 0.6rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text) !important;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--border);
}

div[data-testid="stSlider"] label p {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.78rem !important;
    color: var(--text) !important;
    letter-spacing: 0.02em !important;
}

div[data-testid="stSlider"] div[data-testid="stWidgetLabel"] + div {
    font-family: 'DM Mono', monospace !important;
}

.stButton > button {
    width: 100%;
    background: var(--wine-dark) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.85rem 1rem !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    transition: background 0.2s !important;
    margin-top: 0.5rem !important;
}

.stButton > button:hover {
    background: var(--wine) !important;
}

.result-strip {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 2rem;
}

.result-card {
    padding: 1.6rem 1.6rem 1.4rem;
    border-radius: 10px;
    border: 1px solid var(--border);
}

.result-card.good {
    background: var(--teal-light);
    border-color: rgba(26,122,110,0.15);
}

.result-card.bad {
    background: var(--wine-light);
    border-color: rgba(122,30,46,0.15);
}

.result-card.cluster {
    background: var(--gold-light);
    border-color: rgba(184,146,74,0.15);
}

.result-tag {
    font-size: 0.58rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.good .result-tag {
    color: var(--teal);
}

.bad .result-tag {
    color: var(--wine);
}

.cluster .result-tag {
    color: var(--gold);
}

.result-value {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.8rem;
    font-weight: 300;
    line-height: 1;
    margin-bottom: 6px;
}

.good .result-value {
    color: var(--teal);
}

.bad .result-value {
    color: var(--wine);
}

.cluster .result-value {
    color: #8a6530;
}

.result-sub {
    font-size: 0.72rem;
    color: var(--muted);
}

.prob-wrap {
    margin-bottom: 0.6rem;
}

.prob-label-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.68rem;
    color: var(--muted);
    margin-bottom: 4px;
}

.prob-bar-bg {
    background: #eeebe6;
    border-radius: 4px;
    height: 8px;
    overflow: hidden;
}

.prob-bar-fill {
    height: 100%;
    border-radius: 4px;
    transition: width 0.4s ease;
}

.input-table {
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
}

.input-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
}

.input-row + .input-row {
    border-top: 1px solid var(--border);
}

.input-key {
    padding: 0.55rem 1rem;
    font-size: 0.65rem;
    letter-spacing: 0.05em;
    color: #999;
    background: #f5f4f0;
    border-right: 1px solid var(--border);
}

.input-val {
    padding: 0.55rem 1rem;
    font-size: 0.72rem;
    color: var(--text);
    background: #fff;
}

@media (max-width: 900px) {
    .page-title {
        font-size: 3.8rem;
    }

    .result-strip {
        grid-template-columns: 1fr;
    }
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
<div class="eyebrow">Prediction · Analysis</div>
<div class="page-title">Wine<br><em>Analysis.</em></div>
""", unsafe_allow_html=True)

# ═════════════════════════════════════════════════
# 01 · INPUT
# ═════════════════════════════════════════════════
st.markdown('<div class="section-label">01 · Input Karakteristik Wine</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="slider-group-label">Acidity & Sugar</div>', unsafe_allow_html=True)
    fixed_acidity       = st.slider("Fixed Acidity",       4.0,  16.0,  7.0,  step=0.1)
    volatile_acidity    = st.slider("Volatile Acidity",    0.1,   2.0,  0.5,  step=0.01)
    citric_acid         = st.slider("Citric Acid",         0.0,   1.0,  0.3,  step=0.01)
    residual_sugar      = st.slider("Residual Sugar",      0.5,  16.0,  2.5,  step=0.1)
    chlorides           = st.slider("Chlorides",           0.01,  0.7,  0.08, step=0.01)
    free_sulfur_dioxide = st.slider("Free Sulfur Dioxide", 1,    80,    15)

with col2:
    st.markdown('<div class="slider-group-label">Composition & Density</div>', unsafe_allow_html=True)
    total_sulfur_dioxide = st.slider("Total Sulfur Dioxide", 5,  300,   50)
    density              = st.slider("Density",         0.9900, 1.0050, 0.9960, step=0.0001)
    ph                   = st.slider("pH",               2.5,   4.5,   3.3,  step=0.01)
    sulphates            = st.slider("Sulphates",        0.3,   2.0,   0.6,  step=0.01)
    alcohol              = st.slider("Alcohol",          8.0,  15.0,  10.0,  step=0.1)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

predict_btn = st.button("Analyze Wine Quality")

# ═════════════════════════════════════════════════
# PROSES
# ═════════════════════════════════════════════════
if predict_btn:

    input_data = pd.DataFrame([{
        "fixed acidity":        fixed_acidity,
        "volatile acidity":     volatile_acidity,
        "citric acid":          citric_acid,
        "residual sugar":       residual_sugar,
        "chlorides":            chlorides,
        "free sulfur dioxide":  free_sulfur_dioxide,
        "total sulfur dioxide": total_sulfur_dioxide,
        "density":              density,
        "pH":                   ph,
        "sulphates":            sulphates,
        "alcohol":              alcohol,
    }])

    input_scaled = scaler.transform(input_data)
    prediction   = model_cls.predict(input_scaled)[0]
    probability  = model_cls.predict_proba(input_scaled)[0]

    input_pca    = pca.transform(input_scaled)
    cluster_id   = model_clu.predict(input_pca)[0] if model_clu else 0

    # cluster labels
    if prediction == 1:
        cluster_labels = {
            0: {"name": "Strong Premium Wine",  "desc": "Wine berkualitas dengan kadar alkohol tinggi dan karakter smooth"},
            1: {"name": "Fresh Acidic Wine",    "desc": "Wine segar dengan acidity tinggi dan karakter ringan"},
            2: {"name": "Balanced Luxury Wine", "desc": "Wine premium dengan keseimbangan rasa yang kompleks"},
        }
    else:
        cluster_labels = {
            0: {"name": "Harsh Alcoholic Wine",  "desc": "Kadar alkohol dominan namun kualitas rasa kurang seimbang"},
            1: {"name": "Over Acidic Wine",      "desc": "Keasaman terlalu tinggi sehingga rasa kurang nyaman"},
            2: {"name": "Flat Unbalanced Wine",  "desc": "Karakteristik wine kurang kompleks dan tidak seimbang"},
        }

    cluster      = cluster_labels.get(cluster_id, cluster_labels[0])["name"]
    cluster_desc = cluster_labels.get(cluster_id, cluster_labels[0])["desc"]

    # ─────────────────────────────────────────────
    # 02 · HASIL PREDIKSI
    # ─────────────────────────────────────────────
    st.markdown('<div class="section-label">02 · Hasil Prediksi</div>', unsafe_allow_html=True)

    quality_class = "good" if prediction == 1 else "bad"
    quality_label = "Good Quality"  if prediction == 1 else "Bad Quality"
    quality_icon  = "🍷" if prediction == 1 else "⚠️"
    prob_bad      = probability[0]
    prob_good     = probability[1]

    st.markdown(f"""
    <div class="result-strip">
        <div class="result-card {quality_class}">
            <div class="result-tag">Classification · Logistic Regression</div>
            <div class="result-value">{quality_icon} {quality_label}</div>
            <div class="result-sub">Berdasarkan karakteristik kimia wine</div>
        </div>
        <div class="result-card cluster">
            <div class="result-tag">Clustering Analysis</div>
            <div class="result-value">{cluster}</div>
            <div class="result-sub">{cluster_desc}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ─────────────────────────────────────────────
    # 03 · PROBABILITAS
    # ─────────────────────────────────────────────
    st.markdown('<div class="section-label">03 · Probabilitas Klasifikasi</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="prob-wrap">
        <div class="prob-label-row"><span>Bad Quality</span><span>{prob_bad:.1%}</span></div>
        <div class="prob-bar-bg">
            <div class="prob-bar-fill" style="width:{prob_bad*100:.1f}%; background:#7a1e2e;"></div>
        </div>
    </div>
    <div class="prob-wrap">
        <div class="prob-label-row"><span>Good Quality</span><span>{prob_good:.1%}</span></div>
        <div class="prob-bar-bg">
            <div class="prob-bar-fill" style="width:{prob_good*100:.1f}%; background:#1a7a6e;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(5, 2.8))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#faf9f7')
    ax.bar(["Bad", "Good"], [prob_bad, prob_good],
           color=["#7a1e2e", "#1a7a6e"], width=0.4, edgecolor='none')
    ax.set_ylim(0, 1.15)
    for i, v in enumerate([prob_bad, prob_good]):
        ax.text(i, v + 0.04, f"{v:.2f}", ha='center',
                fontsize=9, color='#6b6b6b', fontfamily='monospace')
    ax.tick_params(colors='#6b6b6b', labelsize=8)
    for spine in ax.spines.values():
        spine.set_edgecolor('#eeeeee')
    ax.yaxis.grid(True, color='#eeeeee', linewidth=0.8)
    ax.set_axisbelow(True)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ─────────────────────────────────────────────
    # 04 · SHAP
    # ─────────────────────────────────────────────
    st.markdown('<div class="section-label">04 · SHAP Explainable AI</div>', unsafe_allow_html=True)

    try:
        feature_names = input_data.columns.tolist()

        # ── Ambil LogisticRegression dari pipeline (named_steps['classifier']) ──
        clf = model_cls.named_steps["classifier"]

        # ── Background: hitung mean & std dari scaler untuk buat dummy background ──
        # Karena X_train tidak disimpan, kita pakai mean vector dari scaler
        # sebagai titik referensi (sama dengan feature_perturbation="interventional")
        background = np.zeros((1, len(feature_names)))  # mean setelah scaling = 0
        masker     = shap.maskers.Independent(background)

        explainer   = shap.LinearExplainer(clf, masker)
        shap_values = explainer.shap_values(input_scaled)

        # ── Normalkan shape ──
        # LinearExplainer binary bisa return:
        # - ndarray shape (1, n_features)  → ambil baris 0
        # - list [class0, class1]          → ambil class1 (Good), baris 0
        if isinstance(shap_values, list):
            sv = np.array(shap_values[1] if len(shap_values) > 1 else shap_values[0])
        else:
            sv = np.array(shap_values)

        shap_row = sv[0] if sv.ndim == 2 else sv

        if len(shap_row) != len(feature_names):
            st.warning(f"Panjang SHAP ({len(shap_row)}) ≠ jumlah fitur ({len(feature_names)}).")
        else:
            shap_df = pd.DataFrame({"Feature": feature_names, "SHAP Value": shap_row})
            shap_df["Abs"] = shap_df["SHAP Value"].abs()
            shap_df = shap_df.sort_values("Abs", ascending=True)

            # ── Chart ──
            fig_shap, ax_shap = plt.subplots(figsize=(8, 5))
            fig_shap.patch.set_facecolor('#ffffff')
            ax_shap.set_facecolor('#faf9f7')
            colors_s = ["#1a7a6e" if x > 0 else "#7a1e2e" for x in shap_df["SHAP Value"]]
            ax_shap.barh(shap_df["Feature"], shap_df["SHAP Value"],
                         color=colors_s, edgecolor='none', height=0.55)
            ax_shap.axvline(0, color='#cccccc', linewidth=1)
            ax_shap.set_xlabel("SHAP Impact", fontsize=9, color='#6b6b6b', fontfamily='monospace')
            ax_shap.tick_params(colors='#6b6b6b', labelsize=8)
            for spine in ax_shap.spines.values():
                spine.set_edgecolor('#eeeeee')
            ax_shap.xaxis.grid(True, color='#eeeeee', linewidth=0.7)
            ax_shap.set_axisbelow(True)
            plt.tight_layout()
            st.pyplot(fig_shap)
            plt.close(fig_shap)

            # ── Kontribusi teks dua kolom ──
            pos_df = shap_df[shap_df["SHAP Value"] > 0].sort_values("SHAP Value", ascending=False)
            neg_df = shap_df[shap_df["SHAP Value"] < 0].sort_values("SHAP Value")

            col_p, col_n = st.columns(2, gap="large")

            with col_p:
                st.markdown('<div class="section-label">Mendukung Good Quality</div>', unsafe_allow_html=True)
                if len(pos_df):
                    rows = "".join(
                        f'<div class="shap-item shap-pos">'
                        f'<span>✅ {r["Feature"]}</span>'
                        f'<span>+{r["SHAP Value"]:.3f}</span></div>'
                        for _, r in pos_df.iterrows()
                    )
                    st.markdown(rows, unsafe_allow_html=True)
                else:
                    st.markdown('<span style="font-size:0.75rem;color:#aaa;">Tidak ada</span>', unsafe_allow_html=True)

            with col_n:
                st.markdown('<div class="section-label">Mendukung Bad Quality</div>', unsafe_allow_html=True)
                if len(neg_df):
                    rows = "".join(
                        f'<div class="shap-item shap-neg">'
                        f'<span>⚠️ {r["Feature"]}</span>'
                        f'<span>{r["SHAP Value"]:.3f}</span></div>'
                        for _, r in neg_df.iterrows()
                    )
                    st.markdown(rows, unsafe_allow_html=True)
                else:
                    st.markdown('<span style="font-size:0.75rem;color:#aaa;">Tidak ada</span>', unsafe_allow_html=True)

    except Exception as e:
        st.warning(f"SHAP tidak dapat dijalankan: {e}")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ─────────────────────────────────────────────
    # 05 · INPUT DATA
    # ─────────────────────────────────────────────
    st.markdown('<div class="section-label">05 · Input Data</div>', unsafe_allow_html=True)

    rows_html = "".join(
        f'<div class="input-row">'
        f'<div class="input-key">{k}</div>'
        f'<div class="input-val">{v}</div>'
        f'</div>'
        for k, v in input_data.iloc[0].items()
    )
    st.markdown(f'<div class="input-table">{rows_html}</div>', unsafe_allow_html=True)