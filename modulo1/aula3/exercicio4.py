preco_gasolina = 5.80
preco_etanol = 4.90


tipo_combustivel = input("Digite o tipo de combustível (E-etanol, G-gasolina): ")

litros_vendidos = float(input("Digite o número de litros vendidos: "))

valor_total = 0

if tipo_combustivel == 'E':
    valor_total = litros_vendidos * preco_etanol
    print(f"O valor a ser pago pelo etanol é: R$ {valor_total:.2f}")
elif tipo_combustivel == 'G':
    valor_total = litros_vendidos * preco_gasolina
    print(f"O valor a ser pago pela gasolina é: R$ {valor_total:.2f}")
else:
    print("Tipo de combustível inválido. Por favor, digite 'E' ou 'G'.")

