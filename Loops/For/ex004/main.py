temperaturas = [22, 25, 19, 30, 28, 15]
acumulador = 0

for temperatura in temperaturas:
    if temperatura <= 25:
        continue
    acumulador += 1

print("O número de temperaturas maiores que 25°C é:", acumulador)