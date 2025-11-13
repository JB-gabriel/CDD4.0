try:
    minha_lista=[10,20,30]
    indice=int(input("digite o indice do numero: "))
    elemento=minha_lista[indice]
    print(elemento)
except IndexError:
    print("indice fora do alcance")

except ValueError:
    print("digite um numero inteiro")
