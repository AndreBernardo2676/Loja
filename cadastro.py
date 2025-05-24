import tkinter as tk
from tkinter import messagebox
from bd import Database

class CadastroGUI(tk.Frame):
    def __init__(self, parent, database):
        super().__init__(parent)
        self.database = database

        tk.Label(self, text="Nome:").pack()
        self.nome = tk.Entry(self)
        self.nome.pack()

        tk.Label(self, text="Categoria:").pack()
        self.categoria = tk.Entry(self)
        self.categoria.pack()

        tk.Label(self, text="Preço:").pack()
        self.preco = tk.Entry(self)
        self.preco.pack()

        tk.Label(self, text="Estoque:").pack()
        self.estoque = tk.Entry(self)
        self.estoque.pack()

        tk.Label(self, text="Fornecedor:").pack()
        self.fornecedor = tk.Entry(self)
        self.fornecedor.pack()

        tk.Button(self, text="Salvar", command=self.salvar_produto).pack()

    def salvar_produto(self):
        self.database.cursor.execute("""
            INSERT INTO produtos (nome, categoria, preco, estoque, fornecedor)
            VALUES (?, ?, ?, ?, ?)
        """, (self.nome.get(), self.categoria.get(), float(self.preco.get()), 
              int(self.estoque.get()), self.fornecedor.get()))
        self.database.conn.commit()
        messagebox.showinfo("Sucesso", "Produto cadastrado!")





