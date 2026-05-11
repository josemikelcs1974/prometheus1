"""
╔══════════════════════════════════════════════════════════════════════╗
║          PROMETHEUS — ETF Rotation Intelligence System               ║
║                    app.py — Punto de Entrada                         ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import os
import logging
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

from config import (
    SYSTEM_NAME, SYSTEM_SUBTITLE, SYSTEM_VERSION,
    COLORS, REFRESH_OPTIONS, DEFAULT_REFRESH,
)

# Configuración básica de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("prometheus.app")

# Configuración de página obligatoria (Primera llamada)
st.set_page_config(
    page_title=f"⚡ {SYSTEM_NAME}",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": (
            f"**{SYSTEM_NAME} v{SYSTEM_VERSION}**\n\n"
            f"{SYSTEM_SUBTITLE}\n\n"
            "⚠️ Uso educativo. No constituye asesoramiento financiero."
        ),
    },
)

def inject_global_css() -> None:
    """Carga inyecta el CSS estático desde static/style.css."""
    try:
        css_path = Path(__file__).parent / "static" / "style.css"
        if css_path.exists():
            css_content = css_path.read_text(encoding="utf-8")
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
        else:
            # Fallback mínimo si el archivo no existe
            st.markdown(
                "<style>body { background-color: #050508; color: #e8e8f0; font-family: monospace; }</style>",
                unsafe_allow_html=True
            )
    except Exception as e:
        logger.error(f"Error inyectando CSS: {e}")

def init_session_state() -> None:
    """Inicializa todas las claves de st.session_state con valores por defecto."""
    defaults = {
        "app_start_time":        datetime.now(timezone.utc),
        "last_data_refresh":     None,
        "last_agent_analysis":   None,
        "auto_refresh_interval": DEFAULT_REFRESH,
        "refresh_counter":       0,
        "system_status":         "INICIANDO",
        "macro_snapshot":        None,
        "etf_rankings":          None,
        "cycle_phase":           None,
        "top_sector":            None,
        "cronos_analysis":       None,
        "nemesis_analysis":      None,
        "aegis_report":          None,
        "analysis_history":      [],
        "phase_history":         [],
        "mode_anthropic_api":    False,
        "system_log":            [],
        "last_rotation_time":    None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def detect_operation_modes() -> None:
    """Detecta disponibilidad de ANTHROPIC_API_KEY para agentes IA."""
    try:
        # Intento 1: Streamlit Secrets
        api_key = st.secrets.get("api_keys", {}).get("ANTHROPIC_API_KEY", "")
        # Intento 2: Variable de entorno si no está en secrets
        if not api_key:
            api_key = os.getenv("ANTHROPIC_API_KEY", "")
        
        st.session_state["mode_anthropic_api"] = bool(
            api_key and api_key.startswith("sk-ant")
        )
    except Exception:
        st.session_state["mode_anthropic_api"] = False

def render_sidebar() -> None:
    """Renderiza la barra lateral Bloomberg Style."""
    C = COLORS
    with st.sidebar:
        # Logo y Título
        st.markdown(
            f"<div style='color:{C['green']};font-family:Courier New,monospace;"
            f"font-size:1.1rem;font-weight:bold;letter-spacing:0.15em;"
            f"padding:8px 0 4px 0;border-bottom:1px solid {C['border']};"
            f"margin-bottom:12px;'>⚡ PROMETHEUS</div>"
            f"<div style='color:{C['text_secondary']};font-family:Courier New,monospace;"
            f"font-size:0.68rem;letter-spacing:0.1em;text-transform:uppercase;"
            f"margin-bottom:16px;'>{SYSTEM_SUBTITLE}</div>",
            unsafe_allow_html=True,
        )

        # Panel de Estado del Sistema
        status = st.session_state.get("system_status", "INICIANDO")
        icons  = {
            "OK":       ("🟢", C["green"]), 
            "WARNING":  ("🟡", C["orange"]),
            "CRITICAL": ("🔴", C["red"]), 
            "INICIANDO":("⚪", C["text_muted"])
        }
        icon, color = icons.get(status, ("⚪", C["text_muted"]))
        
        st.markdown(
            f"<div style='background:{C['bg_secondary']};border:1px solid {C['border']};"
            f"border-radius:3px;padding:10px 12px;margin-bottom:16px;'>"
            f"<div style='color:{C['text_secondary']};font-size:0.68rem;"
            f"text-transform:uppercase;margin-bottom:4px;'>ESTADO DEL SISTEMA</div>"
            f"<div style='color:{color};font-size:1.0rem;font-weight:bold;"
            f"font-family:Courier New,monospace;'>{icon} {status}</div></div>",
            unsafe_allow_html=True,
        )

        # Badge Estado IA
        ai_ok = st.session_state.get("mode_anthropic_api", False)
        badge_color = C["green"] if ai_ok else C["orange"]
        badge_text  = "✓ Agentes IA activos" if ai_ok else "⚠ Sin API key IA"
        st.markdown(
            f"<div style='font-family:Courier New,monospace;font-size:0.75rem;"
            f"margin-bottom:16px; color:{badge_color};'>"
            f"{badge_text}</div>",
            unsafe_allow_html=True,
        )

        # Configuración Auto-Refresh
        st.markdown(
            f"<div style='color:{C['text_secondary']};font-size:0.72rem;"
            f"text-transform:uppercase;margin-bottom:4px;'>AUTO-REFRESH</div>",
            unsafe_allow_html=True,
        )
        selected_refresh = st.selectbox(
            "auto-refresh",
            options=list(REFRESH_OPTIONS.keys()),
            index=list(REFRESH_OPTIONS.keys()).index(st.session_state["auto_refresh_interval"]),
            label_visibility="collapsed",
            key="sb_refresh",
        )
        st.session_state["auto_refresh_interval"] = selected_refresh

        # Timestamp Última Actualización
        last_refresh = st.session_state.get("last_data_refresh")
        refresh_ts   = last_refresh.strftime("%H:%M:%S") if last_refresh else "--:--:--"
        st.markdown(
            f"<div style='color:{C['text_muted']};font-family:Courier New,monospace;"
            f"font-size:0.70rem;margin:8px 0 20px 0;'>Última actualización:<br>"
            f"<span style='color:{C['text_secondary']};'>{refresh_ts}</span></div>",
            unsafe_allow_html=True,
        )

        # Botón Actualización Global
        if st.button("⚡ ACTUALIZACIÓN GLOBAL", use_container_width=True, key="btn_global"):
            # Limpieza selectiva
            for k in ["macro_snapshot", "etf_rankings", "cycle_phase", "top_sector"]:
                st.session_state[k] = None
            st.cache_data.clear()
            st.rerun()

        # Footer Sidebar
        start_time = st.session_state.get("app_start_time", datetime.now(timezone.utc))
        uptime     = datetime.now(timezone.utc) - start_time
        h = int(uptime.total_seconds() // 3600)
        m = int((uptime.total_seconds() % 3600) // 60)
        
        st.markdown(
            f"<hr style='border-color:{C['border']};margin:16px 0;'>"
            f"<div style='color:{C['text_muted']};font-family:Courier New,monospace;"
            f"font-size:0.68rem;text-align:center;'>"
            f"v{SYSTEM_VERSION} · Uptime: {h:02d}h {m:02d}m<br>"
            f"Datos: Yahoo Finance · IA: Claude API<br>"
            f"<span style='font-size:0.62rem;'>⚠ Uso educativo exclusivo</span></div>",
            unsafe_allow_html=True,
        )

def render_welcome() -> None:
    """Renderiza la pantalla de bienvenida institucional."""
    C = COLORS
    st.markdown(
        f"<div style='text-align:center;padding:32px 0 20px 0;'>"
        f"<div style='color:{C['green']};font-family:Courier New,monospace;"
        f"font-size:2.8rem;font-weight:bold;letter-spacing:0.1em;'>"
        f"⚡ PROMETHEUS</div>"
        f"<div style='color:{C['text_secondary']};font-family:Courier New,monospace;"
        f"font-size:0.85rem;letter-spacing:0.25em;text-transform:uppercase;"
        f"margin-top:6px;margin-bottom:48px;'>"
        f"ETF ROTATION INTELLIGENCE SYSTEM · v{SYSTEM_VERSION}</div></div>",
        unsafe_allow_html=True,
    )

    # Panel de Módulos (Replicando la estética del Prompt)
    modules = [
        ("01", "📊", "MACRO DASHBOARD",    "25 activos macro en tiempo real"),
        ("02", "🔄", "ROTACIÓN SECTORIAL", "Ranking 13 sectores + top-5 ETFs"),
        ("03", "⚡", "AGENTE CRONOS",       "Analista macro IA (Claude)"),
        ("04", "⚠️", "AGENTE NEMESIS",      "CRO / Abogado del Diablo"),
        ("05", "🛡️", "MONITOR SISTEMA",    "AEGIS + logs en tiempo real"),
    ]

    st.markdown(
        f"<div style='background:{C['bg_secondary']};border:1px solid {C['border']};"
        f"border-radius:4px;padding:32px 40px;max-width:800px;margin:0 auto 32px auto;'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='color:{C['text_secondary']};font-family:Courier New,monospace;"
        f"font-size:0.75rem;letter-spacing:0.12em;text-transform:uppercase;"
        f"margin-bottom:18px;border-bottom:1px solid {C['border']};"
        f"padding-bottom:10px;'>// MÓDULOS DEL SISTEMA</div>",
        unsafe_allow_html=True,
    )
    for num, icon, name, desc in modules:
        st.markdown(
            f"<div style='padding:10px 0;border-bottom:1px solid {C['bg_main']};"
            f"display: flex; align-items: baseline;'>"
            f"<span style='color:{C['green']};font-family:Courier New,monospace;"
            f"font-size:0.90rem; font-weight: bold;'>{num}</span>"
            f"<span style='color:{C['text_primary']};font-family:Courier New,monospace;"
            f"font-size:0.95rem;margin-left:14px; font-weight: bold;'>{icon} {name}</span>"
            f"<span style='color:{C['text_secondary']};font-family:Courier New,monospace;"
            f"font-size:0.85rem;margin-left:16px;'>— {desc}</span></div>",
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        f"<div style='text-align:center;color:{C['text_secondary']};"
        f"font-family:Courier New,monospace;font-size:0.85rem;'>"
        f"Navega usando el menú lateral izquierdo ←</div>",
        unsafe_allow_html=True,
    )

def render_footer() -> None:
    """Renderiza el footer legal y técnico."""
    C = COLORS
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    st.markdown("<div class='prometheus-divider'></div>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='text-align:center;font-family:Courier New,monospace;"
        f"font-size:0.70rem;color:{C['text_muted']};padding:10px 0 24px 0;'>"
        f"⚡ PROMETHEUS {SYSTEM_VERSION} &nbsp;·&nbsp; "
        f"Datos: Yahoo Finance &nbsp;·&nbsp; IA: Claude API &nbsp;·&nbsp; "
        f"Platform: Streamlit Cloud &nbsp;·&nbsp; {now_utc} UTC<br>"
        f"<span style='font-size:0.62rem; opacity: 0.6;'>⚠️ Advertencia: Solo para fines educativos. "
        f"No se garantiza la exactitud de los datos ni se proporciona asesoramiento financiero.</span></div>",
        unsafe_allow_html=True,
    )

def main() -> None:
    """Función de arranque principal."""
    logger.info("PROMETHEUS Bootstrapping...")
    
    # 1. Inyectar estilos
    inject_global_css()
    
    # 2. Inicializar estado y modos
    init_session_state()
    detect_operation_modes()
    
    # 3. Renderizar UI
    render_sidebar()
    render_welcome()
    
    # 4. Verificaciones de seguridad
    if not st.session_state.get("mode_anthropic_api", False):
        st.warning(
            "⚠️ **Modo sin IA activo.** Configura `ANTHROPIC_API_KEY` en "
            "Streamlit Cloud (Settings → Secrets) para activar los Agentes CRONOS, NEMESIS y AEGIS. "
            "Los datos de mercado y analíticas técnicas operarán con normalidad."
        )
    
    # 5. Footer final
    render_footer()

if __name__ == "__main__":
    main()
