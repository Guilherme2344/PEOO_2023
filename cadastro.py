class Cliente:
    def __init__(self, id, nome, idade):
        self.__id = id
        self.__nome = nome
        self.__idade = idade

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def __str__(self):
        return f'{self.__id} {self.__nome} {self.__idade}'


class NCliente:
    def __init__(self):
        self.__clientes = []

    def inserir(self, c):
        self.__clientes.append(c)

    def listar(self):
        return self.__clientes

    def atualizar(self, valor):
        for i in self.__clientes:
            if i.get_id() == valor.get_id():
                i.set_id(valor.get_id())
                i.set_nome(valor.get_nome())
                i.set_idade(valor.get_idade())

    def excluir(self, c):
        for i in self.__clientes:
            if i.get_id() == c:
                self.__clientes.remove(i)


class UI:
    def menu():
        print('0 - sair; 1 - inserir; 2 - listar; 3 - atualizar; 4 - excluir')
        return int(input())

    def main():
        op = 10
        x = NCliente()
        while op != 0:
            op = UI.menu()
            if op == 1:
                id = int(input('Informe seu id: '))
                nome = input('Informe seu nome: ')
                idade = int(input('Informe sua idade: '))
                a = Cliente(id, nome, idade)
                x.inserir(a)
                print('cliente cadastrado')
            if op == 2:
                for i in x.listar(): print(i)
            if op == 3:
                id = int(input('Informe seu id: '))
                nome = input('Informe o novo nome: ')
                idade = int(input('Informe sua nova idade: '))
                b = Cliente(id, nome, idade)
                x.atualizar(b)
                print('cliente atualizado')
            if op == 4:
                c = int(input('Insira o id do cliente: '))
                x.excluir(c)
                print('cliente excluído')


UI.main()
