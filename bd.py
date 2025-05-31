import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("loja.db")
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
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
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                total REAL NOT NULL,
                data_venda TEXT DEFAULT (datetime('now', 'localtime')),
                FOREIGN KEY (produto_id) REFERENCES produtos(id)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL, 
                senha TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def registrar_venda(self, produto_id, quantidade, total):
        try:
            produto = self.buscar_produto(produto_id)
            if not produto:
                print(f"Erro: Produto ID {produto_id} não encontrado.")
                return False
            if quantidade > produto[3]:  # Índice 3 = estoque
                print("Erro: Quantidade maior que o estoque disponível.")
                return False

            self.cursor.execute("""
                INSERT INTO vendas (produto_id, quantidade, total)
                VALUES (?, ?, ?)
            """, (produto_id, quantidade, total))

            self.cursor.execute("""
                UPDATE produtos
                SET estoque = estoque - ?
                WHERE id = ?
            """, (quantidade, produto_id))

            self.conn.commit()
            print("Venda registrada com sucesso!")
            return True
        except sqlite3.Error as e:
            print(f"Erro ao registrar venda: {e}")
            return False

    def listar_produtos(self):
        self.cursor.execute("SELECT id, nome, preco, estoque FROM produtos")
        return self.cursor.fetchall()

    def buscar_produto(self, produto_id):
        self.cursor.execute("SELECT id, nome, categoria, preco, estoque, fornecedor FROM produtos WHERE id = ?", (produto_id,))
        return self.cursor.fetchone()
    
    def atualiza_produto(self, produto_id, nome, categoria, preco, estoque, fornecedor):
        self.cursor.execute("""
            UPDATE produtos 
            SET nome = ?, categoria = ?, preco = ?, estoque = ?, fornecedor = ?
            WHERE id = ?
        """, (nome, categoria, preco, estoque, fornecedor, produto_id))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()
