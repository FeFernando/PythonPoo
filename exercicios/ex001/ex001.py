#Declaração de Classe
class Gafanhoto():
    # Metodo construtor
    def __init__(self):
        #Atributos de instancias
        self.nome = ""
        self.idade = 0
    #Metodos de instancia
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f'O gafanhoto(a) {self.nome} tem {self.idade} anos'

#Declaração de Objeto

g1 = Gafanhoto()
g1.nome = 'Felipe'
g1.idade = 30
g1.aniversario()
print(g1.mensagem())