"""
╔══════════════════════════════════════════════════════════════════════╗
║          PROMETHEUS — ETF Rotation Intelligence System               ║
║                    app.py — Punto de Entrada                         ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import logging
from datetime import datetime, timezone

import streamlit as st

from config import (
    SYSTEM_NAME, SYSTEM_SUBTITLE, SYSTEM_VERSION,
    COLORS, REFRESH_OPTIONS, DEFAULT_REFRESH,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("prometheus.app")
C = COLORS

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
            "⚠️ Uso educativo. No es asesoramiento financiero."
        ),
    },
)


def inject_global_css() -> None:
    css = f"""
    <style>
    html, body, [class*="css"] {{
        font-family: 'Courier New', monospace !important;
    }}
    .stApp {{ background-color: {C['bg_main']}; }}
    section[data-testid="stSidebar"] {{
        background-color: {C['bg_sidebar']};
        border-right: 1px solid {C['border']};
    }}
    header[data-testid="stHeader"] {{
        background-color: {C['bg_main']};
        border-bottom: 1px solid {C['border']};
    }}
    [data-testid="stMetric"] {{
        background-color: {C['bg_secondary']};
        border: 1px solid {C['border']};
        border-radius: 4px;
        padding: 12px 16px;
    }}
    [data-testid="stMetricLabel"] {{
        color: {C['text_secondary']} !important;
        font-size: 0.72rem !important;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }}
    [data-testid="stMetricValue"] {{
        color: {C['text_primary']} !important;
        font-size: 1.6rem !important;
        font-weight: bold;
    }}
    .stButton > button {{
        background-color: transparent;
        color: {C['green']};
        border: 1px solid {C['green']};
        border-radius: 3px;
        font-family: 'Courier New', monospace !important;
        font-size: 0.88rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        transition: all 0.2s ease;
        padding: 10px 20px;
    }}
    .stButton > button:hover {{
        background-color: {C['green']};
        color: {C['bg_main']};
        box-shadow: 0 0 12px {C['green']}66;
        transform: translateY(-1px);
    }}
    .stSelectbox > div > div {{
        background-color: {C['bg_secondary']};
        border: 1px solid {C['border']};
        border-radius: 3px;
        color: {C['text_primary']};
    }}
    details[data-testid="stExpander"] {{
        background-color: {C['bg_secondary']};
        border: 1px solid {C['border']};
        border-radius: 4px;
    }}
    .stTabs [data-baseweb="tab-list"] {{
        background-color: {C['bg_secondary']};
        border-bottom: 1px solid {C['border']};
    }}
    .stTabs [data-baseweb="tab"] {{
        background-color: transparent;
        color: {C['text_secondary']};
        font-family: 'Courier New', monospace !important;
        font-size: 0.82rem;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        padding: 8px 16px;
    }}
    .stTabs [aria-selected="true"] {{
        color: {C['green']} !important;
        border-bottom: 2px solid {C['green']} !important;
    }}
    ::-webkit-scrollbar {{ width: 5px; height: 5px; }}
    ::-webkit-scrollbar-track {{ background: {C['bg_main']}; }}
    ::-webkit-scrollbar-thumb {{ background: {C['border']}; border-radius: 2px; }}
    .stSpinner > div {{ border-top-color: {C['green']} !important; }}
    .prometheus-card {{
        background-color: {C['bg_secondary']};
        border: 1px solid {C['border']};
        border-radius: 4px;
        padding: 16px;
        margin-bottom: 8px;
    }}
    .prometheus-divider {{
        height: 1px;
        background: linear-gradient(to right, transparent, {C['green']}44, transparent);
        margin: 20px 0;
    }}
    .prometheus-log {{
        background-color: {C['bg_main']};
        border: 1px solid {C['border']};
        border-radius: 3px;
        padding: 12px;
        font-family: 'Courier New', monospace;
        font-size: 0.78rem;
        color: {C['green']};
        max-height: 300px;
        overflow-y: auto;
        line-height: 1.6;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def init_session_state() -> None:
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
    import os
    try:
        api_key = (
            st.secrets.get("api_keys", {}).get("ANTHROPIC_API_KEY", "")
            or os.getenv("ANTHROPIC_API_KEY", "")
        )
    except Exception:
        api_key = os.getenv("ANTHROPIC_API_KEY", "")
    st.session_state["mode_anthropic_api"] = bool(
        api_key and api_key.startswith("sk-ant")
    )


def render_sidebar() -> None:
    with st.sidebar:
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

        status = st.session_state.get("system_status", "INICIANDO")
        icons  = {"OK": ("🟢", C["green"]), "WARNING": ("🟡", C["orange"]),
                  "CRITICAL": ("🔴", C["red"]), "INICIANDO": ("⚪", C["text_muted"])}
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

        ai_ok = st.session_state.get("mode_anthropic_api", False)
        st.markdown(
            f"<div style='font-family:Courier New,monospace;font-size:0.75rem;"
            f"margin-bottom:16px;'>"
            f"{'<span style=color:' + C['green'] + ';>✓ Agentes IA activos</span>' if ai_ok else '<span style=color:' + C['orange'] + ';>⚠ Sin API key IA</span>'}"
            f"</div>",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"<div style='color:{C['text_secondary']};font-size:0.72rem;"
            f"text-transform:uppercase;margin-bottom:4px;'>AUTO-REFRESH</div>",
            unsafe_allow_html=True,
        )
        selected = st.selectbox(
            "auto-refresh",
            options=list(REFRESH_OPTIONS.keys()),
            index=list(REFRESH_OPTIONS.keys()).index(DEFAULT_REFRESH),
            label_visibility="collapsed",
            key="sb_refresh",
        )
        st.session_state["auto_refresh_interval"] = selected

        last = st.session_state.get("last_data_refresh")
        ts   = (f"hace {int((datetime.now(timezone.utc)-last).total_seconds())}s"
                if last else "Sin datos")
        st.markdown(
            f"<div style='color:{C['text_muted']};font-family:Courier New,monospace;"
            f"font-size:0.70rem;margin:8px 0 20px 0;'>Última actualización:<br>"
            f"<span style='color:{C['text_secondary']};'>{ts}</span></div>",
            unsafe_allow_html=True,
        )

        if st.button("⚡ ACTUALIZACIÓN GLOBAL", use_container_width=True,
                     key="btn_global"):
            for k in ["macro_snapshot", "etf_rankings", "cycle_phase"]:
                st.session_state[k] = None
            st.cache_data.clear()
            st.rerun()

        start  = st.session_state.get("app_start_time", datetime.now(timezone.utc))
        uptime = datetime.now(timezone.utc) - start
        h = int(uptime.total_seconds() // 3600)
        m = int((uptime.total_seconds() % 3600) // 60)
        st.markdown(
            f"<hr style='border-color:{C['border']};margin:16px 0;'>"
            f"<div style='color:{C['text_muted']};font-family:Courier New,monospace;"
            f"font-size:0.68rem;text-align:center;'>"
            f"v{SYSTEM_VERSION} · Uptime: {h:02d}h {m:02d}m<br>"
            f"Datos: Yahoo Finance · IA: Claude API<br>"
            f"<span style='font-size:0.62rem;'>⚠ Solo fines educativos</span></div>",
            unsafe_allow_html=True,
        )


def render_welcome() -> None:
    st.markdown(
        f"<div style='text-align:center;padding:32px 0 20px 0;'>"
        f"<div style='color:{C['green']};font-family:Courier New,monospace;"
        f"font-size:2.4rem;font-weight:bold;letter-spacing:0.1em;'>"
        f"⚡ PROMETHEUS</div>"
        f"<div style='color:{C['text_secondary']};font-family:Courier New,monospace;"
        f"font-size:0.80rem;letter-spacing:0.25em;text-transform:uppercase;"
        f"margin-top:6px;margin-bottom:28px;'>"
        f"ETF ROTATION INTELLIGENCE SYSTEM · v{SYSTEM_VERSION}</div></div>",
        unsafe_allow_html=True,
    )

    modules = [
        ("01", "📊", "MACRO DASHBOARD",    "25 activos macro en tiempo real"),
        ("02", "🔄", "ROTACIÓN SECTORIAL", "Ranking 13 sectores + top-5 ETFs"),
        ("03", "⚡", "AGENTE CRONOS",       "Analista macro IA (Claude)"),
        ("04", "⚠️", "AGENTE NEMESIS",      "CRO / Abogado del Diablo"),
        ("05", "🛡️", "MONITOR SISTEMA",    "AEGIS + logs en tiempo real"),
    ]

    st.markdown(
        f"<div style='background:{C['bg_secondary']};border:1px solid {C['border']};"
        f"border-radius:4px;padding:24px 28px;max-width:680px;margin:0 auto 24px auto;'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<div style='color:{C['text_secondary']};font-family:Courier New,monospace;"
        f"font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;"
        f"margin-bottom:14px;border-bottom:1px solid {C['border']};"
        f"padding-bottom:8px;'>// MÓDULOS DISPONIBLES</div>",
        unsafe_allow_html=True,
    )
    for num, icon, name, desc in modules:
        st.markdown(
            f"<div style='padding:7px 0;border-bottom:1px solid {C['bg_main']};'>"
            f"<span style='color:{C['green']};font-family:Courier New,monospace;"
            f"font-size:0.80rem;'>{num}</span>"
            f"<span style='color:{C['text_primary']};font-family:Courier New,monospace;"
            f"font-size:0.82rem;margin-left:10px;'>{icon} {name}</span>"
            f"<span style='color:{C['text_secondary']};font-family:Courier New,monospace;"
            f"font-size:0.75rem;margin-left:12px;'>— {desc}</span></div>",
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        f"<div style='text-align:center;color:{C['text_secondary']};"
        f"font-family:Courier New,monospace;font-size:0.78rem;'>"
        f"Navega usando el menú lateral izquierdo ←</div>",
        unsafe_allow_html=True,
    )


def render_footer() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    st.markdown(
        f"<div class='prometheus-divider'></div>"
        f"<div style='text-align:center;font-family:Courier New,monospace;"
        f"font-size:0.68rem;color:{C['text_muted']};padding:8px 0 16px 0;'>"
        f"⚡ PROMETHEUS {SYSTEM_VERSION} &nbsp;·&nbsp; "
        f"Datos: Yahoo Finance &nbsp;·&nbsp; IA: Claude API &nbsp;·&nbsp; {now}<br>"
        f"<span style='font-size:0.60rem;'>⚠️ Solo fines educativos. "
        f"No constituye asesoramiento financiero.</span></div>",
        unsafe_allow_html=True,
    )


def main() -> None:
    logger.info("PROMETHEUS iniciando")
    inject_global_css()
    init_session_state()
    detect_operation_modes()
    render_sidebar()
    render_welcome()
    if not st.session_state.get("mode_anthropic_api", False):
        st.warning(
            "⚠️ **Modo sin IA activo.** Configure `ANTHROPIC_API_KEY` en "
            "Streamlit Secrets para activar los Agentes CRONOS, NEMESIS y AEGIS. "
            "Los datos de mercado funcionan normalmente."
        )
    render_footer()


main()
