contador = 0
soma = 0
media = 0

while contador < 2:

    nota = float(input("digite a nota : "))

    if nota >= 0 and nota <= 10:
        soma = soma + nota
        contador = contador + 1
    else:
        print("valor invalido")

media = soma / contador
print(media)


refazer = input("digite s ou n para refazer : ")

if refazer == "s":
    soma = 0
    contador =0
    while contador < 2:
        nota = float(input("digite a nota : "))

        if nota >= 0 and nota <= 10:
            soma = soma + nota
            contador = contador + 1
        else:
            print("valor invalido")

    media = soma / contador
    print(media)

else:
    print("finalizado")