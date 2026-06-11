pedidos = [
    {"id": 1, "valor": 50, "pago": True},
    {"id": 2, "valor": 120, "pago": False},
    {"id": 3, "valor": 80,  "pago": True},
    {"id": 4, "valor": 30,  "pago": True}
]

total = 0

for pedido in pedidos:
    if not pedido["pago"]:
        continue
    total += pedido["valor"]
    print(total)