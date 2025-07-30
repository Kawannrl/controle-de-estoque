import sqlite3
from datetime import datetime

class Sessao:
    usuario_logado = None
    tipo_usuario = None
    
    
def conectar_banco ():
    conexao = sqlite3.connect ("controle de estoque")
    return conexao

def criar_tabelas ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''create table if not exists produto (id integer primary key, nome text, valor real, codigo integer, estoque integer, categoria text)''')
    cursor.execute ('''create table if not exists usuarios (id integer primary key, cpf integer, nome text, senha text, classificacao text not null check( classificacao IN ('admin', 'usuario') ))''')
    cursor.execute('''create table if not exists compras_efetuadas (id integer primary key, nome text, valor real, codigo integer, categoria text, data text)''')
    try: 
        cursor.execute ('''insert into usuarios (cpf, nome, senha, classificacao) values ('07472708216', 'roma', '101224', 'admin')''')
    except sqlite3.IntegrityError:
        pass  # Admin já existe

    conexao.commit ()
    conexao.close ()

def criar_usuario(cpf, nome, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('''select cpf from usuarios where cpf=?''', (cpf,))
    usuario1 = cursor.fetchall()
    
    if usuario1:
        print("o usuario já existe, tente outro cpf")
        return False
    else:
        cursor.execute(''' insert into usuarios(cpf, nome, senha, classificacao)
                values (?, ?, ?,'usuario')''', (cpf, nome,senha))
        
        conexao.commit()
        return True
    
def criar_produto(nome, valor, codigo, estoque, categoria ):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('''select nome, codigo from usuarios where cpf=?''', (nome, codigo,))
    produto1 = cursor.fetchall()
    
    if produto1:
        print("este nome já existe e código já existem, tente outro nome e outro codigo de barras")
        return False
    else:
        cursor.execute(''' insert into produto(nome, valor, codigo, estoque, categoria)
                values (?, ?, ?, ?, ?)''', (nome, valor, codigo, estoque, categoria))
        
        conexao.commit()
        return True
    
def buscar_produtos_por_codigos(codigos):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    placeholders = ','.join('?' for _ in codigos)
    cursor.execute(f'''
        SELECT nome, valor, codigo, categoria FROM produto WHERE codigo IN ({placeholders})
    ''', codigos)
    produtos = cursor.fetchall()
    conexao.close()
    return [
        {"nome": nome, "valor": valor, "codigo": codigo, "categoria": categoria}
        for nome, valor, codigo, categoria in produtos
    ]
    
def efetuar_compras_em_lote(lista_de_produtos):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    data_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        cursor.execute("BEGIN TRANSACTION")
        for produto in lista_de_produtos:
            cursor.execute('''
                INSERT INTO compras_efetuadas (nome, valor, codigo, categoria, data)
                VALUES (?, ?, ?, ?, ?)
            ''', (produto['nome'], produto['valor'], produto['codigo'], produto['categoria'], data_compra))

            cursor.execute('''
                UPDATE produto SET estoque = estoque - 1 WHERE codigo = ? AND estoque > 0
            ''', (produto['codigo'],))
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print("Erro ao registrar compras:", e)
    finally:
        conexao.close()

def login(cpf, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM usuarios WHERE cpf=?", (cpf,))
    usuario = cursor.fetchone()
    
    conexao.close()

    if usuario and usuario[3] == senha:
        tipo = usuario[4]
        Sessao.usuario_logado = usuario[1] 
        Sessao.tipo_usuario = tipo
        if tipo == 'admin':
            return 1
        else:
            return 0
    else:
        print("Usuário ou senha inválidos.")
        return -1

def show_usuarios_cadastrados ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''selecte from * usuarios''')
    usuarios = cursor.fetchall ()
    conexao.close ()
    return usuarios
