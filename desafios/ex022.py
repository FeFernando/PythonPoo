from rich import print
from rich.panel import Panel

class ControleRemoto:
    def __init__(self, botao):
        self.botao = botao

    def power(self, comando):
        if comando == '@':
            Panel(title='TV', print(''))