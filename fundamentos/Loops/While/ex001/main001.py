pin = "4321"
tentativas = 3
acertou = False

while tentativas > 0 and not acertou:
    senha = input("Digite sua senha:")
    if senha == pin:
        acertou = True
        print("Acesso liberado!")
    else:
        tentativas = tentativas - 1
        print("Senha incorreta. Tentativas restantes:", tentativas)
    
if tentativas == 0: #ou: if not acertou:
    print("Acessso bloqueado") 