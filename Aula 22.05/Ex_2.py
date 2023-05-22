class Frete:
    def __init__(self, massa, distancia):
        self.__massa = 0
        self.__distancia = 0
        self.set_massa(massa)
        self.set_distancia(distancia)

    def set_massa(self, valor):
        if valor >= 0: self.__massa = valor
        else: raise ValueError()

    def set_distancia(self, valor):
        if valor >= 0: self.__distancia = valor
        else: raise ValueError()

    def get_massa(self):
        return self.__massa

    def get_distancia(self):
        return self.__distancia

    def calcular_frete(self):
        self.__frete = 0.1 * self.__massa * self.__distancia
        return self.__frete
    
    def __str__(self):
        return f'Frete = R$ {self.__frete:.2f}'


class UI:
    @staticmethod
    def main():
        kg = int(input('Digite o valor da massa: '))
        km = int(input('Digite o valor da distância: '))
        frete = Frete(kg, km)
        frete.calcular_frete()
        print(frete)


UI.main()
