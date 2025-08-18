import sqlite3 as sql

DB_PATH = "infos.db"

def get_conn():
    conn = sql.connect(DB_PATH)
    conn.row_factory = sql.Row # Acessar linhas por nome das colunas
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT,
            address TEXT
        )""")

def inserir_cliente(name, email, phone, address):
        with get_conn() as conn:
             conn.execute(
                  "INSERT INTO clientes(name, email, phone, address) VALUES (?,?,?,?)",
                  (name.strip(), email.strip(), phone.strip(), address.strip())
            )





