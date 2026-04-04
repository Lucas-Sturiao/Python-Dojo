usuarios = [
    {"nome": "Lucas", "ativo": True,  "idade": 25},
    {"nome": "Ana",   "ativo": False, "idade": 30},
    {"nome": "João",  "ativo": True,  "idade": 17},
    {"nome": "Maria", "ativo": True,  "idade": 40}
]

total_users = 0

for usuario in usuarios:
    if not usuario["ativo"]:
        continue
    if usuario["idade"] >= 18:
        total_users = total_users + 1
print(total_users)


for usuario in usuarios:
    if usuario["ativo"] == True and usuario["idade"] >= 18:
        total_users = total_users + 1
print(total_users)