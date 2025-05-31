import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class CadastroUsuario:
    def __init__(self, parent):
        self.parent = parent
        self.toplevel = tk.Toplevel(parent)
        self.toplevel.title("Cadastrar Usuário")
        self.toplevel.geometry("400x300")
        self.toplevel.resizable(0, 0)
        self.toplevel.grab_set()  

        self.nome_var = tk.StringVar()
        self.senha_var = tk.StringVar()

        self.obj()

    def obj(self):
        frame = tk.LabelFrame(self.toplevel, text="Cadastro de Usuário", padx=20, pady=20)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Nome:", font=("Roboto", 12)).grid(row=0, column=0, sticky="w")
        self.nome_entry = ttk.Entry(frame, textvariable=self.nome_var, font=("Roboto", 12))
        self.nome_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Senha:", font=("Roboto", 12)).grid(row=1, column=0, sticky="w")
        self.senha_entry = ttk.Entry(frame, textvariable=self.senha_var, font=("Roboto", 12), show="*")
        self.senha_entry.grid(row=1, column=1, pady=5)

        btn_cadastrar = tk.Button(frame, text="Cadastrar", bg="#008B8B", fg="white", font=("Roboto", 12), bd=0, command=self.cadastrar)
        btn_cadastrar.grid(row=2, column=0, columnspan=2, pady=20)

    def cadastrar(self):
        nome = self.nome_var.get().strip()
        senha = self.senha_var.get().strip()

        if not nome or not senha:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return

        try:
            conn = sqlite3.connect("loja.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE nome=?", (nome,))
            if cursor.fetchone():
                messagebox.showerror("Erro", "Este usuário já existe!")
                conn.close()
                return

            cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!!!")
            self.toplevel.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar o usuário: {e}")
