metros_correr, metros_total = map(int, input().split())
if metros_correr % metros_total == 0:
    print('0')
else:
    print(metros_correr % metros_total)
