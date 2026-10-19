from rich import print



class Funcionario:
    def __init__(self, nome, setor, cargo): #Metodo construtor
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
n1 = Funcionario('Felipe', 'Desenvolvimento', 'Analista' )
print(f':handshake: Ola! sou {n1.nome}, {n1.cargo} do setor de {n1.setor} da empresa')

