import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class VendasGUI(tk.Frame):
    def __init__(self, parent, database):
        super().__init__(parent)
        self.database = database

        tk.Label(self, text="Produto:").pack()
        self.produto_combo = ttk.Combobox(self, state="readonly")
        self.produto_combo.pack()

        tk.Button(self, text="Recarregar Produtos", command=self.carregar_produtos).pack()

        tk.Label(self, text="Quantidade:").pack()
        self.quantidade_entry = tk.Entry(self)
        self.quantidade_entry.pack()

        self.total_label = tk.Label(self, text="Total: R$ 0.00")
        self.total_label.pack()

        tk.Button(self, text="Calcular Total", command=self.calcular_total).pack()
        tk.Button(self, text="Finalizar Venda", command=self.finalizar_venda).pack()

        self.produtos = []  
        self.carregar_produtos()

    def carregar_produtos(self):
        self.produtos = self.database.listar_produtos()
        nomes = [f"{p[1]} (Estoque: {p[3]})" for p in self.produtos]
        self.produto_combo['values'] = nomes

    def calcular_total(self):
        try:
            index = self.produto_combo.current()
            if index == -1:
                raise ValueError("Nenhum produto selecionado.")
            quantidade = int(self.quantidade_entry.get())
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")
            preco = self.produtos[index][2]
            total = quantidade * preco
            self.total_label.config(text=f"Total: R$ {total:.2f}")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro inesperado", str(e))

    def finalizar_venda(self):
        try:
            index = self.produto_combo.current()
            if index == -1:
                raise ValueError("Nenhum produto selecionado.")
            produto_id, nome, preco, estoque = self.produtos[index]
            quantidade = int(self.quantidade_entry.get())

            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")
            if quantidade > estoque:
                raise ValueError("Quantidade maior que o estoque disponível.")

            total = quantidade * preco

            sucesso = self.database.registrar_venda(produto_id, quantidade, total)

            if sucesso:
                messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
                self.quantidade_entry.delete(0, tk.END)
                self.total_label.config(text="Total: R$ 0.00")
                self.carregar_produtos()
            else:
                messagebox.showerror("Erro", "Falha ao registrar venda.")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            messagebox.showerror("Erro inesperado", str(e))
