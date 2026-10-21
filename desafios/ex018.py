from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self,titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas
    def analisar(self):
        qtd_carne = 0.40 * self.pessoas
        custo_pessoa = 82.40 * 0.40
        custo_total = custo_pessoa * self.pessoas
        print(Panel(f'Analisando [green]{self.titulo}[/] com [blue]{self.pessoas} convidados[/] \n'
              f'Cada participante comerá 0.4kg e cada kg custa R$82.40\n'
              f'Recomendo [blue]comprar {qtd_carne}kg[/] de carne\n'
              f'O custo total será de [green]R${custo_total:.2f}[/]\n'
              f'Cada pessoa pagará [yellow]R${custo_pessoa:.2f}[/] para participar'))



c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()

#400 gramas por pessoa
#Preço: R$82,40/kg