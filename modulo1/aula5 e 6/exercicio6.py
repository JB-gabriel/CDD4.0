lista_numero = []
for i in range(5):
    numero=input(f"Digite o {i+1}º número: ")

    lista_numero.append(numero)

print(f"Lista na ordem de entrada:{lista_numero}")


print("Lista com a exibição invertida:", lista_numero[::-1])
