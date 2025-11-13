try:
    idade = int(input("Digite sua idade: "))
    print(f"Sua idade é {idade}.")
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")