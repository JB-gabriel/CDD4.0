senha=123456
contador=0

while True:
    numero = int(input("digite a senha : "))
    if senha==numero:
        print("logado")
        break
    elif senha != numero:
        contador+=1
        print("Senha errada, tentativa :", contador)
    if contador == 3:
        print("Conta bloqueada")
        break
