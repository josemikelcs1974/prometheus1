# --- TÍTULOS Y VERSIONES ---
SYSTEM_NAME = "PROMETHEUS"
SYSTEM_SUBTITLE = "ETF Rotation Intelligence System"
SYSTEM_VERSION = "2.0.0"

# --- PALETA DE COLORES (BLOOMBERG STYLE) ---
COLORS = {
    "bg_main": "#050508",
    "bg_secondary": "#010105",
    "green_neon": "#00ff88",
    "red_neon": "#ff3366",
    "orange_neon": "#ffaa00",
    "text_primary": "#e8e8f0",
    "text_secondary": "#8888aa",
    "border_dim": "#1a1a2e"
}

# --- UNIVERSO DE ETFS (13 SECTORES) ---
ETF_UNIVERSE = {
    "TECHNOLOGY": ["XLK", "QQQ", "VGT", "SOXX", "SMH", "IGV", "FTEC", "IYW", "CIBR", "WCLD"],
    "FINANCIALS": ["XLF", "VFH", "KRE", "KBE", "IAI", "IYF", "KBWB", "FNCL", "RYF", "FINU"],
    "HEALTHCARE": ["XLV", "VHT", "IBB", "XBI", "IHI", "IHF", "FHLC", "PJP", "BBH", "ARKG"],
    "ENERGY": ["XLE", "VDE", "OIH", "XOP", "FENY", "IYE", "MLP", "AMLP", "FCG", "RYE"],
    "INDUSTRIALS": ["XLI", "VIS", "IYJ", "FIDU", "PRN", "EXI", "RGI", "AIRR", "JETS", "XAR"],
    "MATERIALS": ["XLB", "VAW", "IYM", "FMAT", "MXI", "RTM", "REMX", "LIT", "PICK", "SLX"],
    "CONSUMER_DISC": ["XLY", "VCR", "FDIS", "IYC", "RTH", "RCD", "IBUY", "FXD", "CARZ", "ONLN"],
    "CONSUMER_STAPLES": ["XLP", "VDC", "FSTA", "IYK", "RHS", "KXI", "PBJ", "FTXG", "FXG", "PSCC"],
    "UTILITIES": ["XLU", "VPU", "FUTY", "IDU", "RYU", "JXI", "UTES", "FXU", "PSCU", "UTSL"],
    "REAL_ESTATE": ["XLRE", "VNQ", "IYR", "FREL", "RWR", "REM", "MORT", "FFR", "KBWY", "SRVR"],
    "COMM_SERVICES": ["XLC", "VOX", "FCOM", "IYZ", "SOCL", "RCM", "NXTG", "PSCT", "IXP", "PNQI"],
    "INTERNATIONAL": ["EFA", "EEM", "VEU", "IEFA", "ACWX", "EWJ", "FXI", "EWZ", "EWG", "MCHI"],
    "ALTERNATIVES": ["GLD", "IAU", "SLV", "PDBC", "DJP", "DBMF", "KMLM", "BNO", "UNG", "CPER"]
}

# --- INDICADORES MACRO ---
MACRO_TICKERS = {
    "S&P 500": "^GSPC",
    "NASDAQ 100": "QQQ",
    "Russell 2000": "^RUT",
    "VIX": "^VIX",
    "Bonos 10Y": "^TNX",
    "Dólar (DXY)": "UUP",
    "Oro": "GLD",
    "Bitcoin": "BTC-USD"
}

# --- PESOS DE MOMENTUM ---
MOMENTUM_WEIGHTS = {
    "W1M": 0.40,
    "W3M": 0.30,
    "W6M": 0.20,
    "W12M": 0.10
}
