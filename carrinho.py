import customtkinter as ctk

ctk.set_appearance_mode ("dark")
ctk.set_default_color_theme ("dark-blue")


class CarrinhoApp (ctk.CTk):
    def __init__ (self):
        super ().__init__ ()
        self.title ("Carrinho de Compras - Funcionário")
        self.geometry ("600x500")
        

        self.produtos = {
            "001": {"nome": "Arroz", "preco": 5.50},
            "002": {"nome": "Feijão", "preco": 7.00},
            "003": {"nome": "Macarrão", "preco": 4.25},
            "004": {"nome": "Açúcar", "preco": 3.99}
        }

        self.carrinho = {}

        self.frame_top = ctk.CTkFrame (self)
        self.frame_top.pack (pady = 10, padx = 10, fill = "x")

        self.entrada_codigo = ctk.CTkEntry (self.frame_top, placeholder_text = "Digite o código do produto")
        self.entrada_codigo.pack (side = "left", padx = (0, 10), expand = True)

        self.botao_adicionar = ctk.CTkButton (self.frame_top, text = "Adicionar", command = self.adicionar_produto)
        self.botao_adicionar.pack (side="left", padx = 5)

        self.botao_remover = ctk.CTkButton (self.frame_top, text = "Remover", command = self.remover_produto)
        self.botao_remover.pack (side = "left", padx = 5)

        self.frame_lista = ctk.CTkFrame (self)
        self.frame_lista.pack (pady = 10, padx = 10, fill = "both", expand = True)

        self.frame_bottom = ctk.CTkFrame (self)
        self.frame_bottom.pack (side = "bottom", fill = "x", padx = 10, pady = 10)

        self.total_label = ctk.CTkLabel (self.frame_bottom, text = "Total: R$ 0.00", font = ("Arial", 14))
        self.total_label.pack (side = "left")

        self.botao_pagamento = ctk.CTkButton (self.frame_bottom, text = "Pagamento", command = self.abrir_pagamento)
        self.botao_pagamento.pack (side = "right")

    def adicionar_produto (self):
        codigo = self.entrada_codigo.get ().strip ()
        if codigo in self.produtos:
            if codigo in self.carrinho:
                self.carrinho [codigo]["quantidade"] += 1
            else:
                self.carrinho [codigo] = {"quantidade": 1}
            self.atualizar_lista ()
        else:
            self.entrada_codigo.configure (placeholder_text = "Código inválido!")

    def remover_produto (self):
        codigo = self.entrada_codigo.get ().strip ()
        if codigo in self.carrinho:
            if self.carrinho [codigo]["quantidade"] > 1:
                self.carrinho [codigo]["quantidade"] -= 1
            else:
                del self.carrinho [codigo]
            self.atualizar_lista ()

    def atualizar_lista (self):
        for widget in self.frame_lista.winfo_children ():
            widget.destroy ()

        total = 0

        for codigo, dados in self.carrinho.items ():
            produto = self.produtos [codigo]
            nome = produto ["nome"]
            preco = produto ["preco"]
            quantidade = dados ["quantidade"]
            subtotal = preco * quantidade
            total += subtotal

            item_frame = ctk.CTkFrame (self.frame_lista)
            item_frame.pack (fill = "x", padx = 5, pady = 2)

            label_nome = ctk.CTkLabel (item_frame, text = f"{nome} (x{quantidade}) - R$ {subtotal:.2f}")
            label_nome.pack (side = "left", padx = 5)

            botao_mais = ctk.CTkButton (item_frame, text = "+", width = 30, command = lambda c = codigo: self.adicionar_quantidade (c))
            botao_mais.pack (side = "right", padx = 2)

            botao_menos = ctk.CTkButton (item_frame, text = "-", width = 30, command = lambda c = codigo: self.remover_quantidade (c))
            botao_menos.pack (side = "right", padx = 2)

        self.total_label.configure (text = f"Total: R$ {total:.2f}")

    def adicionar_quantidade (self, codigo):
        self.carrinho [codigo]["quantidade"] += 1
        self.atualizar_lista ()

    def remover_quantidade (self, codigo):
        if self.carrinho [codigo]["quantidade"] > 1:
            self.carrinho [codigo]["quantidade"] -= 1
        else:
            del self.carrinho [codigo]
        self.atualizar_lista ()

    def abrir_pagamento (self):
        if not self.carrinho:
            return

        janela_pagamento = ctk.CTkToplevel (self)
        janela_pagamento.title ("Pagamento")
        janela_pagamento.geometry ("400x300")

        label = ctk.CTkLabel (janela_pagamento, text = "Pagamento em andamento...", font = ("Arial", 16))
        label.pack (pady = 30)

        # Aqui você pode adicionar formas de pagamento, QR Code, etc.
        finalizar = ctk.CTkButton (janela_pagamento, text = "Finalizar", command = janela_pagamento.destroy)
        finalizar.pack (pady = 20)

if __name__ == "__main__":
    app = CarrinhoApp ()