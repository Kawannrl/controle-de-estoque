import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class CarrinhoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Carrinho de Compras - Funcionário")
        self.geometry("500x400")

        self.produtos = {
            "Arroz": 5.50,
            "Feijão": 7.00,
            "Macarrão": 4.25,
            "Açúcar": 3.99
        }

        self.carrinho = []

        # Lista de produtos
        self.label_lista = ctk.CTkLabel(self, text="Produtos Disponíveis", font=("Arial", 16))
        self.label_lista.pack(pady=5)

        for nome, preco in self.produtos.items():
            botao = ctk.CTkButton(self, text=f"{nome} - R${preco:.2f}",
                                  command=lambda n=nome: self.adicionar_ao_carrinho(n))
            botao.pack(pady=2)

        # Carrinho visual
        self.label_carrinho = ctk.CTkLabel(self, text="Carrinho", font=("Arial", 16))
        self.label_carrinho.pack(pady=10)

        self.lista_itens = ctk.CTkTextbox(self, height=100, width=400)
        self.lista_itens.pack()

        # Total
        self.total_label = ctk.CTkLabel(self, text="Total: R$ 0.00", font=("Arial", 14))
        self.total_label.pack(pady=10)

        # Botão de finalizar
        self.botao_finalizar = ctk.CTkButton(self, text="Finalizar Compra", command=self.finalizar_compra)
        self.botao_finalizar.pack(pady=10)



    def adicionar_ao_carrinho(self, nome_produto):
        preco = self.produtos[nome_produto]
        self.carrinho.append((nome_produto, preco))
        self.atualizar_carrinho()

    def atualizar_carrinho(self):
        self.lista_itens.delete("1.0", "end")
        total = 0
        for nome, preco in self.carrinho:
            self.lista_itens.insert("end", f"{nome} - R$ {preco:.2f}\n")
            total += preco
        self.total_label.configure(text=f"Total: R$ {total:.2f}")

    def finalizar_compra(self):
        if self.carrinho:
            self.lista_itens.insert("end", "\nCompra finalizada!\n")
            self.carrinho.clear()
            self.total_label.configure(text="Total: R$ 0.00")
        else:
            self.lista_itens.insert("end", "Carrinho vazio!\n")

if __name__ == "__main__":
    app = CarrinhoApp()
    app.mainloop()
