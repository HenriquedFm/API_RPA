import re
import sqlite3

def processar_texto(texto):
    palavras = re.findall(r'\\b\\w*ch\\w*\\b', texto, re.IGNORECASE)
    conn = sqlite3.connect('projeto_rpa.db')
    cursor = conn.cursor()
    for palavra in palavras:
        cursor.execute('INSERT INTO dados_processados (palavra) VALUES (?)', (palavra,))
    conn.commit()
    conn.close()
    return palavras
