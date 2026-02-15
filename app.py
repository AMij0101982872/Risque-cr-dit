import requests
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import os



# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Risk Intelligence Pro",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS AVANCÉ ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #f8fafc;
    }

    /* Container Principal */
    .main-card {
        background-color: #ffffff;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
        border: 1px solid #e2e8f0;
    }

    /* Gradient Header */
    .header-style {
        background: linear-gradient(90deg, #1e293b 0%, #334155 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    /* KPI Cards */
    .kpi-box {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        text-align: center;
    }

    /* Custom Button */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.5rem;
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #1d4ed8;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.4);
    }

    /* Score Text */
    .score-display {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 0;
    }
</style>
""", unsafe_allow_html=True)
MODEL_PATH = os.path.join(os.getcwd(), "credit_risk_model.pkl")

# --- CHARGEMENT DU MODÈLE AVEC CACHE ---
MODEL_URL = "https://drive.google.com/uc?export=download&id=1r18X2X_kDJ_mrJ7z193SNOtOyGUwI4Ve"
MODEL_PATH = "credit_risk_model.pkl"

@st.cache_resource
def load_model():
    try:
        if not os.path.exists(MODEL_PATH):
            st.info("📥 Téléchargement du modèle...")
            r = requests.get(MODEL_URL)
            if r.status_code == 200:
                with open(MODEL_PATH, "wb") as f:
                    f.write(r.content)
                st.success("✅ Modèle téléchargé !")
            else:
                st.error(f"❌ Impossible de télécharger le modèle. Status code: {r.status_code}")
                return None

        model = joblib.load(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle : {e}")
        return None

model = load_model()


# --- LOGIQUE DE PRÉDICTION ---
def predict_risk(data):
    features = ["LIMIT_BAL", "AGE", "MARRIAGE", "PAY_0", "SEX", "PAY_2", "PAY_3", "BILL_AMT1", "PAY_AMT1"]
    df = pd.DataFrame([data])[features]
    proba = model.predict_proba(df)[0][1]
    return proba

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.title("Paramètres")
    st.info("Ce dashboard utilise un modèle Random Forest pour évaluer la probabilité de défaut de paiement.")
    st.divider()
    st.write(" **Version:** 2.0.1 (Premium)")
    st.write(" **Update:** Février 2026")

# --- HEADER ---
st.markdown("""
    <div class="header-style">
        <h1 style='margin:0; color:white;'>Risk Intelligence Dashboard</h1>
        <p style='opacity:0.8; margin-top:10px;'>Système d'Aide à la Décision par Intelligence Artificielle</p>
    </div>
""", unsafe_allow_html=True)

# --- KPI SECTION ---
k1, k2, k3, k4 = st.columns(4)
with k1: st.markdown('<div class="kpi-box"><small>MODÈLE</small><br><b>Random Forest</b></div>', unsafe_allow_html=True)
with k2: st.markdown('<div class="kpi-box"><small>PRÉCISION</small><br><b>84.2%</b></div>', unsafe_allow_html=True)
with k3: st.markdown('<div class="kpi-box"><small>LATENCE</small><br><b>12ms</b></div>', unsafe_allow_html=True)
with k4: st.markdown('<div class="kpi-box"><small>STATUT</small><br><b style="color:green;">● Opérationnel</b></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- MAIN CONTENT ---
if model is None:
    st.error("❌ Erreur : Le fichier 'credit_risk_model.pkl' est introuvable. Veuillez vérifier l'emplacement du modèle.")
else:
    col_form, col_res = st.columns([1, 1.2], gap="large")

    with col_form:
        st.markdown("###  Profil Client")
        with st.container():
            c1, c2 = st.columns(2)
            with c1:
                limit_bal = st.number_input("Limite de Crédit ($)", min_value=0, value=50000, step=1000)
                sex = st.selectbox("Sexe", ["Homme", "Femme"])
            with c2:
                age = st.slider("Âge du client", 18, 90, 35)
                marriage = st.selectbox("Statut Marital", ["Marié(e)", "Célibataire", "Autre"])

            st.markdown("---")
            st.markdown("###  Historique de Paiement")
            
            pay_0 = st.select_slider("État du dernier paiement", options=[-1, 0, 1, 2, 3], format_func=lambda x: "À temps" if x <= 0 else f"{x} mois retard")
            
            c3, c4 = st.columns(2)
            with c3:
                bill_amt = st.number_input("Montant dernière facture ($)", min_value=0, value=2000)
            with c4:
                pay_amt = st.number_input("Dernier versement ($)", min_value=0, value=500)
            
            # Mapping pour le modèle
            sex_map = {"Homme": 1, "Femme": 2}
            marriage_map = {"Marié(e)": 1, "Célibataire": 2, "Autre": 3}
            
            submit = st.button("Lancer l'analyse prédictive")

    with col_res:
        st.markdown("###  Analyse du Risque")
        if submit:
            # Préparation des données
            input_data = {
                "LIMIT_BAL": limit_bal, "AGE": age, "MARRIAGE": marriage_map[marriage],
                "PAY_0": pay_0, "SEX": sex_map[sex], "PAY_2": 0, "PAY_3": 0,
                "BILL_AMT1": bill_amt, "PAY_AMT1": pay_amt
            }
            
            risk_proba = predict_risk(input_data)
            risk_percent = risk_proba * 100
            
            # Détermination de la couleur
            color = "#16a34a" if risk_percent < 30 else "#f59e0b" if risk_percent < 70 else "#dc2626"
            label = "CONFIANCE ÉLEVÉE" if risk_percent < 30 else "VIGILANCE REQUISE" if risk_percent < 70 else "ALERTE DÉFAUT"

            # JAUGE INTERACTIVE
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = risk_percent,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': label, 'font': {'size': 24, 'color': color}},
                gauge = {
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                    'bar': {'color': color},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "#e2e8f0",
                    'steps': [
                        {'range': [0, 30], 'color': 'rgba(22, 163, 74, 0.1)'},
                        {'range': [30, 70], 'color': 'rgba(245, 158, 11, 0.1)'},
                        {'range': [70, 100], 'color': 'rgba(220, 38, 38, 0.1)'}
                    ],
                }
            ))
            fig.update_layout(height=350, margin=dict(l=30, r=30, t=50, b=0))
            st.plotly_chart(fig, use_container_width=True)

            # Recommandation
            if risk_percent < 30:
                st.success(f" **Approbation recommandée.** Le profil présente une probabilité de défaut très faible ({risk_percent:.1f}%).")
            elif risk_percent < 70:
                st.warning(f" **Dossier à surveiller.** Des garanties supplémentaires pourraient être nécessaires ({risk_percent:.1f}%).")
            else:
                st.error(f" **Risque de défaut élevé.** L'octroi de crédit présente un danger financier critique ({risk_percent:.1f}%).")
        
        else:
            st.markdown("""
                <div style="text-align:center; padding: 80px; border: 2px dashed #e2e8f0; border-radius: 20px; color: #94a3b8;">
                    <p>Remplissez les informations à gauche et cliquez sur <b>Analyser</b> pour voir les résultats.</p>
                </div>
            """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")

st.caption("© 2026 Risk Intelligence Pro - Système sécurisé de scoring bancaire.")




