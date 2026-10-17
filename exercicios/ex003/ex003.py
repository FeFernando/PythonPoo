class ContaBancaria:
    """Cria uma conta bancaria"""
    def __init__(self, id, nome, saldo = 0): #Metodo Construtor
        self.id = id
        self.titular = nome
        self.saldo = saldo
    def __str__(self):
        return f'UserId:{self.id}  Nome:{self.titular}  Saldo:{self.saldo} '

    def deposito(self, valor):
        self.saldo += valor
    def saque(self, valor):
        if valor > self.saldo:
            print( f'Saque negado, a conta tem {self.saldo}')
        else:
            self.saldo -= valor
            print( f'Saque de {valor} feito')


c1 = ContaBancaria(1234, 'Felipe', 10000)
c1.deposito(50)
c1.saque(11000)
print(c1)