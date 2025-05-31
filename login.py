import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from main import MainApp
from cadastroUsuario import CadastroUsuario

class Login:
    def __init__(self):
        self.loginw = tk.Tk()
        
        self.loginw.title("Login")
        width, height = 500, 600
        screen_width = self.loginw.winfo_screenwidth()
        screen_height = self.loginw.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.loginw.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
        self.loginw.resizable(0, 0)
        self.loginw.protocol('WM_DELETE_WINDOW', self.__login_del__)
        self.loginw.config(bg="#D2B48C")

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.obj()
        self.loginw.mainloop()

    def __login_del__(self):
        if messagebox.askyesno("SAIR", "DESEJA REALMENTE SAIR DO SISTEMA?"):
            self.loginw.destroy()
            exit(0)

    def obj(self):
        self.loginframe = tk.LabelFrame(self.loginw, bg="#D2B48C", height=400, width=300)
        self.loginframe.place(x=103, y=95)

        self.toplabel = tk.Label(self.loginframe, fg="white", bg="#D2B48C", anchor="center", text="Login", font="Roboto 40 bold")
        self.toplabel.place(x=75, y=25)

        # usuario 
        self.userlabel = tk.Label(self.loginframe, text="Usuário", bg="#D2B48C", fg="black", font="Roboto 12")
        self.userlabel.place(x=35, y=120)
        self.us = ttk.Entry(self.loginframe, width=20, textvariable=self.username, font="Roboto 14")
        self.us.place(x=35, y=145, height=40)

        # senha
        self.passlabel = tk.Label(self.loginframe, text="Senha", bg="#D2B48C", fg="black", font="Roboto 12")
        self.passlabel.place(x=35, y=185)

        self.pa = ttk.Entry(self.loginframe, width=20, textvariable=self.password, font="Roboto 14", show="*")
        self.pa.place(x=35, y=205, height=40)

        # btn login 
        self.signin = tk.Button(self.loginframe, width=20, text="ENTRAR", bg="#008B8B", fg="white", bd="0", font="Roboto 14", command=self.verificar_login)
        self.signin.place(x=35, y=290)
        
        # btn cadastro 
        self.btn_cadastrar = tk.Button(self.loginframe, width=20, text="CADASTRAR USUÁRIO", bg="#555555", fg="white", bd="0", font="Roboto 12", command=self.cadastro_usuario)
        self.btn_cadastrar.place(x=35, y=340)

        


    def verificar_login(self):
        usuario = self.username.get()
        senha = self.password.get()

        try:
            conn = sqlite3.connect("loja.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM usuarios WHERE nome=? AND senha=?", (usuario, senha))
            resultado = cursor.fetchone()

            if resultado:
                self.loginw.destroy()
                app = MainApp()
                app.mainloop()  
            else:
                messagebox.showerror("ATENÇÃO", "USUÁRIO OU SENHA INCORRETOS")

            conn.close()
        except sqlite3.Error as erro:
            messagebox.showerror("ERRO", f"Erro de conexão: {erro}")
    def cadastro_usuario(self):
        CadastroUsuario(self.loginw)


if __name__ == "__main__":
    Login()
