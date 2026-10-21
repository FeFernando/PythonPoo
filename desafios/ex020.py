class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick

    def add_favoritos(self, jogo):
        self.jogo = jogo
        lista_favoritos = []

        lista_favoritos.append(self.jogo)

j1 = Gamer ('Felipe', '12felipexd')
j1.add_favoritos('Elden Ring')
j1.add_favoritos('Valorant')
j1.add_favoritos('Call of duty')
print()