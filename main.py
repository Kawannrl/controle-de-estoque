import customtkinter as ctk

ctk.set_appearance_mode ("dark")
ctk.set_default_color_theme ("dark-blue")

class StockMasterApp (ctk.CTk): 
    def __init__ (self):
        super ().__init__ ()

        self.title ("StockMaster - Controle de Estoques")
        self.geometry ("500x300")

        self.label = ctk.CTkLabel (self, text = "Olá, ", font = ctk.CTkFont (size = 20, weight = "bold"))
        self.label.pack (pady = 20)

        self.botao = ctk.CTkButton(self, text = "Clique Aqui", command = self.clicado)
        self.botao.pack (pady = 10)

    def clicado (self):
        self.label.configure (text = "Botão foi clicado!")

if __name__ == "__main__":
    app = StockMasterApp ()
    app.mainloop ()
