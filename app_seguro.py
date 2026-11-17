# ============================================================
# APP SEGURO - VERSAO CORRIGIDA
# ------------------------------------------------------------
# Este codigo corrige as vulnerabilidades de SQL Injection
# presentes em app.py, usando consultas parametrizadas.
# ============================================================

import sqlite3
import hashlib
import secrets

def criar_banco():
    """Cria um banco de dados SQLite com uma tabela de usuarios."""
    conn = sqlite3.connect("usuarios_seguro.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            email TEXT,
            role TEXT DEFAULT 'user'
        )
    """)

    # Insere usuarios de teste com senhas hasheadas
    usuarios_teste = [
        ("admin", "admin123", "admin@empresa.com", "admin"),
        ("joao", "senha456", "joao@email.com", "user"),
        ("maria", "maria789", "maria@email.com", "user"),
    ]

    for username, password, email, role in usuarios_teste:
        salt = secrets.token_hex(16)
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        try:
            cursor.execute(
                "INSERT INTO usuarios (username, password_hash, salt, email, role) VALUES (?, ?, ?, ?, ?)",
                (username, password_hash, salt, email, role)
            )
        except sqlite3.IntegrityError:
            pass  # Usuario ja existe

    conn.commit()
    conn.close()

def login(username, password):
    """
    SEGURO: Usa consulta parametrizada (?) em vez de concatenacao.
    O SQLite trata os parametros como dados, nao como parte do SQL.
    Senhas sao verificadas via hash + salt.
    """
    conn = sqlite3.connect("usuarios_seguro.db")
    cursor = conn.cursor()

    # SEGURO: consulta parametrizada — o ? impede SQL Injection
    cursor.execute(
        "SELECT id, username, password_hash, salt, role FROM usuarios WHERE username = ?",
        (username,)
    )
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        _, db_username, db_hash, db_salt, db_role = resultado
        # Verifica a senha comparando hashes
        input_hash = hashlib.sha256((password + db_salt).encode()).hexdigest()
        if input_hash == db_hash:
            print(f"Login bem-sucedido! Bem-vindo, {db_username} (role: {db_role})")
            return resultado
        else:
            print("Login falhou. Usuario ou senha incorretos.")
            return None
    else:
        print("Login falhou. Usuario ou senha incorretos.")
        return None

def buscar_usuario(username):
    """
    SEGURO: Consulta parametrizada na busca tambem.
    """
    conn = sqlite3.connect("usuarios_seguro.db")
    cursor = conn.cursor()

    # SEGURO: consulta parametrizada
    cursor.execute(
        "SELECT username, email, role FROM usuarios WHERE username = ?",
        (username,)
    )
    resultados = cursor.fetchall()
    conn.close()

    if resultados:
        for r in resultados:
            print(f"Usuario: {r[0]} | Email: {r[1]} | Role: {r[2]}")
    else:
        print("Nenhum usuario encontrado.")
    return resultados

if __name__ == "__main__":
    criar_banco()

    print("=" * 50)
    print("SISTEMA DE LOGIN (versao SEGURA)")
    print("=" * 50)

    print("\n--- Teste 1: Login normal ---")
    login("joao", "senha456")

    print("\n--- Teste 2: Tentativa de SQL Injection (bloqueada) ---")
    login("' OR '1'='1", "' OR '1'='1")

    print("\n--- Teste 3: Tentativa de Injection na busca (bloqueada) ---")
    buscar_usuario("' UNION SELECT username, password_hash, role FROM usuarios --")

    print("\n--- Teste 4: Login com senha errada ---")
    login("joao", "senhaerrada")
