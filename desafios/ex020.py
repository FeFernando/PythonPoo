from rich import print
from rich.panel import Panel



class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, jogo):

        self.jogo = jogo
        self.favoritos.append(self.jogo)

    def ficha(self):
        conteudo = f'Nome real: {self.nome}\n'
        conteudo += f'Jogos favoritos'
        for num, game in enumerate(self.favoritos):
            conteudo += f'\n:video_game: {game}'
        painel = Panel(conteudo,   title=f'Jogador {j1.nick}')

        print(painel)

j1 = Gamer ('Felipe', '12felipexd')
j1.add_favoritos('Elden Ring')
j1.add_favoritos('Valorant')
j1.add_favoritos('Call of duty')
j1.ficha()
