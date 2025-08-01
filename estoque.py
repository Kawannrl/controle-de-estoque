import customtkinter as ctk
import tkinter.messagebox as tkmb
from database import criar_produto, conectar_banco  # + funções que vamos usar abaixo

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class Estoque(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x300")
        self.title("Menu ADM - Controle de Produto")

        self.criar_aba_estoque()
        self.mainloop()

    def cadastrar(self):
        codigo = self.codigo_produto.get()
        nome = self.nome_produto.get()
        valor = self.valor_produto.get()
        quantidade = self.quantidade_produto.get()
        tipo = self.tipo_produto.get()

        if not all([codigo, nome, valor, quantidade, tipo]):
            tkmb.showwarning("Campos vazios", "Preencha todos os campos.")
            return

        try:
            sucesso = criar_produto(nome, float(valor), int(codigo), int(quantidade), tipo)
            if sucesso:
                tkmb.showinfo("Sucesso", f"Produto '{nome}' cadastrado.")
            else:
                tkmb.showerror("Erro", "Código ou nome já cadastrados.")
        except ValueError:
            tkmb.showerror("Erro", "Valor ou quantidade inválidos.")

    def buscar(self):
        codigo = self.codigo_produto.get()
        if not codigo:
            tkmb.showwarning("Código vazio", "Digite o código do produto.")
            return

        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, valor, estoque, categoria FROM produto WHERE codigo=?", (codigo,))
        resultado = cursor.fetchone()
        conexao.close()

        if resultado:
            nome, valor, quantidade, tipo = resultado

            self.nome_produto.delete(0, "end")
            self.valor_produto.delete(0, "end")
            self.quantidade_produto.delete(0, "end")
            self.tipo_produto.delete(0, "end")

            self.nome_produto.insert(0, nome)
            self.valor_produto.insert(0, valor)
            self.quantidade_produto.insert(0, quantidade)
            self.tipo_produto.insert(0, tipo)

            tkmb.showinfo("Encontrado", f"Produto '{nome}' encontrado.")
        else:
            tkmb.showerror("Erro", "Produto não encontrado.")

    def excluir(self):
        codigo = self.codigo_produto.get()
        if not codigo:
            tkmb.showwarning("Código vazio", "Digite o código do produto.")
            return

        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM produto WHERE codigo=?", (codigo,))
        conexao.commit()
        conexao.close()

        tkmb.showinfo("Excluído", f"Produto com código '{codigo}' removido.")
        self.limpar_campos()

    def editar(self):
        codigo = self.codigo_produto.get()
        nome = self.nome_produto.get()
        valor = self.valor_produto.get()
        quantidade = self.quantidade_produto.get()
        tipo = self.tipo_produto.get()

        if not all([codigo, nome, valor, quantidade, tipo]):
            tkmb.showwarning("Campos vazios", "Preencha todos os campos.")
            return

        try:
            conexao = conectar_banco()
            cursor = conexao.cursor()
            cursor.execute(
                '''UPDATE produto 
                   SET nome=?, valor=?, estoque=?, categoria=? 
                   WHERE codigo=?''',
                (nome, float(valor), int(quantidade), tipo, int(codigo))
            )
            conexao.commit()
            conexao.close()

            tkmb.showinfo("Atualizado", f"Produto '{nome}' atualizado.")
        except ValueError:
            tkmb.showerror("Erro", "Valor ou quantidade inválidos.")

    def limpar_campos(self):
        for campo in [self.codigo_produto, self.nome_produto, self.valor_produto, self.quantidade_produto, self.tipo_produto]:
            campo.delete(0, "end")

    def criar_aba_estoque(self):
        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)

        ctk.CTkLabel(frame, text="Código:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.codigo_produto = ctk.CTkEntry(frame)
        self.codigo_produto.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame, text="Nome:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.nome_produto = ctk.CTkEntry(frame)
        self.nome_produto.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame, text="Valor (R$):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.valor_produto = ctk.CTkEntry(frame)
        self.valor_produto.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame, text="Quantidade:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.quantidade_produto = ctk.CTkEntry(frame)
        self.quantidade_produto.grid(row=3, column=1, padx=10, pady=5)

        ctk.CTkLabel(frame, text="Tipo de Produto:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.tipo_produto = ctk.CTkEntry(frame)
        self.tipo_produto.grid(row=4, column=1, padx=10, pady=5)

        botao_frame = ctk.CTkFrame(frame)
        botao_frame.grid(row=5, column=0, columnspan=2, pady=20)

        ctk.CTkButton(botao_frame, text="Cadastrar", command=self.cadastrar).grid(row=0, column=0, padx=10)
        ctk.CTkButton(botao_frame, text="Buscar", command=self.buscar).grid(row=0, column=1, padx=10)
        ctk.CTkButton(botao_frame, text="Editar", command=self.editar).grid(row=0, column=2, padx=10)
        ctk.CTkButton(botao_frame, text="Excluir", command=self.excluir).grid(row=0, column=3, padx=10)


if __name__ == "__main__":
    Estoque()
