lista = [4, -2, 7, 0, 10]


def soma_positivos(lista):
    total = 0

    for numero in lista:
        if numero < 0:
            continue
        elif numero == 0:
            break
        else:
            total += numero

    return total
print(soma_positivos(lista))