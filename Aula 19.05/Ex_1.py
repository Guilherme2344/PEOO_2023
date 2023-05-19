class Pais:
    def __init__(self, nome, populacao, area):
        self.__nome = ''
        self.__populacao = 0
        self.__area = 0
        self.set_nome(nome)
        self.set_populacao(populacao)
        self.set_area(area)
        
    def set_nome(self, nome):
        if len(nome) != 0 and nome.isalpha() == True: self.__nome = nome
        else: raise SyntaxError()

    def set_populacao(self, populacao):
        if populacao >= 0: self.__populacao = populacao
        else: raise ValueError()

    def set_area(self, area):
        if area >= 0: self.__area = area
        else: raise ValueError()

    def get_nome(self):
        return self.__nome
    
    def get_populacao(self):
        return self.__populacao
    
    def get_area(self):
        return self.__area
    
    def densidade(self):
        self.__densidade = self.__populacao / self.__area
        return self.__densidade
    
    def __str__(self):
        return f'{self.__nome} tem a maior densidade demográfica: {self.__densidade} hab/km². População = {self.__populacao} hab e Área = {self.__area} km²'
    

class UI:
    @staticmethod
    def main():
        p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = map(str, input('Digite 10 nomes de países: ').split())
        pop1, pop2, pop3, pop4, pop5, pop6, pop7, pop8, pop9, pop10 = map(int, input('Digite o total de habitantes de cada país: ').split())
        a1, a2, a3, a4, a5, a6, a7, a8, a9, a10 = map(int, input('Digite a área ocupada por cada país: ').split())
        x1 = Pais(p1, pop1, a1)
        x2 = Pais(p2, pop2, a2)
        x3 = Pais(p3, pop3, a3)
        x4 = Pais(p4, pop4, a4)
        x5 = Pais(p5, pop5, a5)
        x6 = Pais(p6, pop6, a6)
        x7 = Pais(p7, pop7, a7)
        x8 = Pais(p8, pop8, a8)
        x9 = Pais(p9, pop9, a9)
        x10 = Pais(p10, pop10, a10)
        valores = [x1.densidade(), x2.densidade(), x3.densidade(), x4.densidade(), x5.densidade(), x6.densidade(), x7.densidade(), x8.densidade(), x9.densidade(), x10.densidade()]
        if x1.densidade() == max(valores): print(x1)
        elif x2.densidade() == max(valores): print(x2)
        elif x3.densidade() == max(valores): print(x3)
        elif x4.densidade() == max(valores): print(x4)
        elif x5.densidade() == max(valores): print(x5)
        elif x6.densidade() == max(valores): print(x6)
        elif x7.densidade() == max(valores): print(x7)
        elif x8.densidade() == max(valores): print(x8)
        elif x9.densidade() == max(valores): print(x9)
        else: print(x10)


UI.main()
