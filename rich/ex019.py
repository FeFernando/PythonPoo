from rich import print
from time import sleep


class Livro:


    def __init__(self, nome, paginas):
        self.nome = nome
        self.paginas = paginas
        self.pagina_atual = 0

    def avancar_paginas(self, num):

        for i in range(num):
            if self.pagina_atual >= self.paginas:
                print(f'[red]Você chegou ao fim do livro[/]')
                break
            self.pagina_atual += 1
            print(f'Página {self.pagina_atual}', end=' ')
            sleep(0.5)









l1 = Livro('O corvo', 20)
l1.avancar_paginas(10)
l1.avancar_paginas(2)