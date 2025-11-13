def Adicao():
    numero1=int(input("Digite um numero: "))
    numero2=int(input("Digite outro numero: "))
    soma=numero1+numero2
    print(soma)

def Exercicio1():
    n=int(input("Digite um numero: "))
    for i in range(1, n + 1):
         print(str(i) * i)

def Exercicio2():
    n=int(input("Digite um numero: "))
    for i in range(1, n + 1):
         for x in range(1, i + 1):
            print(x, end=" ")
         print()
def Exercicio3():
    palavra = "O rato roeu a roupa do rei de Roma"
    contador = 0

    vogais = 'aeiou'

    for i in palavra:


        if i.lower() in vogais:
            contador = contador + 1


    print(f"O número de vogais é: {contador}")



