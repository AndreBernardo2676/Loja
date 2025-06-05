import tkinter as tk
from bd import Database

class RelatorioGUI(tk.Frame):
    def __init__(self, parent, database):
        super().__init__(parent)
        self.database = database

        tk.Button(self, text="Gerar Relatório Geral", command=self.gerar_relatorio).pack()
        tk.Button(self, text="Relatório de Cadastros", command=self.gerar_relatorio_cadastros).pack()
        tk.Button(self, text="Relatório de Vendas", command=self.gerar_relatorio_vendas).pack()
        
        self.texto_relatorio = tk.Text(self)
        self.texto_relatorio.pack(expand=True, fill="both")

    def gerar_relatorio(self):
        self.texto_relatorio.delete(1.0, tk.END)

        self.texto_relatorio.insert(tk.END, "=== PRODUTOS CADASTRADOS ===\n")
        self.database.cursor.execute("SELECT id, nome, categoria, preco, estoque, fornecedor FROM produtos WHERE ativo = 1")
        produtos = self.database.cursor.fetchall()
        for p in produtos:
            self.texto_relatorio.insert(tk.END, f"ID: {p[0]} | Nome: {p[1]} | Categoria: {p[2]} | Preço: R${p[3]:.2f} | Fornecedor: {p[5]} | Estoque: {p[4]}\n")

        self.texto_relatorio.insert(tk.END, "\n=== VENDAS REALIZADAS ===\n")
        self.database.cursor.execute("""
            SELECT v.id, p.nome, v.quantidade, v.total, v.data_venda, p.fornecedor
            FROM vendas v
            JOIN produtos p ON v.produto_id = p.id
            ORDER BY v.data_venda DESC
        """)
        vendas = self.database.cursor.fetchall()
        for v in vendas:
            self.texto_relatorio.insert(
                tk.END,
                f"ID: {v[0]} | Produto: {v[1]} | Qtde: {v[2]} | Total: R${v[3]:.2f} | Fornecedor: {v[5]} |Data: {v[4]}\n"
            )
    def gerar_relatorio_cadastros(self):
            self.texto_relatorio.delete(1.0, tk.END)
            self.texto_relatorio.insert(tk.END, "=== PRODUTOS CADASTRADOS ===\n")
            
            self.database.cursor.execute("""
                SELECT id, nome, categoria, preco, estoque, fornecedor 
                FROM produtos 
                WHERE ativo = 1
            """)
            produtos = self.database.cursor.fetchall()
            for p in produtos:
                self.texto_relatorio.insert(tk.END, f"ID: {p[0]} | Nome: {p[1]} | Categoria: {p[2]} | Preço: R${p[3]:.2f} | Fornecedor: {p[5]} | Estoque: {p[4]}\n")
    
    def gerar_relatorio_vendas(self):
        self.texto_relatorio.delete(1.0, tk.END)
        self.texto_relatorio.insert(tk.END, "=== VENDAS REALIZADAS ===\n")

        self.database.cursor.execute("""
            SELECT v.id, p.nome, v.quantidade, v.total, v.data_venda, p.fornecedor
            FROM vendas v
            JOIN produtos p ON v.produto_id = p.id
            ORDER BY v.data_venda DESC
        """)
        vendas = self.database.cursor.fetchall()
        for v in vendas:
            self.texto_relatorio.insert(
                tk.END,
                f"ID: {v[0]} | Produto: {v[1]} | Qtde: {v[2]} | Total: R${v[3]:.2f} | Fornecedor: {v[5]} | Data: {v[4]}\n"
            )