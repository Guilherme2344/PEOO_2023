import json
from datetime import datetime

class Medicamento:
    def __init__(self,id,descricao,valor,vencimento):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
        self.__vencimento = vencimento
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_valor(self):
        return self.__valor
    def get_vencimento(self):
        return self.__vencimento
    def set_id(self,id):
        self.__id = id
    def set_descricao(self,descricao):
        self.__descricao = descricao
    def set_valor(self,valor):
        self.__valor = valor
    def set_vencimento(self,vencimento):
        self.__vencimento = vencimento
    def to_json(self):
        return { '__id' : self.__id, '__descricao': self.__descricao, '__valor' : self.__valor, '__vencimento': self.__vencimento.strftime('%d/%m/%Y')}
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__valor} - {self.__vencimento}"

class NMedicamento:
    __medicamentos = []


    @classmethod
    def inserir(cls, obj):
        NMedicamento.abrir()
        id = 0
        for medicamento in cls.__medicamentos:
            if medicamento.get_id() > id: id = medicamento.get_id()
        obj.set_id(id + 1)
        cls.__medicamentos.append(obj)
        NMedicamento.salvar()

    @classmethod
    def listar(cls):
        NMedicamento.abrir()
        return cls.__medicamentos

    @classmethod
    def listar_id(cls, id):
        NMedicamento.abrir()
        for medicamento in cls.__medicamentos:
            if medicamento.get_id() == id: return medicamento
        return None

    @classmethod
    def atualizar(cls, obj):
        NMedicamento.abrir()
        medicamento = cls.listar_id(obj.get_id())
        medicamento.set_descricao(obj.get_descricao())
        medicamento.set_valor(obj.get_valor())
        medicamento.set_vencimento(obj.get_vencimento())
        NMedicamento.salvar()

    @classmethod
    def excluir(cls, obj):
        NMedicamento.abrir()
        medicamento = cls.listar_id(obj.get_id())
        cls.__medicamentos.remove(medicamento)
        NMedicamento.salvar()

    @classmethod
    def abrir(cls):
        try:
            cls.__medicamentos = []
            with open('medicamentos.json', 'r') as arquivo:
                a = json.load(arquivo)
                for medicamento in a:
                    m = Medicamento(medicamento['__id'], medicamento['__descricao'], medicamento['__valor'], datetime.strptime(medicamento['__vencimento'], '%d/%m/%Y'))
                    cls.__medicamentos.append(m)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open('medicamentos.json', 'w') as arquivo:
            json.dump(cls.__medicamentos, arquivo, default=Medicamento.to_json)

    @classmethod
    def vencidos(cls):
        for medicamento in cls.__medicamentos:
            hoje = datetime.today()
            if medicamento.get_vencimento() < hoje:
                return medicamento
            return None


class UI:
    @classmethod
    def main(cls):
        op = 50
        while op != 0:
            op = UI.menu()
            if op == 1:
                UI.inserir()
            if op == 2:
                UI.listar()
            if op == 3:
                UI.atualizar()
            if op == 4:
                UI.excluir()
            if op == 5:
                UI.vencidos()

    @classmethod
    def menu(cls):
        print('0 - sair | 1 - inserir | 2 - listar | 3 - atualizar | 4 - excluir | 5 - vencidos')
        return int(input())

    @classmethod
    def inserir(cls):
        descricao = input('Descrição: ')
        valor = float(input('Valor: '))
        vencimento = datetime.strptime(input('Vencimento no formato dd/mm/aaaa: '), '%d/%m/%Y')
        medicamento = Medicamento(0, descricao, valor, vencimento)
        NMedicamento.inserir(medicamento)

    @classmethod
    def listar(cls):
        for medicamento in NMedicamento.listar(): print(medicamento)

    @classmethod
    def atualizar(cls):
        UI.listar()
        id = int(input('Id do medicamento a ser atualizado: '))
        descricao = input('Nova descrição: ')
        valor = float(input('Novo valor: '))
        vencimento = datetime.strptime(input('Novo vencimento no formato dd/mm/aaaa: '), '%d/%m/%Y')
        medicamento = Medicamento(id, descricao, valor, vencimento)
        NMedicamento.atualizar(medicamento)

    @classmethod
    def excluir(cls):
        UI.listar()
        id = int(input('Id do medicamento a ser excluído: '))
        medicamento = Medicamento(id, '', '', '')
        NMedicamento.excluir(medicamento)
    
    @classmethod
    def vencidos(cls):
        for medicamento in NMedicamento.vencidos(): print(medicamento)


UI.main()
