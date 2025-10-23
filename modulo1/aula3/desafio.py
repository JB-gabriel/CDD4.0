nota1=float(input("nota 1: "))
nota2=float(input("nota 2: "))
nota3=float(input("nota 3: "))
media=(nota1+nota2+nota3)/3
if media>=7.0:
    print("aprovado")
elif media>=4.0:
    print("reculperação")
else:
    print("reprovado")