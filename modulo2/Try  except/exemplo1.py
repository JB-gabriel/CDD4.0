try:
    x = 10
    y = int(input("Digite um número para dividir 10: ")) # Solicita a entrada do usuário
    resultado = x / y
    print(f"O resultado é: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero. Tente novamente com outro número.")

print("O programa continua aqui (não quebrou).")