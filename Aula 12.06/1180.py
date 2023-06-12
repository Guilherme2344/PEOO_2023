valor = int(input())
vetor = list(map(int, input().split()))
menor = min(vetor)
posicao = 0
for i in range(valor):
  if vetor[i] == menor:
    posicao = i
print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
