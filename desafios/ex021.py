from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor

    def escrever(self, msg):
        if self.cor == 'azul':
           print(f'[blue]{msg}[/]')
        elif self.cor == 'vermelho':
            print(f'[red]{msg}[/]')
        elif self.cor == 'verde':
            print(f'[green]{msg}[/]')
        else:
            print(msg)


c1 = Caneta('azul')
c2 = Caneta('vermelho')


c1.escrever('Ola mundo')
c2.escrever('Mensagem em vermelho')