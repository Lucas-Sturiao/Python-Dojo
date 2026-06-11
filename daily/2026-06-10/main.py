estoque = [
    {"nome": "Teclado", "quantidade": 10},
    {"nome": "Mouse", "quantidade": 5},
    {"nome": "Monitor", "quantidade": 3}
]

print("==== Sistema de controle de Estoque ====")
print("1. Listar produtos")
print("2. Adicionar produto")
print("3. Atualizar quantidade")
print("4. Remover produto")
print("5. Sair")

while True:
    number = input("Escolha uma das opções: ")

    if number == "1":
        print(estoque)

    elif number == "2":
        nome = input("Digite o nome do produto: ")
        quantidade = input("Digite a quantidade do produto: ")

        novo = {"nome": nome, "quantidade": quantidade}

        estoque.append(novo)
        print(f"Produto {nome} adicionado ao estoque!")

    elif number == "3":
        item = input("Digite o item da lista voce deseja alterar: ")
        for produto in estoque:
            if item == produto["nome"]:
                nova_quantidade = int(input("Digite a nova quantidade do produto: "))
                produto["quantidade"] = nova_quantidade
                print(estoque)
                
            else:
                print("Produto inexistente.")
        print("Em construção")

    elif number == "4":
        print("Em construção")

    elif number == "5":
        print("Saindo...")
        break

    else:
        print("Opção inexistente!")