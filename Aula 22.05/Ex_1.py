class Retangulo:
    def __init__(self, base, altura):
        self.__base = 0
        self.__altura = 0
        self.set_base(base)
        self.set_altura(altura)

    def set_base(self, valor):
        if valor >= 0: self.__base = valor
        else: raise ValueError()

    def set_altura(self, valor):
        if valor >= 0: self.__altura = valor
        else: raise ValueError()

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def calcular_area(self):
        self.__area = self.__base * self.__altura
        return self.__area

    def calcular_diagonal(self):
        self.__diagonal = (self.__base ** 2 + self.__altura ** 2)**0.5
        return self.__diagonal
    
    def __str__(self):
        return f'Área = {self.__area}; Diagonal = {self.__diagonal}'


class UI:
    @staticmethod
    def main():
        b = int(input('Digite o valor da base: '))
        h = int(input('Digite o valor da altura: '))
        retangulo = Retangulo(b, h)
        retangulo.calcular_area()
        retangulo.calcular_diagonal()
        print(retangulo)


UI.main()
