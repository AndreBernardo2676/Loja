import tkinter as tk
from tkinter import ttk
from bd import Database
from cadastro import CadastroGUI
from relatorio import RelatorioGUI
from vendas import VendasGUI
from editarProduto import EditarProdutoGUI

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🛍️ Lojinha Estácio")
        self.geometry("800x500")  
        self.configure(bg="#f5f5f5")

        # Estilizando os widgets/Frames
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Tema
        self.style.configure("TNotebook", background="#ffffff", borderwidth=0)
        self.style.configure("TNotebook.Tab", padding=[10, 5], font=("Arial", 12, "bold"))
        self.style.configure("TFrame", background="#ffffff")

        self.database = Database()

        # Notebook com espaçamento ajustado
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        # As abas com um frame com cor
        self.cadastro_tab = CadastroGUI(self.notebook, self.database)
        self.vendas_tab = VendasGUI(self.notebook, self.database)
        self.relatorio_tab = RelatorioGUI(self.notebook, self.database)
        self.editarProduto_tab = EditarProdutoGUI(self.notebook, self.database)

        self.notebook.add(self.cadastro_tab, text="Cadastro")
        self.notebook.add(self.vendas_tab, text="Vendas")          
        self.notebook.add(self.editarProduto_tab, text="Editar produto")
        self.notebook.add(self.relatorio_tab, text="Relatórios")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()