import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("loja.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL,
                estoque INTEGER NOT NULL,
                fornecedor TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()
