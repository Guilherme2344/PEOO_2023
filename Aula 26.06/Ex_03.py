import enum

class Dias(enum.Enum):
    SEGUNDA = 1
    TERÇA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5


class Turno(enum.Enum):
    MATUTINO = 1
    VESPERTINO = 2
    NOTURNO = 3


class Estagiario:
    def __init__(self, nome, cpf, telefone, dias, turno):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__dias = dias
        self.__turno = turno
        self.set_dias(dias)
        self.set_turno(turno)

    def set_dias(self, valor):
        if valor >= 1 and valor <= 5: self.__dias = valor
        else: raise ValueError()

    def set_turno(self, valor):
        if valor >= 1 and valor <= 3: self.__turno = valor
        else: raise ValueError()

    def get_dias(self):
        return self.__dias
    
    def get_turno(self):
        return self.__turno
    
    def __str__(self):
        return f'Nome = {self.__nome}; CPF = {self.__cpf}\nTelefone = {self.__telefone}; Dias = {self.__dias.name}; Turno = {self.__turno.name}'
    

class UI:
    def main():
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu cpf no formato 000.000.000-00: ')
        telefone = input('Digite seu telefone no formato (00) 00000-0000: ')
        dias = Dias(int(input('Digite 1 para Segunda; 2 para Terça; 3 para Quarta; 4 para Quinta; 5 para Sexta: ')))
        turno = Turno(int(input('Digite 1 para Matutino; 2 para Vespertino; 3 para Noturno: ')))
        x = Estagiario(nome, cpf, telefone, dias, turno)
        print(x)


UI.main()
