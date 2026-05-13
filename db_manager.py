import sqlite3
import pandas as pd
import os
from datetime import datetime

# --- CONFIGURACIÓN DE BASE DE DATOS ---
DB_PATH = 'data/prometheus_core.db'

def init_db():
    """Inicializa la base de datos y crea las tablas necesarias."""
    if not os.path.exists('data'):
        os.makedirs('data')
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Tabla de Configuración de ETFs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS etf_config (
            ticker TEXT PRIMARY KEY,
            nombre TEXT,
            sector TEXT,
            fecha_adicion DATETIME
        )
    ''')
    
    # Tabla de Logs del Sistema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS system_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            nivel TEXT,
            mensaje TEXT
        )
    ''')
    
    # Insertar sectores por defecto si está vacía
    cursor.execute("SELECT COUNT(*) FROM etf_config")
    if cursor.fetchone()[0] == 0:
        default_etfs = [
            ('XLK', 'Technology Select Sector SPDR', 'Tecnología'),
            ('XLF', 'Financial Select Sector SPDR', 'Finanzas'),
            ('XLV', 'Health Care Select Sector SPDR', 'Salud'),
            ('XLE', 'Energy Select Sector SPDR', 'Energía'),
            ('XLI', 'Industrial Select Sector SPDR', 'Industria'),
            ('XLB', 'Materials Select Sector SPDR', 'Materiales'),
            ('XLY', 'Consumer Discretionary Select Sector SPDR', 'Consumo Discrecional'),
            ('XLP', 'Consumer Staples Select Sector SPDR', 'Consumo Básico'),
            ('XLU', 'Utilities Select Sector SPDR', 'Utilities'),
            ('XLRE', 'Real Estate Select Sector SPDR', 'Inmobiliario'),
            ('XLC', 'Communication Services Select Sector SPDR', 'Comunicaciones')
        ]
        cursor.executemany("INSERT INTO etf_config (ticker, nombre, sector, fecha_adicion) VALUES (?, ?, ?, ?)", 
                           [(t, n, s, datetime.now()) for t, n, s in default_etfs])
    
    conn.commit()
    conn.close()

def log_event(nivel, mensaje):
    """Guarda un evento en la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO system_logs (timestamp, nivel, mensaje) VALUES (?, ?, ?)", 
                   (datetime.now(), nivel, mensaje))
    conn.commit()
    conn.close()

def get_logs(limit=50):
    """Obtiene los últimos logs."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(f"SELECT * FROM system_logs ORDER BY timestamp DESC LIMIT {limit}", conn)
    conn.close()
    return df

def get_etf_config():
    """Obtiene la configuración de ETFs."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM etf_config", conn)
    conn.close()
    return df

def add_etf(ticker, nombre, sector):
    """Añade un nuevo ETF a la configuración."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO etf_config (ticker, nombre, sector, fecha_adicion) VALUES (?, ?, ?, ?)", 
                       (ticker.upper(), nombre, sector, datetime.now()))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
