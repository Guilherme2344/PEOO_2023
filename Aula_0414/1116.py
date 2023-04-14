casos = int(input())
for i in range(casos):
    try:
        valor_1, valor_2 = map(float, input().split())
        divisão = valor_1 / valor_2
        print(f'{divisão:.1f}')
    except ZeroDivisionError:
        print('divisao impossivel')
