#Declaração de Classe
class Gafanhoto():
    """
    Essa classe cria um gafanhoto que tem nome e idade
    Para criar uma nova pessoa use:
    variavel = Gafanhoto(nome, idade)
    """
    # Metodo construtor
    def __init__(self, n='', i=0):
        #Atributos de instancias
        self.nome = n
        self.idade = i
    #Metodos de instancia
    def aniversario(self):
        self.idade += 1
    def __str__(self):#Dunder Method
        return f'O gafanhoto(a) {self.nome} tem {self.idade} anos'

#Declaração de Objeto

g1 = Gafanhoto("MARIA", 20)
#g1.aniversario()
print(g1)

#print(g1.__doc__) #Dunder Attribute