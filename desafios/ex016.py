from rich import print
from rich import inspect



class Funcionario:
    #Atributos de classe
    empresa = 'Curso em video'

    def __init__(self, nome, setor, cargo): #Metodo construtor
        #Atributos de intancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    def apresentacao(self):
        return f'Olá sou {self.nome}, {self.cargo} no setor de {self.setor} na empresa {Funcionario.empresa}'


n1 = Funcionario('Felipe', 'Desenvolvimento', 'Analista' )
#inspect(n1)
print(n1.apresentacao())

