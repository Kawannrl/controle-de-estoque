import database
# import interface

def tentar_login(cpf, senha):
    return database.login(cpf, senha)

def tentar_cadastro (cpf, nome, senha):
    
    if database.criar_usuario (cpf, nome, senha):
        return True
    return False