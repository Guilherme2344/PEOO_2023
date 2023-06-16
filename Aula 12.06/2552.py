n, m = map(int, input().split())
matriz = []
linha = [0] * (m + 2)
for k in range(n):
    linha = list(map(int, input().split()))
    linha.insert(0, 0)
    linha.append(0)
    matriz.append(linha)
linha = [0] * (m + 2)
matriz.append(linha)
print(matriz)
