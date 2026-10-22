from rich import print
from rich.panel import Panel

lista_favoritos = []

class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick

    def add_favoritos(self, jogo):

        self.jogo = jogo

        lista_favoritos.append(self.jogo)

j1 = Gamer ('Felipe', '12felipexd')
j1.add_favoritos('Elden Ring')
j1.add_favoritos('Valorant')
j1.add_favoritos('Call of duty')
print(Panel(
    f'Nome real: {j1.nome}\n\n'
    f':video_game: Jogos favoritos:\n'
    f'[blue]:video_game:{chr(10).join(sorted(lista_favoritos))}[/]',
    title=f'Jogador {j1.nick}'
))
