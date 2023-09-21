import json
from datetime import datetime

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    def set_id(self, id):
        self.__id = id

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_fone(self, fone):
        self.__fone = fone

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def __str__(self):
        return f'{self.__id}; {self.__nome}; {self.__email}; {self.__fone}'

    
class NCliente:
    __clientes = []

    @classmethod
    def inserir(cls, obj):
        NCliente.abrir()
        id = 0
        for cliente in cls.__clientes:
            if cliente.get_id() > id: id = cliente.get_id()
        obj.set_id(id + 1)
        cls.__clientes.append(obj)
        NCliente.salvar()

    @classmethod
    def listar(cls):
        NCliente.abrir()
        return cls.__clientes

    @classmethod
    def listar_id(cls, id):
        NCliente.abrir()
        for cliente in cls.__clientes:
            if cliente.get_id() == id: return cliente
        return None

    @classmethod
    def atualizar(cls, obj):
        NCliente.abrir()
        cliente = cls.listar_id(obj.get_id())
        cliente.set_nome(obj.get_nome())
        cliente.set_email(obj.get_email())
        cliente.set_fone(obj.get_fone())
        NCliente.salvar()

    @classmethod
    def excluir(cls, obj):
        NCliente.abrir()
        cliente = cls.listar_id(obj.get_id())
        cls.__clientes.remove(cliente)
        NCliente.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__clientes = []
            with open('clientes.json', 'r') as arquivo:
                a = json.load(arquivo)
                for cliente in a:
                    c = Cliente(cliente['_Cliente__id'], cliente['_Cliente__nome'], cliente['_Cliente__email'], cliente['_Cliente__fone'])
                    cls.__clientes.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('clientes.json', 'w') as arquivo:
            json.dump(cls.__clientes, arquivo, default=vars)

class Servico:
    def __init__(self, id, desc, valor, duracao):
        self.__id = id
        self.__desc = desc
        self.__valor = valor
        self.__duracao = duracao

    def set_id(self, id):
        self.__id = id

    def set_desc(self, desc):
        self.__desc = desc

    def set_valor(self, valor):
        self.__valor = valor

    def set_duracao(self, duracao):
        self.__duracao = duracao

    def get_id(self):
        return self.__id

    def get_desc(self):
        return self.__desc

    def get_valor(self):
        return self.__valor

    def get_duracao(self):
        return self.__duracao

    def __str__(self):
        return f'{self.__id}; {self.__desc}; {self.__valor}; {self.__duracao}'


class NServico:
    __servicos = []
    
    @classmethod
    def inserir(cls, servico):
        NServico.abrir()
        id = 0
        for i in cls.__servicos:
            if i.get_id() > id: id = i.get_id()
        servico.set_id(id + 1)
        cls.__servicos.append(servico)
        NServico.salvar()

    @classmethod
    def listar(cls):
        NServico.abrir()
        return cls.__servicos

    @classmethod
    def listar_id(cls, id):
        NServico.abrir()
        for i in cls.__servicos:
            if i.get_id() == id: return i
        return None

    @classmethod
    def atualizar(cls, obj):
        NServico.abrir()
        servico = NServico.listar_id(obj.get_id())
        servico.set_desc(obj.get_desc())
        servico.set_valor(obj.get_valor())
        servico.set_duracao(obj.get_duracao())
        NServico.salvar()

    @classmethod
    def excluir(cls, obj):
        NServico.abrir()
        servico = NServico.listar_id(obj.get_id())
        cls.__servicos.remove(servico)
        NServico.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__servicos = []
            with open('servicos.json', 'r') as arquivo:
                a = json.load(arquivo)
                for servico in a:
                    s = Servico(servico['_Servico__id'], servico['_Servico__desc'], servico['_Servico__valor'], servico['_Servico__duracao'])
                    cls.__servicos.append(s)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('servicos.json', 'w') as arquivo:
            json.dump(cls.__servicos, arquivo, default=vars)


