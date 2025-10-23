list_nomes = []
list_senhas = []
quantidade = 5

for i in range(quantidade):
    print(f"\nUsuário {i + 1}:")

    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    list_nomes.append(nome)
    list_senhas.append(senha)

for i, nome_usuario in enumerate(list_nomes):

    senha_correspondente = list_senhas[i]


    print(f"| {i+1:<7} | {nome_usuario:<15} | {senha_correspondente:<7} |")