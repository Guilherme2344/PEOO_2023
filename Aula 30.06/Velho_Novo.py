from datetime import datetime

class Jogador:
    def __init__(self, nome, data):
        self.__nome = nome
        self.__data = data

    def get_data(self):
        return self.__data
    
    def get_nome(self):
        return self.__nome
    
    def __str__(self):
        return f'{self.__nome}; {self.__data}'
    

class Time:
    def __init__(self, nome):
        self.__nome = nome
        self.__jogadores = []

    def inserir(self, jogador):
        self.__jogadores.append(jogador)

    def listar(self):
        return self.__jogadores
    
    def idade(self):
        for i in range(len(self.__jogadores)):
            time = []
            hoje = datetime.today()
            for j in self.__jogadores:
                nome = j.get_nome()
                data = j.get_data()
                data_format = datetime.strptime(data, '%d/%m/%Y')
                idade = ((hoje - data_format).days) / 365
                time.append([nome, idade])
            self.__velho = time[0]
            self.__novo = time[1]
            for jogador in time:
                if jogador[1] > self.__velho[1]:
                    self.__velho = jogador
                elif jogador[1] < self.__novo[1]:
                    self.__novo = jogador
            return self.__velho, self.__novo
    

    def __str__(self):
        return f'O jogador mais velho é {self.__velho[0]} com {self.__velho[1]:.2f} anos\nO jogador mais novo é {self.__novo[0]} com {self.__novo[1]:.2f} anos'


x = Jogador('gui', '19/09/2008')
y = Jogador('carla', '10/08/2007')
z = Jogador('carlos', '10/08/2005')
w = Jogador('gute', '20/06/2002')
a = Time('abc')
a.inserir(x)
a.inserir(y)
a.inserir(z)
a.inserir(w)
a.idade()
print(a)
