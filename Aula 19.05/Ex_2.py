class PeçaDominó:
    def __init__(self, lado_1_esquerda, lado_1_direita, lado_2_esquerda, lado_2_direita):
        self.__lado_1_esquerda = 0
        self.__lado_1_direita = 0
        self.__lado_2_esquerda = 0
        self.__lado_2_direita = 0
        self.set_lado_1_esquerda(lado_1_esquerda)
        self.set_lado_1_direita(lado_1_direita)
        self.set_lado_2_esquerda(lado_2_esquerda)
        self.set_lado_2_direita(lado_2_direita)

    def set_lado_1_esquerda(self, lado):
        if lado >= 0 and lado <= 6: self.__lado_1_esquerda = lado
        else: raise ValueError()

    def set_lado_1_direita(self, lado):
        if lado >= 0 and lado <= 6: self.__lado_1_direita = lado
        else: raise ValueError()

    def set_lado_2_esquerda(self, lado):
        if lado >= 0 and lado <= 6: self.__lado_2_esquerda = lado
        else: raise ValueError()

    def set_lado_2_direita(self, lado):
        if lado >= 0 and lado <= 6: self.__lado_2_direita = lado
        else: raise ValueError()

    def get_lado_1_esquerda(self):
        return self.__lado_1_esquerda
    
    def get_lado_1_direita(self):
        return self.__lado_1_direita
    
    def get_lado_2_esquerda(self):
        return self.__lado_2_esquerda
    
    def get_lado_2_direita(self):
        return self.__lado_2_direita
    
    def combinar(self):
        self.__domino = True
        if self.__lado_1_esquerda == self.__lado_2_esquerda:
            return self.__domino
        elif self.__lado_1_direita == self.__lado_2_direita:
            return self.__domino
        elif self.__lado_1_esquerda == self.__lado_2_direita:
            return self.__domino
        elif self.__lado_1_direita == self.__lado_2_esquerda:
            return self.__domino
        else:
            self.__domino = False 
            return self.__domino

    def __str__(self):
        return f'Situação dos dois lados = {self.__domino}'
    

class UI:
    @staticmethod
    def main():
        peca1_esq, peca_1_dir = map(int, input('Digite os valores dos dois lados da primeira peça: ').split())
        peca2_esq, peca_2_dir = map(int, input('Digite os valores dos dois lados da segunda peça: ').split())
        x = PeçaDominó(peca1_esq, peca_1_dir, peca2_esq, peca_2_dir)
        x.combinar()
        print(x)


UI.main()
