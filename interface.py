import customtkinter
import tkinter.messagebox as tkmb
import app
import database

customtkinter.set_appearance_mode ("dark")
customtkinter.set_default_color_theme ("dark-blue")
database.criar_tabelas()
janela = customtkinter.CTk ()
janela.geometry ("500x300")
janela.title ("Login e Cadastro")

# senha_usuario = "1234"
# cpf_usuario = "123456789"

def login():
    usercpf = cpf.get()
    password = senha.get()
    
    resultado = app.tentar_login(usercpf, password)
    
    if resultado == 0:
        tkmb.showinfo("Bem-vindo, usuário!")
        
    elif resultado == 1:
        tkmb.showinfo("Bem-vindo, admin!")
        
    else:
        tkmb.showerror("Falha ao realizar login", "CPF ou senha inválidos.")
        
def cadastro ():
    
    novo_cpf = cpf_cadastro.get()
    novo_nome = nome_cadastro.get()
    nova_senha = senha_cadastro.get()
    

    if app.tentar_cadastro(novo_cpf, novo_nome, nova_senha):
            tkmb.showinfo("cadastro realizado com sucesso")
    else:
        tkmb.showerror("falha ao realizar cadastro, tente novamente")

tabview = customtkinter.CTkTabview (janela)
tabview.pack (expand = True, fill = "both", padx = 20, pady = 20)

tabview.add ("Login")
tabview.add ("Cadastro")
 
login_tab = tabview.tab ("Login")

texto = customtkinter.CTkLabel (login_tab, text = "Fazer Login")
texto.pack (padx = 10, pady = 10)

cpf = customtkinter.CTkEntry (login_tab, placeholder_text = "CPF")
cpf.pack (padx = 10, pady = 10)

senha = customtkinter.CTkEntry (login_tab, placeholder_text = "Senha", show = "*")
senha.pack (padx = 10, pady = 10)

checkbox = customtkinter.CTkCheckBox (login_tab, text = "Lembrar Login")
checkbox.pack (padx = 10, pady = 10)

botao = customtkinter.CTkButton (login_tab, text = "Entrar", command = login)
botao.pack (padx = 10, pady = 10)
    
cadastro_tab = tabview.tab("Cadastro")

texto = customtkinter.CTkLabel (cadastro_tab, text = "Fazer Cadastro")
texto.pack (padx = 10, pady = 10)

cpf_cadastro = customtkinter.CTkEntry (cadastro_tab, placeholder_text = "CPF")
cpf_cadastro.pack (padx = 10, pady = 10)

nome_cadastro = customtkinter.CTkEntry (cadastro_tab, placeholder_text = "NOME")
nome_cadastro.pack (padx = 10, pady = 10)

senha_cadastro = customtkinter.CTkEntry (cadastro_tab, placeholder_text = "Senha", show = "*")
senha_cadastro.pack (padx = 10, pady = 10)

confirmar_senha = customtkinter.CTkEntry (cadastro_tab, placeholder_text = "Confirmar Senha", show = "*")
confirmar_senha.pack (padx = 10, pady = 10)

botao = customtkinter.CTkButton (cadastro_tab, text = "Cadastrar", command = cadastro)
botao.pack (padx = 10, pady = 10)
    
janela.mainloop ()

