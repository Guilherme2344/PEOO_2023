valor_1 = int(input())
valor_2 = int(input())
valor_3 = int(input())

soma_1 = (valor_1 * 2) + (valor_3 * 2)
soma_2 = (valor_2 * 2) + (valor_3 * 4)
soma_3 = (valor_1 * 4) + (valor_2 * 2)

valores = [soma_1, soma_2, soma_3]
print(min(valores))
