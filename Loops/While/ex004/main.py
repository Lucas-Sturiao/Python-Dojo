saldo = 1000

while saldo >= 0:
    if saldo >= 200:
        saldo -= 200
        print("Saque de R$200,00 efetuado com sucesso! Saldo restante:", saldo) 
    else:
        print("Saldo insuficiente.")
        break