from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def ferver_agua(self):
        print("1. Fervendo agua a 100 graus Celsius")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

    def preparar(self):
            print(f"-"*10, 'Iniciando Preparo', "-"*10)
            self.ferver_agua()
            self.misturar()
            self.servir()


class Cafe(BebidaQuente):

    def misturar(self):
        print("2. Passando agua pressurizada pelo pó de café moido")
    def servir(self):
        print("3. Servindo em xicara pequena")