class Agenda:
    def __init__(self, id, data, confirm, idCliente, idServico):
        self.__id = id
        self.__data = data
        self.__confirm = confirm
        self.__idCliente = idCliente
        self.__idServico = idServico

    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_confirm(self, confirm):
        self.__confirm = confirm

    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente

    def set_idServico(self, idServico):
        self.__idServico = idServico

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_confirm(self):
        return self.__confirm

    def get_idCliente(self):
        return self.__idCliente

    def get_idServico(self):
        return self.__idServico
    
    def to_json(self):
        return { '__id' : self.__id, '__data': self.__data.strftime('%d/%m/%Y'), '__confirm': self.__confirm, '__idCliente' : self.__idCliente, '__idServico' : self.__idServico}

    def __str__(self):
        return f'{self.__id}; {self.__data}; {self.__confirm}; {self.__idCliente}; {self.__idServico}'


class NAgenda:
    __agendas = []

    @classmethod
    def inserir(cls, obj):
        NAgenda.abrir()
        id = 0
        for agenda in cls.__agendas:
            if agenda.get_id() > id: id = agenda.get_id()
        obj.set_id(id + 1)
        cls.__agendas.append(obj)
        NAgenda.salvar()

    @classmethod
    def listar(cls):
        NAgenda.abrir()
        return cls.__agendas

    @classmethod
    def listar_id(cls, id):
        NAgenda.abrir()
        for agenda in cls.__agendas:
            if agenda.get_id() == id: return agenda
        return None

    @classmethod
    def atualizar(cls, obj):
        NAgenda.abrir()
        agenda = cls.listar_id(obj.get_id())
        agenda.set_data(obj.get_data())
        agenda.set_confirm(obj.get_confirm())
        agenda.set_idCliente(obj.get_idCliente())
        agenda.set_idServico(obj.get_idServico())
        NAgenda.salvar()

    @classmethod
    def excluir(cls, obj):
        NAgenda.abrir()
        agenda = cls.listar_id(obj.get_id())
        cls.__agendas.remove(agenda)
        NAgenda.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__agendas = []
            with open('agendas.json', 'r') as arquivo:
                a = json.load(arquivo)
                for agenda in a:
                    d = Agenda(agenda['__id'], datetime.strptime(agenda['__data'], '%d/%m/%Y'), agenda['__confirm'], agenda['__idCliente'], agenda['__idServico'])
                    cls.__agendas.append(d)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('agendas.json', 'w') as arquivo:
            json.dump(cls.__agendas, arquivo, default=Agenda.to_json)



