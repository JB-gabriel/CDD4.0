op = 2

match op:
    case 1:
        titulo = "Opção 1"
    case 2:
        titulo = "Opção 2"
    case 3:
        titulo = "Opção 3"
    case _:
        titulo = "Opção Errada"

print(f"Título: {titulo}")