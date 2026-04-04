tentativas = 5
pin = "9999"

while tentativas > 0:
    senha = input("Digite sua senha:")
    if senha == pin:
        print("Acesso liberado!")
        break
    else:
        tentativas -= 1
        print("Senha incorreta, tentativas restantes:", tentativas)

if tentativas == 0:
    print("Acesso bloqueado.")