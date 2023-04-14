entrada = input().split()
A = int(entrada[0])
B = int(entrada[1])
if A%B == 0 or B%A == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
