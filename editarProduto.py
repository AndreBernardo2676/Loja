import tkinter as tk
from tkinter import ttk, messagebox

class EditarProdutoGUI(tk.Frame):
    def __init__(self, parent, database):
        super().__init__(parent)
        self.database = database

        self.produto_id_var = tk.StringVar()
        self.nome_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.preco_var = tk.StringVar()
        self.estoque_var = tk.StringVar()
        self.fornecedor_var = tk.StringVar()

        self.criar_widgets()

    def criar_widgets(self):
        frame = tk.LabelFrame(self, text="Editar Produto", padx=20, pady=20)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        tk.Label(frame, text="ID do Produto:", font=("Roboto", 12)).grid(row=0, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.produto_id_var, font=("Roboto", 12), width=15).grid(row=0, column=1, pady=5, sticky="w")
        tk.Button(frame, text="Buscar", command=self.buscar_produto).grid(row=0, column=2, padx=5)

        tk.Label(frame, text="Nome:", font=("Roboto", 12)).grid(row=1, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.nome_var, font=("Roboto", 12)).grid(row=1, column=1, columnspan=2, pady=5, sticky="ew")

        tk.Label(frame, text="Categoria:", font=("Roboto", 12)).grid(row=2, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.categoria_var, font=("Roboto", 12)).grid(row=2, column=1, columnspan=2, pady=5, sticky="ew")

        tk.Label(frame, text="Preço:", font=("Roboto", 12)).grid(row=3, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.preco_var, font=("Roboto", 12)).grid(row=3, column=1, columnspan=2, pady=5, sticky="ew")

        tk.Label(frame, text="Estoque:", font=("Roboto", 12)).grid(row=4, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.estoque_var, font=("Roboto", 12)).grid(row=4, column=1, columnspan=2, pady=5, sticky="ew")

        tk.Label(frame, text="Fornecedor:", font=("Roboto", 12)).grid(row=5, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.fornecedor_var, font=("Roboto", 12)).grid(row=5, column=1, columnspan=2, pady=5, sticky="ew")

        tk.Button(self, text="Atualizar", command=self.atualizar_produto).pack()

        for i in range(3):
            frame.grid_columnconfigure(i, weight=1)

    def buscar_produto(self):
        produto_id = self.produto_id_var.get().strip()
        if not produto_id.isdigit():
            messagebox.showwarning("Atenção", "Digite um ID válido!")
            return

        try:
            produto = self.database.buscar_produto(int(produto_id))
            if not produto:
                messagebox.showerror("Erro", f"Nenhum produto encontrado com ID {produto_id}")
                return

            self.nome_var.set(produto[1])
            self.categoria_var.set(produto[2])
            self.preco_var.set(str(produto[3]))
            self.estoque_var.set(str(produto[4]))
            self.fornecedor_var.set(produto[5])
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar produto: {e}")

    def atualizar_produto(self):
        produto_id = self.produto_id_var.get().strip()
        nome = self.nome_var.get().strip()
        categoria = self.categoria_var.get().strip()
        preco = self.preco_var.get().strip()
        estoque = self.estoque_var.get().strip()
        fornecedor = self.fornecedor_var.get().strip()

        if not all([produto_id, nome, categoria, preco, estoque, fornecedor]):
            messagebox.showwarning("Atenção", "Todos os campos devem ser preenchidos!")
            return

        try:
            preco = float(preco)
            estoque = int(estoque)
        except ValueError:
            messagebox.showwarning("Erro", "Preço deve ser número decimal e estoque número inteiro.")
            return

        try:
            sucesso = self.database.atualiza_produto(int(produto_id), nome, categoria, preco, estoque, fornecedor)
            if sucesso is None: 
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Falha ao atualizar produto.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar produto: {e}")