class UI:
    @classmethod
    def main(cls):
        op = 50
        while op != 0:
            op = UI.menu()
            if op == 1: UI.ClienteInserir()
            if op == 2: UI.ClienteListar()
            if op == 3: UI.ClienteAtualizar()
            if op == 4: UI.ClienteExcluir()
            if op == 5: UI.ServicoInserir()
            if op == 6: UI.ServicoListar()
            if op == 7: UI.ServicoAtualizar()
            if op == 8: UI.ServicoExcluir()
            if op == 9: UI.AgendaInserir()
            if op == 10: UI.AgendaListar()
            if op == 11: UI.AgendaAtualizar()
            if op == 12: UI.AgendaExcluir()
            if op == 13: UI.AgendaDia()

    @classmethod
    def menu(cls):
        print('0 - sair; 1 - inserir cliente; 2 - listar cliente; 3 - atualizar cliente; 4 - excluir cliente\n5 - inserir serviço; 6 - listar serviço; 7 - atualizar serviço; 8 - excluir serviço\n9 - inserir agenda; 10 - listar agenda; 11 - atualizar agenda; 12 excluir agenda; 13 - abrir agenda')
        return int(input())

    @classmethod
    def ClienteInserir(cls):
        nome = input('Nome: ')
        email = input('E-mail: ')
        fone = input('Fone: ')
        cliente = Cliente(0, nome, email, fone)
        NCliente.inserir(cliente)

    @classmethod
    def ClienteListar(cls):
        for cliente in NCliente.listar(): print(cliente)

    @classmethod
    def ClienteAtualizar(cls):
        UI.ClienteListar()
        id = int(input('id do cliente a ser atualizado: '))
        nome = input('Novo nome: ')
        email = input('Novo e-mail')
        fone = input('Novo fone: ')
        cliente = Cliente(id, nome, email, fone)
        NCliente.atualizar(cliente)

    @classmethod
    def ClienteExcluir(cls):
        UI.ClienteListar()
        id = int(input('id do cliente a ser excluído: '))
        cliente = Cliente(id, '', '', '')
        NCliente.excluir(cliente)

    @classmethod
    def ServicoInserir(cls):
        desc = input('Descrição: ')
        valor = float(input('Valor: '))
        duracao = input('Duração: ')
        servico = Servico(0, desc, valor, duracao)
        NServico.inserir(servico)

    @classmethod
    def ServicoListar(cls):
        for servico in NServico.listar(): print(servico)

    @classmethod
    def ServicoAtualizar(cls):
        UI.ServicoListar()
        id = int(input('Digite o id a ser atualizado: '))
        desc = input('Nova descrição: ')
        valor = float(input('Novo valor: '))
        duracao = input('Nova duração: ')
        servico = Servico(id, desc, valor, duracao)
        NServico.atualizar(servico)

    @classmethod
    def ServicoExcluir(cls):
        UI.ServicoListar()
        id = int(input('Digite o id a ser excluído: '))
        servico = Servico(id, '', '', '')
        NServico.excluir(servico)

    @classmethod
    def AgendaInserir(cls):
        data = datetime.strptime(input('Data no formato dd/mm/aaaa: '), '%d/%m/%Y')
        confirm = input('Confirmar? s/n: ')
        if confirm == 's': confirm = 'Sim'
        else: confirm = 'Não'
        UI.ClienteListar()
        idCliente = int(input('id do cliente: '))
        UI.ServicoListar()
        idServico = int(input('id do serviço: '))
        agenda = Agenda(id, data, confirm, idCliente, idServico, '', '', '')
        NAgenda.inserir(agenda)
        
    @classmethod
    def AgendaListar(cls):
        for agenda in NAgenda.listar(): print(agenda)

    @classmethod
    def AgendaAtualizar(cls):
        UI.AgendaListar()
        id = int(input('id da agenda a ser atualizada: '))
        data = datetime.strptime(input('Data no formato dd/mm/aaaa: '), '%d/%m/%Y')
        confirm = input('Confirmar? s/n: ')
        if confirm == 's': confirm = 'Sim'
        else: confirm = 'Não'
        UI.ClienteListar()
        idCliente = int(input('Novo id do cliente: '))
        UI.ServicoListar()
        idServico = int(input('Novo id do serviço: '))
        agenda = Agenda(id, data, confirm, idCliente, idServico, '', '', '')
        NAgenda.atualizar(agenda)

    @classmethod
    def AgendaExcluir(cls):
        UI.AgendaListar()
        id = int(input('id da agenda a ser excluída: '))
        agenda = Agenda(id, '', '', '', '', '', '', '')
        NAgenda.excluir(agenda)

    @classmethod
    def AgendaDia(cls):
        data = datetime.strptime(input('Digite a data da agenda: '), '%d/%m/%Y')
        hora_init = datetime.strptime(input('Digite a hora inicial: '), '%H:%M')
        hora_final = datetime.strptime(input('Digite a hora final: '), '%H:%M')
        duracao = datetime.strptime(input('Duração em minutos: '), '%M')
        while hora_init <= hora_final:
            data_horario = datetime(data.year, data.month, data.day, hora_init.hour, hora_init.minute)
            agenda = Agenda(0, data_horario, 0, 0, 0)
            NAgenda.inserir(agenda)
            hora_init += timedelta(minutes=duracao.minute)


UI.main()
