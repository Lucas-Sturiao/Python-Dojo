usuarios = [
    {"nome": "Lucas", "ativo": True,  "idade": 25},
    {"nome": "Ana",   "ativo": False, "idade": 30},
    {"nome": "João",  "ativo": True,  "idade": 17},
    {"nome": "Maria", "ativo": True,  "idade": 40}
]

def contar_usuarios_validos(usuarios):
    acumulador = 0 

    for usuario in usuarios:
        if usuario["ativo"] and usuario["idade"] >= 18:
           acumulador += 1
        
    return acumulador
print(contar_usuarios_validos(usuarios))