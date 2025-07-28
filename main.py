import customtkinter as ctk
from interface import LoginApp
import database

ctk.set_appearance_mode ("dark")
ctk.set_default_color_theme ("dark-blue")

class StockMasterApp (ctk.CTk): 
    def __init__ (self):
        super ().__init__ ()

        self.title ("StockMaster - Controle de Estoques")
        self.geometry ("300x200")

        self.label = ctk.CTkLabel (self, text = "Bem Vindo ", font = ctk.CTkFont (size = 20, weight = "bold"))
        self.label.pack (pady = 20)

        self.botao = ctk.CTkButton(self, text = "Iniciar", command = self.abrir_login)
        self.botao.pack (pady = 10)

    def abrir_login (self):
        self.destroy ()
        LoginApp ()

if __name__ == "__main__":
    database.conectar_banco()
    database.criar_tabelas()
    app = StockMasterApp ()
    app.mainloop ()
