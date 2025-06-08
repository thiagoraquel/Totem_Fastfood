import sqlite3
import os

diretorio_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(diretorio_base, "database", "menu.db")

# Cria o DB, caso não tenha (SQLITE)
os.makedirs(os.path.dirname(db_path), exist_ok=True)

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Cria a Tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS itens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
""")

# Seed com os dados (não implementado painel de administrador, 
# então os dados serão por seed/inserção manual).
cursor.execute("SELECT COUNT(*) FROM itens")
if cursor.fetchone()[0] == 0:
    items = [
        ("X-Tudo", 14.99),
        ("Batata P", 4.99),
        ("Batata M", 5.99),
        ("Big Monstro", 16.99),
        ("Lata Refrigerante", 4.99)
    ]
    cursor.executemany("INSERT INTO itens (name, price) VALUES (?, ?)", items)

connection.commit()
connection.close()

print(f"Banco criado com sucesso em: {db_path}")
