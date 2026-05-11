/**
 * src/config.ts — FUENTE ÚNICA DE VERDAD (PROMETHEUS v2.0.0)
 * Sincronización exacta con los requerimientos técnicos de la arquitectura.
 */

export const SYSTEM_NAME = "PROMETHEUS";
export const SYSTEM_SUBTITLE = "ETF Rotation Intelligence System";
export const SYSTEM_VERSION = "2.0.0";

// --- CONFIGURACIÓN DE UI (BLOOMBERG STYLE) ---
export const COLORS = {
  bg_main: "#050508",
  bg_secondary: "#0d0d14",
  bg_sidebar: "#08080f",
  green: "#00ff88",
  red: "#ff3366",
  orange: "#ffaa00",
  blue: "#00aaff",
  text_primary: "#e8e8f0",
  text_secondary: "#8888aa",
  text_muted: "#444466",
  border: "#1a1a2e",
};

// --- ESTRUCTURA DEL UNIVERSO ETF ---
export const ETF_UNIVERSE = {
  TECHNOLOGY: ["XLK", "QQQ", "VGT", "SOXX", "SMH", "IGV", "FTEC", "IYW", "CIBR", "WCLD"],
  FINANCIALS: ["XLF", "VFH", "KRE", "KBE", "IAI", "IYF", "KBWB", "FNCL", "RYF", "FINU"],
  HEALTHCARE: ["XLV", "VHT", "IBB", "XBI", "IHI", "IHF", "FHLC", "PJP", "BBH", "ARKG"],
  ENERGY: ["XLE", "VDE", "OIH", "XOP", "FENY", "IYE", "MLP", "AMLP", "FCG", "RYE"],
  INDUSTRIALS: ["XLI", "VIS", "IYJ", "FIDU", "PRN", "EXI", "RGI", "AIRR", "JETS", "XAR"],
  MATERIALS: ["XLB", "VAW", "IYM", "FMAT", "MXI", "RTM", "REMX", "LIT", "PICK", "SLX"],
  CONSUMER_DISC: ["XLY", "VCR", "FDIS", "IYC", "RTH", "RCD", "IBUY", "FXD", "CARZ", "ONLN"],
  CONSUMER_STAPLES: ["XLP", "VDC", "FSTA", "IYK", "RHS", "KXI", "PBJ", "FTXG", "FXG", "PSCC"],
  UTILITIES: ["XLU", "VPU", "FUTY", "IDU", "RYU", "JXI", "UTES", "FXU", "PSCU", "UTSL"],
  REAL_ESTATE: ["XLRE", "VNQ", "IYR", "FREL", "RWR", "REM", "MORT", "FFR", "KBWY", "SRVR"],
  COMM_SERVICES: ["XLC", "VOX", "FCOM", "IYZ", "SOCL", "RCM", "NXTG", "PSCT", "IXP", "PNQI"],
  INTERNATIONAL: ["EFA", "EEM", "VEU", "IEFA", "ACWX", "EWJ", "FXI", "EWZ", "EWG", "MCHI"],
  ALTERNATIVES: ["GLD", "IAU", "SLV", "PDBC", "DJP", "DBMF", "KMLM", "BNO", "UNG", "CPER"],
};

// --- MACRO INDICATORS ---
export const MACRO_TICKERS = {
  "S&P 500": "^GSPC",
  "NASDAQ 100": "QQQ",
  "Russell 2000": "^RUT",
  "VIX": "^VIX",
  "Bonos 10Y": "^TNX",
  "Dólar (DXY)": "UUP",
  "Oro": "GLD",
  "Bitcoin": "BTC-USD",
};

// --- PESOS DE MOMENTUM (Lógica Institucional) ---
export const MOMENTUM_WEIGHTS = {
  W1M: 0.40, // 40% peso corto plazo
  W3M: 0.30, 
  W6M: 0.20,
  W12M: 0.10, // 10% peso largo plazo
};

// --- FASES DEL CICLO MACRO ---
export const CYCLE_PHASES = {
  EXPANSION: { 
    name: "Expansión", 
    desc: "Crecimiento acelerado. Bullish Tech/Disc.",
    top_sectors: ["TECHNOLOGY", "CONSUMER_DISC", "FINANCIALS"] 
  },
  PEAK: { 
    name: "Pico", 
    desc: "Máximo crecimiento, inflación subiendo. Reequilibrio a Energía.",
    top_sectors: ["ENERGY", "MATERIALS", "INDUSTRIALS"] 
  },
  CONTRACTION: { 
    name: "Contracción", 
    desc: "Ralentización. Bearish. Refugio en Defensive.",
    top_sectors: ["HEALTHCARE", "CONSUMER_STAPLES", "UTILITIES"] 
  },
  RECOVERY: { 
    name: "Recuperación", 
    desc: "Saliendo del pozo. Early bull Financials.",
    top_sectors: ["FINANCIALS", "REAL_ESTATE", "COMM_SERVICES"] 
  },
};

export const REFRESH_OPTIONS = {
  "OFF": 0,
  "30 seg": 30,
  "1 min": 60,
  "5 min": 300,
};

export const DEFAULT_REFRESH = "1 min";
