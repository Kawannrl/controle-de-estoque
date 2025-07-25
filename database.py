import sqlite3
from flask import session
def conectar_banco ():
    conexao = sqlite3.connect ("controle de estoque")
    return conexao

def criar_tabelas ():
    conexao = conectar_banco ()
    cursor = conexao.cursor ()
    cursor.execute ('''create table if not exists produto (id integer primary key, nome text, valor real, codigo integer, estoque integer, categoria text)''')
    cursor.execute ('''create table if not exists usuarios (id integer primary key, cpf integer, nome text, senha text, classificacao text not null check( classificacao IN ('admin', 'usuario') ))''')
    
    try: 
        cursor.execute ('''insert into usuarios (cpf, nome, senha, classificacao) values ('07472708216', 'roma', '101224', 'admin')''')
    except sqlite3.IntegrityError:
        pass  # Admin já existe

    conexao.commit ()
    conexao.close ()
    
    def criar_usuario (cpf, nome, senha):
        conexao = conectar_banco ()
        cursor = conexao.cursor ()
        cursor.execute (''' insert into usuarios (cpf, nome, senha, classificacao) values (?, ?, ?'usuario')''', (cpf, nome,senha))
        conexao.commit ()
        return True
    
    def login (cpf, senha):
        conexao = conectar_banco ()
        cursor = conexao.cursor ()
        cursor.execute ("select * from usuarios where cpf = ?", (cpf,))
        usuario = cursor.fetchone ()
        conexao.close ()

        if usuario and usuario [3] == senha:
            tipo = usuario [4]
            if tipo == 'admin':
                session ['ademin'] = usuario [1]
                # return redirect(url_for('home1'))
            else:
                session ['usuario'] = usuario [1]
                # return redirect(url_for('home'))
        else:
            print ("Usuário ou senha inválidos.")

    def show_usuarios_cadastrados ():
        conexao = conectar_banco ()
        cursor = conexao.cursor ()
        cursor.execute ('''selecte from * usuarios''')
        usuarios = cursor.fetchall ()
        conexao.close ()
        return usuarios