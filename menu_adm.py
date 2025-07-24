import customtkinter
import tkinter.messagebox as tkmb

customtkinter.set_appearance_mode ("dark")
customtkinter.set_default_color_theme ("dark-blue")

janela = customtkinter.CTk ()
janela.geometry ("700x300")
janela.title ("Menu ADM - Controle de Produto")

estoque = {}

def cadastrar ():
    codigo = codigo_produto.get ()
    nome = nome_produto.get ()
    valor = valor_produto.get ()
    quantidade = quantidade_produto.get ()
    tipo = tipo_produto ()

    if not all ([codigo, nome, valor, quantidade, tipo]):
        tkmb.showwarning ("Campos vazios", "Preencha todos os campos.")
        return

    if codigo in estoque:
        tkmb.showerror ("Erro", "Código já cadastrado.")
        return

    try:
        estoque [codigo] = {
            "nome": nome,
            "valor": float (valor),
            "quantidade": int (quantidade),
            "tipo": tipo
        }
        tkmb.showinfo ("Sucesso", f"Produto '{nome}' cadastrado.")
    except ValueError:
        tkmb.showerror ("Erro", "Valor ou quantidade inválidos.")
        
def buscar ():
    codigo = codigo_produto.get ()
    produto = estoque.get (codigo)

    if produto:
        nome_produto.delete (0, "end")
        valor_produto.delete (0, "end")
        quantidade_produto.delete (0, "end")
        tipo_produto.delete (0, "end")

        nome_produto.insert(0, produto["nome"])
        valor_produto.insert(0, produto["valor"])
        quantidade_produto.insert(0, produto["quantidade"])
        tipo_produto.insert(0, produto["tipo"])

        tkmb.showinfo("Encontrado", f"Produto '{produto['nome']}' encontrado.")
    else:
        tkmb.showerror("Erro", "Produto não encontrado.")
        
def excluir ():
    codigo = codigo_produto.get ()
    if codigo in estoque:
        del estoque [codigo]
        tkmb.showinfo("Excluído", f"Produto com código '{codigo}' removido.")
        limpar_campos ()
    else:
        tkmb.showerror ("Erro", "Produto não encontrado.")
        
def editar ():
    codigo = codigo_produto.get ()
    if codigo not in estoque:
        tkmb.showerror("Erro", "Produto não encontrado.")
        return

    try:
        estoque [codigo] = {
            "nome": nome_produto.get(),
            "valor": float(valor_produto.get()),
            "quantidade": int(quantidade_produto.get()),
            "tipo": tipo_produto.get()
        }
        tkmb.showinfo("Atualizado", f"Produto '{nome_produto.get()}' atualizado.")
    except ValueError:
        tkmb.showerror("Erro", "Valor ou quantidade inválidos.")

def limpar_campos():
    for campo in [codigo_produto, nome_produto, valor_produto, quantidade_produto, tipo_produto]:
        campo.delete (0, "end")
        
# Interface
frame = customtkinter.CTkFrame (janela)
frame.pack (padx = 20, pady = 20, fill = "both", expand = True)

customtkinter.CTkLabel (frame, text="Código:").grid (row = 0, column = 0, padx = 10, pady = 5, sticky = "w")
codigo_produto = customtkinter.CTkEntry (frame)
codigo_produto.grid (row = 0, column = 1, padx = 10, pady = 5)

customtkinter.CTkLabel (frame, text = "Nome:").grid (row = 1, column = 0, padx = 10, pady = 5, sticky = "w")
nome_produto = customtkinter.CTkEntry (frame)
nome_produto.grid (row = 1, column = 1, padx = 10, pady = 5)

customtkinter.CTkLabel (frame, text = "Valor (R$):").grid (row = 2, column = 0, padx = 10, pady = 5, sticky = "w")
valor_produto = customtkinter.CTkEntry (frame)
valor_produto.grid (row = 2, column = 1, padx = 10, pady = 5)

customtkinter.CTkLabel (frame, text = "Quantidade:").grid (row = 3, column = 0, padx = 10, pady = 5, sticky = "w")
quantidade_produto = customtkinter.CTkEntry (frame)
quantidade_produto.grid (row = 3, column = 1, padx = 10, pady = 5)

customtkinter.CTkLabel (frame, text = "Tipo de Produto:").grid (row = 4, column = 0, padx = 10, pady = 5, sticky = "w")
tipo_produto = customtkinter.CTkEntry (frame)
tipo_produto.grid (row = 4, column = 1, padx = 10, pady = 5)

# Botões
botao_frame = customtkinter.CTkFrame (frame)
botao_frame.grid (row = 5, column = 0, columnspan = 2, pady = 20)

customtkinter.CTkButton (botao_frame, text="Cadastrar", command=cadastrar).grid (row = 0, column = 0, padx = 10)
customtkinter.CTkButton (botao_frame, text="Buscar", command=buscar).grid (row = 0, column = 1, padx = 10)
customtkinter.CTkButton (botao_frame, text="Editar", command=editar).grid (row = 0, column = 2, padx = 10)
customtkinter.CTkButton (botao_frame, text="Excluir", command=excluir).grid (row = 0, column = 3, padx = 10)

janela.mainloop ()