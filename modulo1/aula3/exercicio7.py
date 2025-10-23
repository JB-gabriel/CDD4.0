nome=input("digite seu nome: ")
for c in nome:
    if c == nome[-1] :
        print(c)
    else:
        print(c, end=" , ")

