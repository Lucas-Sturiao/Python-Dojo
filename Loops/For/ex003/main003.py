pedidos = [
    {"id": 1, "valor": 100, "status": "pago"},
    {"id": 2, "valor": 50,  "status": "cancelado"},
    {"id": 3, "valor": 80,  "status": "pago"},
    {"id": 4, "valor": 30,  "status": "pago"},
]
soma_pagos = 0


for pedido in pedidos:
    if pedido["status"] == "pago":
        soma_pagos += pedido["valor"]
    else:
        break
print("O valor total dos pedidos pagos antes do cancelamento é:", soma_pagos)