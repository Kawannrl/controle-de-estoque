import customtkinter as ctk
import tkinter.messagebox as tkmb
import app
from carrinho import CarrinhoApp
from estoque import Estoque

ctk.set_appearance_mode ("dark")
ctk.set_default_color_theme ("dark-blue")

senha_usuario = "1234"
cpf_usuario = "12345678909"

class LoginApp (ctk.CTk):
    def __init__ (self):
        super ().__init__ ()

        self.geometry ("600x400")
        self.title ("Login e Cadastro")

        self.criar_interface ()
        self.mainloop ()

    def criar_interface (self):
        self.tabview = ctk.CTkTabview (self)
        self.tabview.pack (expand = True, fill = "both", padx = 20, pady = 20)

        self.tabview.add ("Login")
        self.tabview.add ("Cadastro")

        self.criar_aba_login ()
        self.criar_aba_cadastro ()

    def validar_cpf (self, cpf: str) -> bool:
        cpf = ''.join (filter (str.isdigit, cpf))
        if len (cpf) != 11 or cpf == cpf [0] * 11:
            return False
        soma = sum (int(cpf [i]) * (10 - i) for i in range (9))
        digito1 =  (soma * 10 % 11) % 10
        soma = sum (int(cpf [i]) * (11 - i) for i in range (10))
        digito2 =  (soma * 10 % 11) % 10
        return cpf [-2:] == f"{digito1}{digito2}"

    def criar_aba_login (self):
        login_tab = self.tabview.tab ("Login")

        ctk.CTkLabel (login_tab, text = "Fazer Login").pack (padx = 10, pady = 10)

        self.cpf_entry = ctk.CTkEntry (login_tab, placeholder_text = "CPF")
        self.cpf_entry.pack (padx = 10, pady = 10)

        self.senha_entry = ctk.CTkEntry (login_tab, placeholder_text = "Senha", show = "*")
        self.senha_entry.pack (padx = 10, pady = 10)

        ctk.CTkCheckBox (login_tab, text = "Lembrar Login").pack (padx = 10, pady = 10)

        ctk.CTkButton (login_tab, text = "Entrar", command = self.login).pack (padx = 10, pady = 10)

    def criar_aba_cadastro (self):
        cadastro_tab = self.tabview.tab ("Cadastro")

        ctk.CTkLabel (cadastro_tab, text = "Fazer Cadastro").pack (padx = 10, pady = 10)

        self.cpf_cadastro = ctk.CTkEntry (cadastro_tab, placeholder_text = "CPF")
        self.cpf_cadastro.pack (padx = 10, pady = 10)
        
        self.nome_cadastro = ctk.CTkEntry (cadastro_tab, placeholder_text = "NOME")
        self.nome_cadastro.pack (padx = 10, pady = 10)

        self.senha_cadastro = ctk.CTkEntry (cadastro_tab, placeholder_text = "Senha", show = "*")
        self.senha_cadastro.pack (padx = 10, pady = 10)

        self.confirmar_senha = ctk.CTkEntry (cadastro_tab, placeholder_text = "Confirmar Senha", show = "*")
        self.confirmar_senha.pack (padx = 10, pady = 10)

        ctk.CTkButton (cadastro_tab, text="Cadastrar", command = self.cadastro).pack (padx = 10, pady = 10)

    def login (self):
        usercpf = self.cpf_entry.get ()
        password = self.senha_entry.get ()
        
        resultado = app.tentar_login (usercpf, password)
        
        if resultado == 0:
            tkmb.showinfo ("Login Funcionario","Bem-vindo, Funcionario!")
            self.destroy () 
            carrinho = CarrinhoApp ()
            carrinho.mainloop ()
        elif resultado == 1:
            tkmb.showinfo ("Login admin","Bem-vindo, admin!")
            self.destroy ()
            estoque = Estoque ()
            estoque.mainloop ()
        else:
            tkmb.showerror ("Falha ao realizar login", "CPF ou senha inválidos.")

    def cadastro (self):
        
        novo_cpf = self.cpf_cadastro.get ()
        novo_nome = self.nome_cadastro.get ()
        nova_senha = self.senha_cadastro.get ()
        
        if app.tentar_cadastro (novo_cpf, novo_nome, nova_senha):
                tkmb.showinfo ("cadastro realizado","cadastro realizado com sucesso")
        else:
            tkmb.showerror ("falha","falha ao realizar cadastro, tente novamente")  