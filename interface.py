import customtkinter
import tkinter.messagebox as tkmb

customtkinter.set_appearance_mode ("dark")
customtkinter.set_default_color_theme ("dark-blue")

janela = customtkinter.CTk ()
janela.geometry ("500x300")
janela.title ("Login e Cadastro")

senha_usuario = "1234"
cpf_usuario = "12345678909"

def validar_cpf (cpf: str) -> bool:
    cpf = ''.join (filter (str.isdigit, cpf))
    if len (cpf) != 11 or cpf == cpf [0] * 11:
        return False
    soma = sum (int (cpf [i]) * (10 - i) for i in range (9))
    digito1 = (soma * 10 % 11) % 10
    soma = sum (int (cpf [i]) * (11 - i) for i in range (10))
    digito2 =  (soma * 10 % 11) % 10
    return cpf [-2:] == f"{digito1}{digito2}"

def login ():
    
    cpf_input = cpf.get ()
    senha_input = senha.get ()    
    
    if cpf_input == cpf_usuario and senha_input == senha_usuario:
        tkmb.showinfo ("Login Realizado", "Login realizado com sucesso")
        customtkinter.CTkLabel (janela, text = "Menu").pack ()
    elif cpf_input != cpf_usuario and senha_input == senha_usuario:
        tkmb.showerror ("Erro CPF", "CPF inválido")
    elif cpf_input == cpf_usuario and senha_input != senha_usuario:
        tkmb.showerror ("Erro senha", "Senha inválido")
    else:
        tkmb.showerror ("Erro", "Senha e CPF inválido")
        
def cadastro ():
    
    novo_cpf = cpf_cadastro.get ()
    nova_senha = senha_cadastro.get ()
    confirmar = confirmar_senha.get ()

    if not novo_cpf or not nova_senha or not confirmar:
        tkmb.showwarning ("Campos vazios", "Preencha todos os campos")
    elif not validar_cpf(novo_cpf):
        tkmb.showerror("Erro CPF", "CPF inválido")
    elif nova_senha != confirmar:
        tkmb.showerror ("Erro", "Senhas não coincidem")
    else:
        tkmb.showinfo ("Cadastro", "Cadastro realizado com sucesso")

# Abas: Login e Cadastro
tabview = customtkinter.CTkTabview (janela)
tabview.pack (expand = True, fill = "both", padx = 20, pady = 20)

tabview.add ("Login")
tabview.add ("Cadastro")
 
# Aba Login
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
    
# Aba Cadastro
cadastro_tab = tabview.tab("Cadastro")

texto = customtkinter.CTkLabel (cadastro_tab, text = "Fazer Cadastro")
texto.pack (padx = 10, pady = 10)

cpf_cadastro = customtkinter.CTkEntry (cadastro_tab, placeholder_text = "CPF")
cpf_cadastro.pack (padx = 10, pady = 10)

senha_cadastro = customtkinter.CTkEntry (cadastro_tab, placeholder_text = "Senha", show = "*")
senha_cadastro.pack (padx = 10, pady = 10)

confirmar_senha = customtkinter.CTkEntry (cadastro_tab, placeholder_text = "Confirmar Senha", show = "*")
confirmar_senha.pack (padx = 10, pady = 10)

botao = customtkinter.CTkButton (cadastro_tab, text = "Cadastrar", command = cadastro)
botao.pack (padx = 10, pady = 10)
    
janela.mainloop ()