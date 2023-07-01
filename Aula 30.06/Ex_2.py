class Esporte:
    def __init__(self, nome, horarios, mensalidade):
        self.__nome = nome
        self.__horarios = horarios
        self.__mensalidade = mensalidade

    def get_mensalidade(self):
        return self.__mensalidade

    def __str__(self):
        return f'{self.__nome}; {self.__horarios}; {self.__mensalidade}'
    

class Academia:
    def __init__(self, nome, endereco):
        self.__nome = nome
        self.__endereco = endereco
        self.__esportes = []

    def inserir(self, esporte):
        self.__esportes.append(esporte)

    def listar(self):
        return self.__esportes
    
    def media_mensal(self):
        for i in range(len(self.__esportes)):
            valores = []
            for j in self.__esportes:
                valores.append(j.get_mensalidade())
            self.__media = sum(valores) / len(self.__esportes)
        return self.__media
    
    def __str__(self):
        return f'A média é igual a R$ {self.__media:.2f}'
    

x = Esporte('futebol', 'nhnhbh', 200)
y = Esporte('basquete', 'hyhuhyuhu', 100)
z = Esporte('taco', 'nuhygy', 50)
a = Academia('A', 'nhinyihg')
a.inserir(x)
a.inserir(y)
a.inserir(z)
a.media_mensal()
print(a)
