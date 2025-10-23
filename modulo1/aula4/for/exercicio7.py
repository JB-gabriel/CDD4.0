contador = 0
for valor in range(4):
    valor=int(input("digite um numero: "))
    if valor<0:
        contador += 1
print(contador)