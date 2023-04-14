maior = -1
for valor in range(100):
  X = int(input())
  if X > maior:
    maior = X
    posicao = valor
print(maior)
print(posicao+1)
