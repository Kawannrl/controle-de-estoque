import customtkinter as ctk

class main():
    def __init__(self):
        super().__init__()
        
        self.title("StockMaster - Controle de Estoques")
        self.geometry("500x300")
        
        self.label = ctk.CtkLabel(self, text = "Olá, ", font = ctk.CtkFont(size = 20, weight = "bold"))
        self.label.pack(pady = 20)
        
        self.botao = ctk.CtkButton(self, text = "Clique Aqui", command = self.clicado)
        self.botao.pack(pady = 10)
        
    def clicado(self):
        self.label.configure(text = "Botão foi clicado!")
        
        
        
        
if __name__ == "__main__":
    app = main()
    app.mainloop()