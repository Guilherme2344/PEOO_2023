linhas = 12
colunas = 12
matriz = []
opcao = input()
for linha in range(linhas):
    for coluna in range(colunas):
        matriz[linha][coluna] = float(input())

soma = 0
contador = 1
for linha in range(linhas):
    for coluna in range(colunas):
        if coluna > linha:
            soma += matriz[linha][coluna]
            contador += 1

if opcao == 'S': print(f'{soma:.1f}')
elif opcao == 'M': print(f'{soma/contador:.1f}')
