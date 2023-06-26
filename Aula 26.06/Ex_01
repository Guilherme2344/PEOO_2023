from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

    def idade(self):
        hoje = datetime.now()
        tempo = (hoje - self.__nascimento)
        self.__total_dias = tempo.days // 365
        return self.__total_dias

    def __str__(self):
        return f'Nome = {self.__nome}; CPF = {self.__cpf}; Telefone = {self.__telefone}; Idade = {self.__total_dias} anos'


class UI:
    def main():
        nome = input('Digite o nome: ')
        cpf = input('Digite o cpf no formato 000.000.000-00: ')
        telefone = input('Digite o telefone no formato (00) 00000-0000: ')
        nascimento = datetime.strptime(input('Digite a data de nascimento no formato dd/mm/aaaa: '), '%d/%m/%Y')
        x = Paciente(nome, cpf, telefone, nascimento)
        x.idade()
        print(x)

    
UI.main()
