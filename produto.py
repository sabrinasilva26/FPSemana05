class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco 
        self.quantidade = quantidade
    

    def adicionar_stock(self, quantidade):
            
            if quantidade > 0:
                self.quantidade+=quantidade
                print(1)
            else:
                print(0)

    def vender(self,quantidade):
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
            print(1)
        else:
            print(0)

    def exibir_info(self):
         print(f"{self.nome} {self.preco} {self.quantidade} ")

produto1 = Produto("Vaso", 19.99, 100)
produto1.adicionar_stock(-20)
produto1.adicionar_stock(20)
produto1.vender(50)
produto1.vender(100)
produto1.exibir_info() 


   


