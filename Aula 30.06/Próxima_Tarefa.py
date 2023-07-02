from datetime import datetime

class Pessoa:
    def __init__(self, nome, tarefa, data):
        self.__nome = nome
        self.__tarefa = tarefa
        self.__data = data

    def get_nome(self):
        return self.__nome
    
    def get_data(self):
        return self.__data
    
    def get_tarefa(self):
        return self.__tarefa
    
    def __str__(self):
        return f'{self.__nome}; {self.__tarefa}; {self.__data}'
    

class Agenda:
    def __init__(self):
        self.__agenda = []

    def inserir(self, dia):
        self.__agenda.append(dia)

    def listar(self):
        return self.__agenda
    
    def proximo(self):
        for i in range(len(self.__agenda)):
            lista = []
            lista_data = []
            hoje = datetime.today()
            for j in self.__agenda:
                nome = j.get_nome()
                tarefa = j.get_tarefa()
                data = j.get_data()
                data_format = datetime.strptime(data, '%d/%m/%Y')
                proximo = (data_format - hoje).days
                lista.append([nome, tarefa, proximo])
                lista_data.append(data_format)
            self.__proximo = lista[0]
            for p in lista:
                if p[2] < self.__proximo[2]:
                    self.__proximo = p
            self.__data_prox = lista_data[0]
            for x in lista_data:
                if x < self.__data_prox:
                    self.__data_prox = x
            self.__data_prox = datetime.strftime(self.__data_prox, '%d/%m/%Y')
            return self.__proximo, self.__data_prox
    
    def __str__(self):
        return f'A próxima tarefa é de:\nNome: {self.__proximo[0]}; Tarefa: {self.__proximo[1]}; Data: {self.__data_prox}'
    

x = Pessoa('gui', 'escovar os dentes', '10/08/2023')
y = Pessoa('carla', 'pentear o cabelo', '19/09/2023')
z = Pessoa('carlos', 'arrumar a cama', '10/07/2023')
a = Agenda()
a.inserir(x)
a.inserir(y)
a.inserir(z)
a.proximo()
print(a)
