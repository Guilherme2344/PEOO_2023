class Equacao2:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def delta(self):
        self.__delta = self.__b ** 2 - 4*self.__a*self.__c
        return self.__delta

    def tem_raizes_reais(self):
        if self.__delta >= 0: return 'Raízes Reais'
        else: return 'Raízes Não Reais'

    def raiz_1(self):
        x = (-self.__b + self.__delta ** 0.5) / (2 * self.__a)
        return x

    def raiz_2(self):
        x = (-self.__b - self.__delta ** 0.5) / (2 * self.__a)
        return x

    def __str__(self):
        return f'a = {self.__a}; b = {self.__b}; c = {self.__c}'
