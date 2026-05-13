import yfinance as yf
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

@st.cache_data(ttl=60)
def fetch_macro_data(tickers):
    """
    Obtiene datos de yfinance para una lista de tickers con caché de 60 segundos.
    Implementa manejo de errores robusto.
    """
    data = {}
    status = True
    
    try:
        # Descargar datos del último día para obtener el cierre anterior y el actual
        df = yf.download(list(tickers.values()), period="2d", interval="1d", group_by='ticker', progress=False)
        
        for name, ticker in tickers.items():
            try:
                if ticker in df.columns.levels[0]:
                    ticker_data = df[ticker]
                    current_price = ticker_data['Close'].iloc[-1]
                    prev_price = ticker_data['Close'].iloc[0]
                    change = ((current_price - prev_price) / prev_price) * 100
                    data[name] = {
                        "ticker": ticker,
                        "price": current_price,
                        "change": change,
                        "status": "OK"
                    }
                else:
                    data[name] = {"ticker": ticker, "price": 0.0, "change": 0.0, "status": "ERROR"}
            except Exception:
                data[name] = {"ticker": ticker, "price": 0.0, "change": 0.0, "status": "ERROR"}
                
    except Exception as e:
        status = False
        print(f"Error global en fetch_macro_data: {e}")
        
    return data, status

def get_market_condition(vix, spx_change):
    """
    Determina la condición del mercado basándose en VIX y SPX.
    Refleja la mentalidad de rigor y paciencia.
    """
    if vix > 30:
        return "⚠️ ALTA VOLATILIDAD", "El mercado muestra signos de estrés extremo. Es momento de máxima disciplina y preservación de capital. No actúe por impulso."
    elif vix > 20:
        return "🟡 PRECAUCIÓN", "Volatilidad moderada detectada. El sistema recomienda una exposición prudente y reequilibrios estratégicos si es necesario."
    else:
        if spx_change > 0:
            return "🟢 ESTABILIDAD ASCENDENTE", "Condiciones favorables para la rotación de activos. Mantenga el rigor en la selección de sectores líderes."
        else:
            return "🔵 CONSOLIDACIÓN", "Mercado en fase de absorción. Paciencia y observación de niveles clave son fundamentales."

def format_currency(val):
    return f"${val:,.2f}"

def format_percent(val):
    return f"{val:+.2f}%"
