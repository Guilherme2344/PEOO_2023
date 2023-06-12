valor_inteiro = int(input())
for valor in range(10):
  vezes = valor_inteiro*2
  if valor == 0:
    print(f'N[{valor}] = {valor_inteiro}')
  else:
    valor_inteiro = vezes
    print(f'N[{valor}] = {vezes}')
