usuarios = [
    {"nome": "Lucas", "ativo": True,  "idade": 25},
    {"nome": "Ana",   "ativo": False, "idade": 30},
    {"nome": "João",  "ativo": True,  "idade": 17},
    {"nome": "Maria", "ativo": True,  "idade": 40}
]


def contar_ativos(usuarios):
    contador = 0

    for usuario in usuarios:
        if not usuario["ativo"] or usuario["idade"] < 18:
            continue
        contador += 1
    return contador

print("O número de usuários ativos maiores de 18 anos é:", contar_ativos(usuarios))