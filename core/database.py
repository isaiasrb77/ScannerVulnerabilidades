import sqlite3
from datetime import datetime

def inicializar_db():
    conn = sqlite3.connect('scanner_history.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS auditorias 
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, fecha TEXT, objetivo TEXT, categoria TEXT, hallazgos TEXT)''')
    conn.commit()
    conn.close()

def guardar_auditoria(objetivo, categoria, hallazgos):
    conn = sqlite3.connect('scanner_history.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO auditorias (fecha, objetivo, categoria, hallazgos) VALUES (?, ?, ?, ?)",
                   (datetime.now().strftime("%Y-%m-%d %H:%M"), objetivo, categoria, str(hallazgos)))
    conn.commit()
    conn.close()