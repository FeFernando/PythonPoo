from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self, nome, preco):
        self.nome =  nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f'{self.nome.center(30, ' ')}'
        conteudo += f'{'-' * 30}'
        precof = f'R${self.preco:.2f}'
        conteudo += f'{precof.center(30, '_').replace('.', ',')}'
        etiqueta = Panel(conteudo, title='Produto', width= 34)
        print(etiqueta)


p1 = Produto('Limão', 10.50)
p1.etiqueta()