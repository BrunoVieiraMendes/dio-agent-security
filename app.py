# ============================================================
# APP VULNERAVEL - EXEMPLO EDUCACIONAL
# ------------------------------------------------------------
# AVISO: Este codigo contem vulnerabilidades INTENCIONAIS
# para fins de aprendizado em ciberseguranca.
# NAO use este codigo em producao.
# ============================================================

import sqlite3

def criar_banco():
    """Cria um banco de dados SQLite com uma tabela de usuarios."""
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            role TEXT DEFAULT 'user'
        )
    """)
    # Insere usuarios de teste
    cursor.execute("INSERT OR IGNORE INTO usuarios (id, username, password, email, role) VALUES (1, 'admin', 'admin123', 'admin@empresa.com', 'admin')")
    cursor.execute("INSERT OR IGNORE INTO usuarios (id, username, password, email, role) VALUES (2, 'joao', 'senha456', 'joao@email.com', 'user')")
    cursor.execute("INSERT OR IGNORE INTO usuarios (id, username, password, email, role) VALUES (3, 'maria', 'maria789', 'maria@email.com', 'user')")
    conn.commit()
    conn.close()

def login(username, password):
    """
    VULNERAVEL: SQL Injection
    O username e a password sao concatenados diretamente na query SQL.
    Um atacante pode manipular a query para burlar a autenticacao.
    """
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # VULNERAVEL: concatenacao direta de entrada do usuario na query
    query = f"SELECT * FROM usuarios WHERE username = '{username}' AND password = '{password}'"
    print(f"[DEBUG] Query executada: {query}")

    cursor.execute(query)
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        print(f"Login bem-sucedido! Bem-vindo, {resultado[1]} (role: {resultado[4]})")
        return resultado
    else:
        print("Login falhou. Usuario ou senha incorretos.")
        return None

def buscar_usuario(username):
    """
    VULNERAVEL: SQL Injection na busca
    Mesmo problema: entrada do usuario concatenada diretamente.
    """
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # VULNERAVEL: concatenacao direta
    query = f"SELECT username, email, role FROM usuarios WHERE username = '{username}'"
    print(f"[DEBUG] Query executada: {query}")

    cursor.execute(query)
    resultados = cursor.fetchall()
    conn.close()

    for r in resultados:
        print(f"Usuario: {r[0]} | Email: {r[1]} | Role: {r[2]}")
    return resultados

if __name__ == "__main__":
    criar_banco()

    print("=" * 50)
    print("SISTEMA DE LOGIN (versao vulneravel)")
    print("=" * 50)

    print("\n--- Teste 1: Login normal ---")
    login("joao", "senha456")

    print("\n--- Teste 2: SQL Injection no login ---")
    # O atacante usa ' OR '1'='1 para burlar a autenticacao
    login("' OR '1'='1", "' OR '1'='1")

    print("\n--- Teste 3: SQL Injection para extrair dados ---")
    # O atacante usa UNION para extrair todos os usuarios
    buscar_usuario("' UNION SELECT username, password, role FROM usuarios --")

    print("\n--- Teste 4: Login com senha errada (falha normal) ---")
    login("joao", "senhaerrada")
