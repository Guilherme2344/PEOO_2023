import json

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
    def __init__(self):
        self.__clientes = []

    def inserir(self, c):
        self.__clientes.append(c)

    def listar(self):
        return self.__clientes
    
    def listar_id(self, c_id):
        for cliente in self.__clientes:
            if cliente.get_id() == c_id:
                return cliente
        return None
    
    def atualizar(self, valor):
        for i in self.__clientes:
            if i.get_id() == valor.get_id():
                i.set_id(valor.get_id())
                i.set_nome(valor.get_nome())
                i.set_email(valor.get_email())
                i.set_fone(valor.get_fone())

    def excluir(self, c):
        for i in self.__clientes:
            if i.get_id() == c:
                self.__clientes.remove(i)

    def abrir(self, nome):
        try:
            with open(nome, 'r') as arquivo:
                self.__clientes = json.load(arquivo)
        except FileNotFoundError:
            print(f'Arquivo {nome} não encontrado.')

    def salvar(self, nome):
        with open(nome, 'w') as arquivo:
            json.dump(self.__clientes, arquivo, indent=4)


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
                id = int(input('Id: '))
                nome = input('Nome: ')
                email = input('E-mail: ')
                fone = input('Fone: ')
                a = Cliente(id, nome, email, fone)
                x.inserir(a)
                print('cliente cadastrado')
            if op == 2:
                for i in x.listar(): print(i)
            if op == 3:
                id = int(input('Id: '))
                nome = input('Novo nome: ')
                email = input('Novo e-mail: ')
                fone = input('Novo fone: ')
                b = Cliente(id, nome, email, fone)
                x.atualizar(b)
                print('cliente atualizado')
            if op == 4:
                id = int(input('Id: '))
                x.excluir(id)
                print('cliente excluído')

UI.main()


@classmethod
  def abrir(cls):
    cls.clientes = []
    try: 
      with open("clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
          #cliente = Cliente(**obj)
          cliente = Cliente(obj["_id"], obj["_nome"], obj["_email"], obj["_fone"])
          cls.clientes.append(cliente)
    except (FileNotFoundError):
      pass      

  @classmethod 
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
      json.dump(cls.clientes, arquivo, default=lambda obj: obj.__dict__)
