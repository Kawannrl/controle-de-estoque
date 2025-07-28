import database
# import interface

def tentar_login(cpf, senha):
    
    if database.login(cpf, senha):
        return True
    return False

def tentar_cadastro(cpf, nome, senha):
    
    if database.criar_usuario(cpf, nome, senha):
        return True
    return False