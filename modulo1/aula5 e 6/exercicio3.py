nomes_alunos = []
NUMERO_DE_ALUNOS = 5

for i in range(NUMERO_DE_ALUNOS):
    nome = input(f"Digite o nome do aluno {i + 1}: ")

    nomes_alunos.append(nome)


for indice in range(len(nomes_alunos)):
    print(f"Posição no Array (indice): {indice} | nome do aluno: {nomes_alunos[indice]}")

busca = input("busque o aluno: ")
if busca in nomes_alunos:
        print(f"{busca}: {nomes_alunos[indice]}foi o aluno numero, {indice} matriculado")
else:
        print("Nenhum aluno encontrado")


