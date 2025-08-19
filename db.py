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


def listar_clientes(termo=None):
    with get_conn() as conn:
        if termo:
            cur = conn.execute("""
                SELECT * FROM clientes
                WHERE name LIKE ? OR email LIKE ? OR phone LIKE ? OR address LIKE ?
                ORDER BY id DESC
            """, (f"%{termo}%", f"%{termo}%", f"%{termo}%", f"%{termo}%"))
        else:
            cur = conn.execute("SELECT * FROM clientes ORDER BY id DESC")
        return cur.fetchall()


def obter_cliente(id_):
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM clientes WHERE id = ?", (id_,))
        return cur.fetchone()

def atualizar_cliente(id, name, email, phone, address):
    with get_conn() as conn:
        conn.execute("""
            UPDATE clientes
            SET name = ?, email = ?, phone = ?, address = ?
            WHERE id = ?
        """, (name.strip(), email.strip(), phone.strip(), address.strip(), id))
