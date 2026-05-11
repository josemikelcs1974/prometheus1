import streamlit as st
import config
from datetime import datetime
import pandas as pd
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="⚡ PROMETHEUS | v2.0.0",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTÉTICA INSTITUCIONAL (BLOOMBERG) ---
st.markdown("""
<style>
    /* Global Styles */
    [data-testid="stAppViewContainer"] { background-color: #050508; color: #e8e8f0; }
    [data-testid="stHeader"] { background: rgba(5, 5, 8, 0.8); }
    [data-testid="stSidebar"] { background-color: #010105; border-right: 1px solid #1a1a2e; }
    
    /* Typography */
    .mono-text { font-family: 'JetBrains Mono', 'Fira Code', monospace; }
    h1, h2, h3 { font-family: 'Inter', sans-serif; color: #00ff88 !important; letter-spacing: 0.05em; font-weight: 800; }
    
    /* Custom Components */
    .status-badge {
        background: rgba(0, 255, 136, 0.1);
        border: 1px solid rgba(0, 255, 136, 0.3);
        color: #00ff88;
        padding: 4px 12px;
        border-radius: 4px;
        font-size: 0.7rem;
        font-weight: bold;
    }
    
    .metric-card {
        background: #0d0d14;
        border: 1px solid #1a1a2e;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
    }

    /* Logs Area */
    .log-container {
        height: 250px;
        overflow-y: auto;
        background: #08080c;
        border: 1px solid #1a1a2e;
        padding: 10px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 0.7rem;
        color: #00ff88;
    }
</style>
""", unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'initialized' not in st.session_state:
    st.session_state.initialized = True
    st.session_state.logs = [f"[{datetime.now().strftime('%H:%M:%S')}] SYSTEM INITIALIZED"]

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/nolan/64/flash-on.png", width=50)
    st.markdown(f"# {config.SYSTEM_NAME}")
    st.caption(f"{config.SYSTEM_SUBTITLE} | v{config.SYSTEM_VERSION}")
    
    st.markdown("---")
    st.markdown("### 🛠️ CONTROL PANEL")
    
    refresh_rate = st.selectbox("AUTOMATED SYNC", ["OFF", "30S", "1M", "5M"], index=2)
    st.button("🔄 REFRESH GLOBAL CORE")
    
    st.markdown("---")
    st.markdown("### 🛡️ AEGIS STATUS")
    col1, col2 = st.columns(2)
    col1.markdown(f":green[● ONLINE]")
    col2.markdown(f":green[● ACTIVE]")
    
    st.markdown("---")
    st.info("⚠️ IA AGENTS: PENDING API KEY")

# --- MAIN DASHBOARD ---
def render_header():
    col_l, col_r = st.columns([3, 1])
    with col_l:
        st.title(f"⚡ {config.SYSTEM_NAME} CORE")
        st.markdown(f"**{config.SYSTEM_SUBTITLE}** — *Institutional Intelligence Engine*")
    with col_r:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f'<div class="status-badge">SESSION ACTIVE: {datetime.now().strftime("%H:%M UTC")}</div>', unsafe_allow_html=True)

def render_modules():
    st.markdown("---")
    st.subheader("// ACTIVE MODULES")
    
    cols = st.columns(4)
    modules = [
        ("📊", "MACRO", "25 Global Assets"),
        ("🔄", "ROTATION", "13 Sectoral Matrices"),
        ("⚡", "CRONOS", "IA Prediction Engine"),
        ("⚠️", "NEMESIS", "Risk Surveillance")
    ]
    
    for i, (icon, name, desc) in enumerate(modules):
        with cols[i]:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 2rem;">{icon}</div>
                <div style="font-weight: bold; color: #00ff88; margin: 10px 0;">{name}</div>
                <div style="font-size: 0.7rem; color: #8888aa;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

def render_logs():
    st.markdown("---")
    st.subheader("📡 AEGIS REAL-TIME DATA STREAM")
    
    new_log = f"[{datetime.now().strftime('%H:%M:%S')}] PING: DATA PROVIDER CONNECTED (SIMULATION)"
    st.session_state.logs.append(new_log)
    if len(st.session_state.logs) > 50: st.session_state.logs.pop(0)
    
    log_text = "\n".join(reversed(st.session_state.logs))
    st.markdown(f'<div class="log-container"><pre>{log_text}</pre></div>', unsafe_allow_html=True)

def render_compatibility_notice():
    st.markdown("---")
    st.warning("🔄 **COMPATIBILITY MODE ENABLED**: This app is currently running in Streamlit mode to ensure 100% platform stability as requested by the developer.")

# --- EXECUTION ---
render_header()
render_modules()
render_logs()
render_compatibility_notice()

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f'<div style="text-align: center; color: #444466; font-size: 0.6rem;">PROMETHEUS v{config.SYSTEM_VERSION} | CODED BY AI STUDIO EXPERT AGENT</div>', unsafe_allow_html=True)
