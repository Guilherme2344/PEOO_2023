def aprovado(nota_1, nota_2):
    média = (nota_1 + nota_2) / 2
    if média >= 60:
        mensagem = 'verdadeiro'
        return mensagem
    else:
        mensagem = 'falso'
        return mensagem


print(aprovado(59, 59))
