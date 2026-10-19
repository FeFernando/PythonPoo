from rich.table import Table
from rich import print

class Produto:
    def __init__(self, nome, preco):
        self.nome =  nome
        self.preco = preco

    def etiqueta(self):
        tabela = Table(title='Produto', show_lines=True)
        tabela.add_row(self.nome)
        tabela.add_row(str(self.preco))
        print(tabela)

p1 = Produto('Limão', 10.50)
p1.etiqueta()