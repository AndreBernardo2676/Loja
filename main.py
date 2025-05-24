import tkinter as tk
from tkinter import ttk
from bd import Database
from cadastro import CadastroGUI
from relatorio import RelatorioGUI

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lojinha Estácio")
        self.geometry("400x300")

        self.database = Database()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.cadastro_tab = CadastroGUI(self.notebook, self.database)
        self.relatorio_tab = RelatorioGUI(self.notebook, self.database)
        
        self.notebook.add(self.cadastro_tab, text="Cadastro")
        self.notebook.add(self.relatorio_tab, text="Relatórios")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
