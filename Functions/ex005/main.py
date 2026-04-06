produtos = [
    {"nome": "Teclado", "estoque": 10},
    {"nome": "Mouse",   "estoque": 0},
    {"nome": "Monitor", "estoque": 5},
    {"nome": "Cabo",    "estoque": 0}
]

def contar_estoque(produtos):
    contador = 0
    for produto in produtos:
        if produto["estoque"] == 0:
            continue
        contador += 1
    return contador
print("O número de estoques é de:", contar_estoque(produtos))