def formatar_texto(nome):
    palavras = nome.split()
    resultado = ''
    for palavra in palavras:
        resultado += palavra.capitalize()
    return resultado


print(formatar_texto('GUILHERME CRISTIANO MEDEIROS SILVA'))
