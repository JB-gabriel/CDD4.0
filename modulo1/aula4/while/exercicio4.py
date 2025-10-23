qtd_alunos=int(input("digite quantos alunos: "))
contador=0
soma=0
while contador<qtd_alunos:
    aluno=int(input("digite a nota do aluno: "))
    contador=contador+1
    soma=soma+aluno
    media=soma/contador
print(media)