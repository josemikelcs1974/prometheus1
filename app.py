"""
⚡ PROMETHEUS — ETF Rotation Intelligence System
Fase 1: Estructura, Estética y Gestión de Estado
"""

import streamlit as st
import config
from datetime import datetime
import time

# --- CONFIGURACIÓN DE PÁGINA (BLOOMBERG STYLE) ---
st.set_page_config(
    page_title="⚡ PROMETHEUS | v2.0.0",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INYECCIÓN DE CSS PERSONALIZADO ---
st.markdown("""
<style>
    /* Estética Dark Institutional */
    [data-testid="stAppViewContainer"] {
        background-color: #050508;
        color: #e8e8f0;
    }
    [data-testid="stSidebar"] {
        background-color: #010105;
        border-right: 1px solid #1a1a2e;
    }
    
    /* Tipografía Mono */
    html, body, [class*="css"] {
        font-family: 'Courier New', Courier, monospace !important;
    }

    /* Títulos y Enlaces */
    h1, h2, h3 { color: #00ff88 !important; letter-spacing: 0.1em; }
    
    /* Botones Neón */
    .stButton>button {
        background-color: transparent;
        color: #00ff88;
        border: 1px solid #00ff88;
        border-radius: 2px;
        transition: all 0.3s;
        text-transform: uppercase;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00ff88;
        color: #050508;
        box-shadow: 0 0 15px #00ff88;
    }

    /* Divider Neón */
    .prometheus-divider {
        height: 1px;
        background: linear-gradient(to right, transparent, #00ff88, transparent);
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- INICIALIZACIÓN DE ESTADO ---
if 'system_status' not in st.session_state:
    st.session_state.system_status = "OK"
if 'last_refresh' not in st.session_state:
    st.session_state.last_refresh = datetime.now()

# --- SIDEBAR: ESTADO Y CONTROL ---
with st.sidebar:
    st.markdown(f"### ⚡ {config.SYSTEM_NAME}")
    st.caption(f"{config.SYSTEM_SUBTITLE} | v{config.SYSTEM_VERSION}")
    
    st.markdown("---")
    
    # Status Panel
    col_status, col_signal = st.columns(2)
    with col_status:
        st.markdown(f"**STATUS:**  \n:green[{st.session_state.system_status}]")
    with col_signal:
        st.markdown(f"**AGENTS:**  \n:green[ACTIVE]")
        
    st.markdown("---")
    
    # Refresh Control
    refresh_option = st.selectbox("AUTO-REFRESH", ["OFF", "30 seg", "1 min", "5 min"], index=2)
    
    st.button("🔄 ACTUALIZACIÓN GLOBAL")
    
    st.markdown("---")
    st.caption(f"Último Sync: {st.session_state.last_refresh.strftime('%H:%M:%S')} UTC")
    st.caption(f"Backend: Streamlit Core")

# --- MAIN: DASHBOARD BASE ---
def main():
    st.markdown(f"# ⚡ {config.SYSTEM_NAME}")
    st.markdown(f"*{config.SYSTEM_SUBTITLE}*")
    
    st.markdown('<div class="prometheus-divider"></div>', unsafe_allow_html=True)
    
    # Bienvenida e Instrucciones
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("// MÓDULOS DISPONIBLES")
        st.info("""
        1. **📊 MACRO DASHBOARD**: Visualización de 25 activos clave.
        2. **🔄 ROTACIÓN SECTORIAL**: Rankings de momentum dinámicos.
        3. **⚡ AGENTE CRONOS**: El motor de inteligencia macro.
        4. **⚠️ AGENTE NEMESIS**: El supervisor de riesgos.
        """)
        
    with col2:
        st.subheader("// CONFIGURACIÓN")
        st.toggle("Modo Simulación", value=True)
        st.toggle("Alertas Sonoras", value=False)
        st.markdown("---")
        st.warning("⚠️ Pendiente: API Key de Claude para IA.")

    # Log de Auditoría AEGIS
    st.markdown('<div class="prometheus-divider"></div>', unsafe_allow_html=True)
    st.subheader("🛡️ AEGIS: MONITOR DE SISTEMA")
    log_area = st.empty()
    log_area.code(f"""
    [{st.session_state.last_refresh}] PROMETHEUS CORE v{config.SYSTEM_VERSION} INITIALIZED...
    [{st.session_state.last_refresh}] ESTABLECIENDO CONEXIÓN CON DATA PROVIDER...
    [{st.session_state.last_refresh}] MÓDULOS DE IA EN ESPERA DE CREDENCIALES...
    """)

if __name__ == "__main__":
    main()
