import customtkinter

customtkinter.set_appearance_mode ("dark")
customtkinter.set_default_color_theme ("dark-blue")

janela = customtkinter.CTk ()
janela.geometry ("500x300")

def login ():

    texto = customtkinter.CTkLabel (janela, text = "Fazer Login")
    texto.pack (padx = 10, pady = 10)

    cpf = customtkinter.CTkEntry (janela, placeholder_text = "CPF")
    cpf.pack (padx = 10, pady = 10)

    senha = customtkinter.CTkEntry (janela, placeholder_text = "Senha", show = "*")
    senha.pack (padx = 10, pady = 10)

    checkbox = customtkinter.CTkCheckBox (janela, text = "Lembrar Login")
    checkbox.pack (padx = 10, pady = 10)

    botao = customtkinter.CTkButton (janela, text = "Entrar", command = login)
    botao.pack (padx = 10, pady = 10)
    
def  cadastro ():
    texto = customtkinter.CTkLabel (janela, text = "Fazer Cadastro")
    texto.pack (padx = 10, pady = 10)

    cpf = customtkinter.CTkEntry (janela, placeholder_text = "CPF")
    cpf.pack (padx = 10, pady = 10)

    senha = customtkinter.CTkEntry (janela, placeholder_text = "Senha", show = "*")
    senha.pack (padx = 10, pady = 10)
    
    confirmar_senha = customtkinter.CTkEntry (janela, placeholder_text = "Confirmar Senha")
    confirmar_senha.pack (padx = 10, pady = 10)

    botao = customtkinter.CTkButton (janela, text = "Cadastrar")
    botao.pack (padx = 10, pady = 10)
    
janela.mainloop ()