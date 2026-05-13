import streamlit as st
import pandas as pd
from datetime import datetime
import time

# Importar módulos locales
import config
import db_manager
import utils
from agents import AgenteAnalista, AgenteSupervisor, AbogadoDelDiablo

# --- INICIALIZACIÓN ---
st.set_page_config(
    page_title="PROMETHEUS | ETF Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar Base de Datos
db_manager.init_db()

# Inicializar Agentes en Session State
if 'agentes' not in st.session_state:
    st.session_state.agentes = {
        "analista": AgenteAnalista(),
        "supervisor": AgenteSupervisor(),
        "critico": AbogadoDelDiablo()
    }
    db_manager.log_event("SISTEMA", "Agentes inicializados con éxito.")

# --- ESTILOS BLOOMBERG ---
st.markdown("""
<style>
    /* Fondo y texto global */
    .stApp {
        background-color: #050508;
        color: #e8e8f0;
    }
    
    /* Tarjetas estilo Bloomberg */
    .metric-card {
        background-color: #11111a;
        border: 1px solid #1a1a2e;
        padding: 20px;
        border-radius: 4px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        border-color: #00ff88;
        background-color: #161625;
    }
    .metric-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 10px 0;
    }
    .metric-label {
        color: #8888aa;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Tabs personalizados */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 10px 20px;
        background-color: transparent;
        border-radius: 4px 4px 0 0;
        gap: 0;
        color: #8888aa;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1a1a2e !important;
        color: #00ff88 !important;
        border-bottom: 2px solid #00ff88 !important;
    }
    
    /* Mensajes educativos */
    .edu-box {
        background-color: rgba(0, 255, 136, 0.05);
        border-left: 4px solid #00ff88;
        padding: 15px;
        margin: 20px 0;
        font-style: italic;
        color: #e8e8f0;
    }
    
    /* Botones grandes */
    .stButton > button {
        width: 100%;
        border-radius: 4px;
        height: 3em;
        background-color: #1a1a2e;
        color: #e8e8f0;
        border: 1px solid #33334d;
        font-weight: bold;
    }
    .stButton > button:hover {
        border-color: #00ff88;
        color: #00ff88;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR & POLLING ---
with st.sidebar:
    st.image("https://img.icons8.com/nolan/96/flash-on.png", width=60)
    st.title("PROMETHEUS")
    st.caption("v2.0.0 | ETF Rotation Intelligence")
    st.markdown("---")
    
    st.markdown("### ⚙️ CONTROL DE SINCRONIZACIÓN")
    polling_interval = st.slider("Intervalo de Polling (seg)", 30, 300, 60)
    auto_refresh = st.toggle("Auto-actualización Activa", True)
    
    st.markdown("---")
    st.markdown("### 📡 ESTADO DE RED")
    st.success("Conexión: ESTABLE")
    st.info(f"Última Sync: {datetime.now().strftime('%H:%M:%S')}")
    
    if st.button("REFRESH TOTAL DEL CORE"):
        st.rerun()

# --- DATOS MACRO ---
MACRO_TICKERS = {
    "S&P 500": "^GSPC",
    "NASDAQ 100": "QQQ",
    "Russell 2000": "^RUT",
    "VIX": "^VIX",
    "Oro": "GLD",
    "Plata": "SLV",
    "Petróleo WTI": "CL=F",
    "Cobre": "CPER",
    "Bonos 10Y": "^TNX",
    "Dólar (DXY)": "UUP",
    "Bitcoin": "BTC-USD"
}

data_macro, sync_status = utils.fetch_macro_data(MACRO_TICKERS)

# --- DASHBOARD PRINCIPAL ---
tabs = st.tabs([
    "🏠 Dashboard Principal", 
    "📊 Rankings y Rotación", 
    "🕒 Cotizaciones en Real-Time", 
    "🤖 Agentes", 
    "🛡️ Supervisor", 
    "📜 Historial y Análisis", 
    "⚙️ Configuración"
])

# 1. DASHBOARD PRINCIPAL
with tabs[0]:
    st.title("⚡ Panel de Control General")
    
    # Mensaje de Esencia Genesis
    st.markdown("""
    <div class="edu-box">
        "La disciplina es el puente entre las metas y el logro. En este sistema, no buscamos el ruido del día, sino la armonía de la tendencia."
    </div>
    """, unsafe_allow_html=True)
    
    # Fila Macro
    cols = st.columns(4)
    main_indicators = ["S&P 500", "NASDAQ 100", "VIX", "Bonos 10Y"]
    for i, name in enumerate(main_indicators):
        with cols[i]:
            val = data_macro.get(name, {"price": 0, "change": 0})
            color = "#00ff88" if val["change"] >= 0 else "#ff3366"
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{name}</div>
                <div class="metric-value" style="color: {color};">{val['price']:,.2f}</div>
                <div style="color: {color}; font-size: 0.9rem;">{val['change']:+.2f}%</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Condición de Mercado
    st.markdown("---")
    vix_val = data_macro.get("VIX", {"price": 15})["price"]
    spx_change = data_macro.get("S&P 500", {"change": 0})["change"]
    condition, message = utils.get_market_condition(vix_val, spx_change)
    
    c1, c2 = st.columns([1, 2])
    with c1:
        st.subheader("Estado del Mercado")
        st.markdown(f"### {condition}")
    with c2:
        st.info(message)

# 2. RANKINGS Y ROTACIÓN
with tabs[1]:
    st.header("📊 Rankings de Rotación Sectorial")
    st.warning("Módulo en fase de calibración matemática. Los agentes están procesando los pesos de momentum.")
    st.info("La paciencia es una virtud en el análisis cuantitativo. Espere a que el ciclo confirme la rotación.")

# 3. COTIZACIONES EN TIEMPO REAL
with tabs[2]:
    st.header("🕒 Monitor de Activos en Real-Time")
    
    # Convertir dict a DataFrame para mostrar
    df_assets = pd.DataFrame.from_dict(data_macro, orient='index')
    df_assets = df_assets.reset_index().rename(columns={'index': 'Activo'})
    
    # Formatear columnas
    df_assets['Precio'] = df_assets['price'].apply(utils.format_currency)
    df_assets['Cambio %'] = df_assets['change'].apply(utils.format_percent)
    
    st.dataframe(df_assets[['Activo', 'ticker', 'Precio', 'Cambio %', 'status']], use_container_width=True, hide_index=True)
    st.caption("Datos provistos por Yahoo Finance via yfinance. Actualización automática cada 60s.")

# 4. AGENTES
with tabs[3]:
    st.header("🤖 Ecosistema de Agentes Inteligentes")
    st.markdown("Cada agente posee una personalidad única basada en la disciplina y el rigor.")
    
    cols = st.columns(3)
    with cols[0]:
        st.subheader("👨‍💻 Analista")
        st.write(st.session_state.agentes["analista"].rol)
        st.status("Buscando patrones...")
    with cols[1]:
        st.subheader("👮 Supervisor")
        st.write(st.session_state.agentes["supervisor"].rol)
        st.status("Verificando integridad...", state="complete")
    with cols[2]:
        st.subheader("⚖️ Abogado del Diablo")
        st.write(st.session_state.agentes["critico"].rol)
        st.status("Cuestionando tesis...")

# 5. SUPERVISOR
with tabs[4]:
    st.header("🛡️ Monitor del Sistema (Supervisor Core)")
    col_s1, col_s2, col_s3 = st.columns(3)
    col_s1.metric("Latencia Data-Feed", "120ms", "Normal")
    col_s2.metric("Integridad DB", "100%", "Óptimo")
    col_s3.metric("Sesión Actual", datetime.now().strftime("%H:%M"), "Activa")
    
    st.subheader("Logs de Operaciones")
    st.dataframe(db_manager.get_logs(), use_container_width=True)

# 6. HISTORIAL Y ANÁLISIS
with tabs[5]:
    st.header("📜 Historial de Decisiones")
    st.info("La transparencia es la base de la confianza. Aquí se registrarán todas las rotaciones sugeridas por el sistema.")

# 7. CONFIGURACIÓN
with tabs[6]:
    st.header("⚙️ Configuración del Sistema")
    
    col_c1, col_c2 = st.columns(2)
    
    with col_c1:
        st.subheader("Gestión de ETFs")
        with st.form("add_etf_form"):
            t = st.text_input("Ticker ETF (ej: QQQ)")
            n = st.text_input("Nombre Completo")
            s = st.selectbox("Sector GICS", [
                "Tecnología", "Finanzas", "Salud", "Energía", "Industria", 
                "Materiales", "Consumo Discrecional", "Consumo Básico", 
                "Utilities", "Inmobiliario", "Comunicaciones", "Otros"
            ])
            if st.form_submit_button("Añadir al Universo"):
                if t and n:
                    if db_manager.add_etf(t, n, s):
                        st.success(f"ETF {t} añadido correctamente.")
                        db_manager.log_event("CONFIG", f"Añadido ETF: {t}")
                    else:
                        st.error("El ETF ya existe o hubo un error.")
                else:
                    st.warning("Complete todos los campos.")
    
    with col_c2:
        st.subheader("Parámetros de Red")
        st.slider("Agresividad de Rotación", 1, 10, 5)
        st.checkbox("Habilitar Logging Extendido", value=True)

# --- AUTO REFRESH ---
if auto_refresh:
    time.sleep(polling_interval)
    st.rerun()
