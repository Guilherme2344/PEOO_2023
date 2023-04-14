N = int(input())
valor1 = 0
valor2 = 1
for i in range(N):
  if i == N-1:
    print(valor1)
  else:
    print(valor1, end=" ")
  valor3 = valor1 + valor2
  valor1 = valor2
  valor2 = valor3
