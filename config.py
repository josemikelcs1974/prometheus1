"""
╔══════════════════════════════════════════════════════════════════════╗
║          PROMETHEUS — ETF Rotation Intelligence System               ║
║                    config.py — Cerebro Global                        ║
║                                                                      ║
║  FUENTE ÚNICA DE VERDAD para todos los parámetros del sistema.       ║
║  Nunca hardcodear valores en otros módulos.                          ║
╚══════════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 1 — IDENTIDAD DEL SISTEMA
# ══════════════════════════════════════════════════════════════════════

SYSTEM_NAME     = "PROMETHEUS"
SYSTEM_SUBTITLE = "ETF Rotation Intelligence System"
SYSTEM_VERSION  = "2.0.0"
PYTHON_TARGET   = "3.12"

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 2 — UNIVERSO DE ETFs POR SECTOR
# ══════════════════════════════════════════════════════════════════════

ETF_UNIVERSE: dict[str, list[str]] = {
    "TECHNOLOGY": [
        "XLK", "QQQ", "VGT", "SOXX", "SMH",
        "IGV", "FTEC", "IYW", "CIBR", "WCLD",
    ],
    "FINANCIALS": [
        "XLF", "VFH", "KRE", "KBE", "IAI",
        "IYF", "KBWB", "FNCL", "RYF", "FINU",
    ],
    "HEALTHCARE": [
        "XLV", "VHT", "IBB", "XBI", "IHI",
        "IHF", "FHLC", "PJP", "BBH", "ARKG",
    ],
    "ENERGY": [
        "XLE", "VDE", "OIH", "XOP", "FENY",
        "IYE", "MLP", "AMLP", "FCG", "RYE",
    ],
    "INDUSTRIALS": [
        "XLI", "VIS", "IYJ", "FIDU", "PRN",
        "EXI", "RGI", "AIRR", "JETS", "XAR",
    ],
    "MATERIALS": [
        "XLB", "VAW", "IYM", "FMAT", "MXI",
        "RTM", "REMX", "LIT", "PICK", "SLX",
    ],
    "CONSUMER_DISC": [
        "XLY", "VCR", "FDIS", "IYC", "RTH",
        "RCD", "IBUY", "FXD", "CARZ", "ONLN",
    ],
    "CONSUMER_STAPLES": [
        "XLP", "VDC", "FSTA", "IYK", "RHS",
        "KXI", "PBJ", "FTXG", "FXG", "PSCC",
    ],
    "UTILITIES": [
        "XLU", "VPU", "FUTY", "IDU", "RYU",
        "JXI", "UTES", "FXU", "PSCU", "UTSL",
    ],
    "REAL_ESTATE": [
        "XLRE", "VNQ", "IYR", "FREL", "RWR",
        "REM", "MORT", "FFR", "KBWY", "SRVR",
    ],
    "COMM_SERVICES": [
        "XLC", "VOX", "FCOM", "IYZ", "SOCL",
        "RCM", "NXTG", "PSCT", "IXP", "PNQI",
    ],
    "INTERNATIONAL": [
        "EFA", "EEM", "VEU", "IEFA", "ACWX",
        "EWJ", "FXI", "EWZ", "EWG", "MCHI",
    ],
    "ALTERNATIVES": [
        "GLD", "IAU", "SLV", "PDBC", "DJP",
        "DBMF", "KMLM", "BNO", "UNG", "CPER",
    ],
}

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 3 — TICKERS MACRO
# ══════════════════════════════════════════════════════════════════════

MACRO_TICKERS: dict[str, str] = {
    "S&P 500":       "^GSPC",
    "NASDAQ 100":    "QQQ",
    "NASDAQ Comp":   "^IXIC",
    "Dow Jones":     "^DJI",
    "Russell 2000":  "^RUT",
    "VIX":           "^VIX",
    "MOVE Index":    "^MOVE",
    "Bonos 10Y":     "^TNX",
    "Bonos 30Y":     "^TYX",
    "TLT ETF":       "TLT",
    "HYG (HY)":      "HYG",
    "LQD (IG)":      "LQD",
    "Dólar (DXY)":   "UUP",
    "EUR/USD":       "EURUSD=X",
    "Oro":           "GLD",
    "Plata":         "SLV",
    "Petróleo Brent":"BZ=F",
    "Petróleo WTI":  "CL=F",
    "Gas Natural":   "NG=F",
    "Cobre":         "CPER",
    "Bitcoin":       "BTC-USD",
    "Ethereum":      "ETH-USD",
    "SPY":           "SPY",
    "Emerging Mkt":  "EEM",
}

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 4 — BENCHMARKS PARA CORRELACIONES
# ══════════════════════════════════════════════════════════════════════

CORRELATION_BENCHMARKS: dict[str, str] = {
    "VIX":          "^VIX",
    "Bonos 10Y":    "^TNX",
    "S&P 500":      "^GSPC",
    "Dólar":        "UUP",
    "Oro":          "GLD",
    "Brent":        "BZ=F",
    "HY Bonds":     "HYG",
    "Russell 2000": "^RUT",
}

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 5 — MODELO DE CICLO ECONÓMICO (8 FASES)
# ══════════════════════════════════════════════════════════════════════

CYCLE_PHASES: dict[int, dict] = {
    1: {
        "name":          "RECUPERACIÓN TEMPRANA",
        "color":         "#00ff88",
        "icon":          "🌱",
        "top_sectors":   ["TECHNOLOGY", "CONSUMER_DISC", "FINANCIALS"],
        "neutral":       ["INDUSTRIALS", "COMM_SERVICES", "REAL_ESTATE"],
        "avoid_sectors": ["UTILITIES", "CONSUMER_STAPLES", "ENERGY"],
        "description":   "GDP toca fondo y rebota. Crédito expandiéndose. Fed acomodaticia.",
        "macro_signals": ["Fed recortando", "PMI subiendo desde < 50", "Spreads HY comprimiéndose"],
    },
    2: {
        "name":          "EXPANSIÓN PLENA",
        "color":         "#00cc66",
        "icon":          "📈",
        "top_sectors":   ["INDUSTRIALS", "MATERIALS", "TECHNOLOGY"],
        "neutral":       ["FINANCIALS", "ENERGY", "CONSUMER_DISC"],
        "avoid_sectors": ["UTILITIES", "REAL_ESTATE", "CONSUMER_STAPLES"],
        "description":   "Crecimiento robusto. Beneficios acelerando. Empleo en máximos.",
        "macro_signals": ["PMI > 55", "Cobre al alza", "Spreads en mínimos"],
    },
    3: {
        "name":          "EXPANSIÓN TARDÍA",
        "color":         "#88cc00",
        "icon":          "⚡",
        "top_sectors":   ["ENERGY", "MATERIALS", "FINANCIALS"],
        "neutral":       ["INDUSTRIALS", "HEALTHCARE", "CONSUMER_STAPLES"],
        "avoid_sectors": ["TECHNOLOGY", "CONSUMER_DISC", "REAL_ESTATE"],
        "description":   "Fed subiendo tipos. Inflación elevada. Commodities fuertes.",
        "macro_signals": ["Fed hawkish", "Inflación persistente", "Curva aplanándose"],
    },
    4: {
        "name":          "PICO DE CICLO",
        "color":         "#ffaa00",
        "icon":          "⚠️",
        "top_sectors":   ["ENERGY", "CONSUMER_STAPLES", "HEALTHCARE"],
        "neutral":       ["UTILITIES", "MATERIALS", "COMM_SERVICES"],
        "avoid_sectors": ["REAL_ESTATE", "CONSUMER_DISC", "TECHNOLOGY"],
        "description":   "Curva invertida. Spreads ampliándose. Amplitud reducida.",
        "macro_signals": ["Curva invertida", "Spreads HY ampliándose", "PMI cayendo"],
    },
    5: {
        "name":          "DESACELERACIÓN",
        "color":         "#ff8800",
        "icon":          "📉",
        "top_sectors":   ["HEALTHCARE", "CONSUMER_STAPLES", "UTILITIES"],
        "neutral":       ["COMM_SERVICES", "REAL_ESTATE", "ALTERNATIVES"],
        "avoid_sectors": ["FINANCIALS", "INDUSTRIALS", "MATERIALS"],
        "description":   "GDP desacelerando. PMI < 50. Volatilidad subiendo.",
        "macro_signals": ["PMI < 50", "Desempleo subiendo", "VIX > 20"],
    },
    6: {
        "name":          "RECESIÓN TEMPRANA",
        "color":         "#ff4444",
        "icon":          "🔴",
        "top_sectors":   ["CONSUMER_STAPLES", "UTILITIES", "ALTERNATIVES"],
        "neutral":       ["HEALTHCARE", "COMM_SERVICES"],
        "avoid_sectors": ["ENERGY", "MATERIALS", "FINANCIALS", "INDUSTRIALS"],
        "description":   "GDP negativo. Crédito contrayéndose. Fed cambiando a dovish.",
        "macro_signals": ["GDP < 0", "Fed recortando urgente", "Spreads > 700 bps"],
    },
    7: {
        "name":          "RECESIÓN PROFUNDA",
        "color":         "#cc0000",
        "icon":          "💀",
        "top_sectors":   ["ALTERNATIVES", "UTILITIES", "CONSUMER_STAPLES"],
        "neutral":       ["HEALTHCARE"],
        "avoid_sectors": ["TECHNOLOGY", "FINANCIALS", "ENERGY", 
                          "INDUSTRIALS", "MATERIALS", "CONSUMER_DISC"],
        "description":   "Capitulación. Mínimos de mercado. QE y política fiscal máxima.",
        "macro_signals": ["VIX > 40", "Fed en 0%", "GDP cayendo"],
    },
    8: {
        "name":          "INFLEXIÓN / TRANSICIÓN",
        "color":         "#9900ff",
        "icon":          "🔄",
        "top_sectors":   ["TECHNOLOGY", "FINANCIALS", "CONSUMER_DISC"],
        "neutral":       ["INDUSTRIALS", "MATERIALS", "HEALTHCARE"],
        "avoid_sectors": ["UTILITIES", "CONSUMER_STAPLES"],
        "description":   "Señales mixtas. Primeras señales de recuperación sin confirmación.",
        "macro_signals": ["PMI rebotando", "VIX bajando", "Liderazgo rotando"],
    },
}

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 6 — PARÁMETROS DEL MODELO
# ══════════════════════════════════════════════════════════════════════

MOMENTUM_WEIGHTS: dict[str, float] = {
    "1m":  0.20,
    "3m":  0.35,
    "6m":  0.30,
    "12m": 0.15,
}

FACTOR_WEIGHTS: dict[str, float] = {
    "momentum":     0.30,
    "relative_str": 0.25,
    "cycle_align":  0.25,
    "inst_volume":  0.20,
}

ROTATION_COOLDOWN_DAYS:   int   = 21
CONFIRMATION_SIGNALS_REQ: int   = 4
TRIPLE_CONFIRM_PERIODS:   int   = 3
ROTATION_MIN_SCORE_DIFF:  float = 8.0

VIX_NEUTRAL_MAX:  float = 15.0
VIX_RISK_OFF:     float = 25.0
VIX_EXTREME:      float = 35.0
VIX_CAPITULATION: float = 40.0

RSI_OVERBOUGHT:       float = 75.0
RSI_OVERSOLD:         float = 28.0
BELOW_SMA200_PENALTY: float = 0.5
MIN_RS_SCORE:         float = 0.0
MIN_VOLUME_RATIO:     float = 0.5

CORRELATION_WINDOW: int = 30

CORR_HIGH_VIX_ALERT:  float = 0.65
CORR_LOW_BONDS_ALERT: float = -0.70
CORR_HIGH_SPY_INFO:   float = 0.95
CORR_HIGH_DXY_ALERT:  float = -0.60

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 7 — CACHÉ (segundos)
# ══════════════════════════════════════════════════════════════════════

CACHE_TTL_QUOTES:     int = 60
CACHE_TTL_HISTORICAL: int = 3600
CACHE_TTL_MACRO:      int = 60
CACHE_TTL_AGENTS:     int = 300
CACHE_TTL_RANKINGS:   int = 120
CACHE_TTL_CORR:       int = 3600

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 8 — AGENTES IA
# ══════════════════════════════════════════════════════════════════════

AGENT_MODEL:      str = "claude-sonnet-4-5"
AGENT_MAX_TOKENS: int = 2048
AGENT_TIMEOUT:    int = 45
AGENT_MAX_RETRIES:int = 2

CRONOS_TEMPERATURE:  float = 0.3
NEMESIS_TEMPERATURE: float = 0.7
AEGIS_TEMPERATURE:   float = 0.2

MAX_ANALYSIS_HISTORY: int = 10

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 9 — PARÁMETROS DE DESCARGA
# ══════════════════════════════════════════════════════════════════════

CORRELATION_DOWNLOAD_PERIOD: str      = "90d"
TECHNICAL_PERIOD:            str      = "1y"
DEFAULT_INTERVAL:            str      = "1d"
BULK_DOWNLOAD_TIMEOUT:       int      = 30
BULK_MAX_WORKERS:            int      = 8
MAX_RETRIES:                 int      = 3
RETRY_BACKOFF:               list[int]= [1, 2, 4]

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 10 — TEMA VISUAL BLOOMBERG
# ══════════════════════════════════════════════════════════════════════

COLORS: dict[str, str] = {
    "bg_main":        "#050508",
    "bg_secondary":   "#0d0d14",
    "bg_tertiary":    "#12121c",
    "bg_sidebar":     "#08080f",
    "green":          "#00ff88",
    "red":            "#ff3366",
    "orange":         "#ffaa00",
    "blue":           "#00aaff",
    "purple":         "#9900ff",
    "text_primary":   "#e8e8f0",
    "text_secondary": "#8888aa",
    "text_muted":     "#444466",
    "border":         "#1a1a2e",
    "grid":           "#111120",
    "risk_on":        "#00ff88",
    "risk_off":       "#ff3366",
    "neutral":        "#ffaa00",
    "panic":          "#ff0044",
    "phase_1": "#00ff88", "phase_2": "#00cc66",
    "phase_3": "#88cc00", "phase_4": "#ffaa00",
    "phase_5": "#ff8800", "phase_6": "#ff4444",
    "phase_7": "#cc0000", "phase_8": "#9900ff",
}

FONT_PRIMARY: str = "'Courier New', 'Lucida Console', monospace"

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 11 — REGLAS MACRO
# ══════════════════════════════════════════════════════════════════════

MACRO_RULES: dict[str, dict] = {
    "VIX": {
        "risk_on_max":    15.0,
        "neutral_max":    25.0,
        "risk_off_max":   35.0,
        "interpretation": "< 15 Calma | 15-25 Cautela | > 25 Miedo | > 35 Pánico",
    },
    "YIELD_CURVE": {
        "normal_min":    50,
        "flat_min":       0,
        "inverted_max": -50,
        "interpretation": "> 50bps Normal | 0-50bps Plana | < 0 Invertida",
    },
    "DXY_TREND": {
        "risk_on_max":  -0.5,
        "neutral_min":  -0.5,
        "neutral_max":   0.5,
        "risk_off_min":  0.5,
        "interpretation": "Dólar débil = RISK-ON | Dólar fuerte = RISK-OFF",
    },
    "HYG_LQD_RATIO": {
        "trend_risk_on":  "ascending",
        "trend_risk_off": "descending",
        "interpretation": "HYG/LQD subiendo = spreads comprimiendo = RISK-ON",
    },
}

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 12 — AUTO-REFRESH
# ══════════════════════════════════════════════════════════════════════

REFRESH_OPTIONS: dict[str, int] = {
    "OFF":    0,
    "30 seg": 30,
    "1 min":  60,
    "5 min":  300,
}
DEFAULT_REFRESH: str = "1 min"

# ══════════════════════════════════════════════════════════════════════
# SECCIÓN 13 — VALIDACIÓN DE INTEGRIDAD
# ══════════════════════════════════════════════════════════════════════

def _validate_config() -> None:
    """Valida consistencia interna al importar."""
    assert abs(sum(MOMENTUM_WEIGHTS.values()) - 1.0) < 1e-9, \
        "MOMENTUM_WEIGHTS deben sumar 1.0"
    assert abs(sum(FACTOR_WEIGHTS.values()) - 1.0) < 1e-9, \
        "FACTOR_WEIGHTS deben sumar 1.0"
    assert set(CYCLE_PHASES.keys()) == {1, 2, 3, 4, 5, 6, 7, 8}, \
        "CYCLE_PHASES debe tener fases 1 a 8"
    valid_sectors = set(ETF_UNIVERSE.keys())
    for phase_num, phase_data in CYCLE_PHASES.items():
        for sector in phase_data["top_sectors"] + phase_data["avoid_sectors"]:
            assert sector in valid_sectors, \
                f"Fase {phase_num}: sector '{sector}' no existe en ETF_UNIVERSE"


_validate_config()
