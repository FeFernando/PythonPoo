from rich import print
from rich.table import Table

dicionario = [
    {"nome": "arroz", "preco": 25.90},
    {"nome": "feijao", "preco": 8.50},
    {"nome": "macarrao", "preco": 5.99},
    {"nome": "oleo", "preco": 7.49},
    {"nome": "acucar", "preco": 4.79},
    {"nome": "cafe", "preco": 18.90},
    {"nome": "leite", "preco": 5.50},
    {"nome": "tomate", "preco": 6.99},
    {"nome": "batata", "preco": 4.50},
    {"nome": "suco", "preco": 9.90}
]



tabela = Table(title='Tabela de preços')

tabela.add_column("Nome")
tabela.add_column("Preço")

for i in dicionario:
    tabela.add_row(i["nome"], str(i["preco"]))

print(tabela)