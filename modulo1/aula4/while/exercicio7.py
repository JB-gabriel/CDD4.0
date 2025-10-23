contador=0
soma=0
media=0
while contador<2:
    nota=int(input("digite a nota : "))
    if nota>=0 and nota<=10:
        soma=soma+nota
        contador=contador+1
    else:
        print("valor invalido")

media=soma/contador
print(media)