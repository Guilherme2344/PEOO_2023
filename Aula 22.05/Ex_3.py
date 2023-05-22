class EquacaoGrau2:
    def __init__(self, a, b, c):
        self.__a = 1
        self.__b = 0
        self.__c = 0
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

    def set_a(self, valor):
        if valor != 0: self.__a = valor
        else: raise ValueError()

    def set_b(self, valor):
        self.__b = valor

    def set_c(self, valor):
        self.__c = valor

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c
    
    def delta(self):
        self.__delta = self.__b **2 - 4 * self.__a * self.__c
        return f'Delta = {self.__delta}'
    
    def TemRaizesReais(self):
        if self.__delta < 0: return f'Raízes Reais? {False}'
        else: return f'Raízes Reais? {True}'

    def equacao(self):
        self.__delta = self.__b ** 2 - 4 * self.__a * self.__c
        self.__x1 = (-self.__b + (self.__delta)**0.5) / 2 * self.__a
        self.__x2 = (-self.__b - (self.__delta)**0.5) / 2 * self.__a
        return self.__x1, self.__x2
    
    def __str__(self):
            if self.__delta < 0: return 'Não há raízes reais'
            else: return f'X1 = {self.__x1} e X2 = {self.__x2}'


class UI:
    @staticmethod
    def main():
        a = int(input('Digite o valor de a: '))
        b = int(input('Digite o valor de b: '))
        c = int(input('Digite o valor de c: '))
        equa = EquacaoGrau2(a, b, c)
        print(equa.delta())
        print(equa.TemRaizesReais())
        equa.equacao()
        print(equa)


UI.main()
