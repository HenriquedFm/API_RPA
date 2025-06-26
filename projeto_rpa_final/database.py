import sqlite3

def criar_banco():
    conn = sqlite3.connect('projeto_rpa.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS piadas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_processados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palavra TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def inserir_dado(texto):
    conn = sqlite3.connect('projeto_rpa.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO piadas (texto) VALUES (?)', (texto,))
    conn.commit()
    conn.close()
