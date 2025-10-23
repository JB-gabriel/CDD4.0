nome_aluno=[]
alunos=5
CONTADOR=0
print("---cadstro dos alunos---")
for i in range(alunos):
    nome=input("Digite o nome do aluno: ")
    CONTADOR=CONTADOR+1
    nome_aluno.append(nome)

print("---cadstro dos alunos---")
print(f"lista de alunos:{nome_aluno}")

print("\nNomes dos alunos:")
for nome in nome_aluno:
    print(f"- {nome}")
