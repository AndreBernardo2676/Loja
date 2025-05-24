import tkinter as tk
from bd import Database

class RelatorioGUI(tk.Frame):
    def __init__(self, parent, database):
        super().__init__(parent)
        self.database = database

        tk.Button(self, text="Gerar Relatório", command=self.gerar_relatorio).pack()
        self.texto_relatorio = tk.Text(self)
        self.texto_relatorio.pack(expand=True, fill="both")

    def gerar_relatorio(self):
        self.texto_relatorio.delete(1.0, tk.END)
        self.database.cursor.execute("SELECT * FROM produtos")
        produtos = self.database.cursor.fetchall()
        for produto in produtos:
            self.texto_relatorio.insert(tk.END, f"{produto}\n")
