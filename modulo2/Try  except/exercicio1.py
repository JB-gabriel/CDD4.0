try:
    numbers=int(input("digite o primeiro numero: "))
    numbers2=int(input("digite o segundo numero: "))
    resultado=numbers/numbers2

except ZeroDivisionError:
    print("o valor 0 nao pode ser dividido")

except ValueError:
    print("digite um numero inteiro")

else:
    print(f" Resultado: {resultado}")
finally:
    print("---OPERAÇÃO REALIZADA COM SUCESSO---")