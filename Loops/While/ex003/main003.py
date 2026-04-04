numeros = [3, -1, 5, 0, 8]
soma_positivos = 0
i = 0

while i < len(numeros):
    if numeros[i] < 0:
        i += 1
        continue
    elif numeros[i] == 0:
        break
    else:
        soma_positivos += numeros[i]

    i += 1
print("A soma dos números positivos é:", soma_positivos)