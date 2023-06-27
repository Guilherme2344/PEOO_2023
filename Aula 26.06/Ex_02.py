import enum
from datetime import datetime

class Pagamento(enum.Enum):
    ABERTO = 1
    PARCIAL = 2
    PAGO = 3


class Boleto:
    def __init__(self, barra, data_emissao, data_vencimento, data_pagamento, valor_boleto, valor_pago, situacao):
        self.__barra = barra
        self.__data_emissao = data_emissao
        self.__data_vencimento = data_vencimento
        self.__data_pagamento = data_pagamento
        self.__valor_boleto = valor_boleto
        self.__valor_pago = valor_pago
        self.__situacao = situacao
        self.pagar(valor_pago)

    def pagar(self, valor):
        if valor <= self.__valor_pago: self.__valor_pago = valor
        else: raise ValueError()

    def situacao(self):
        if self.__valor_pago == 0: 
            self.__situacao = Pagamento.ABERTO.name
        elif self.__valor_pago > 0 and self.__valor_pago < self.__valor_boleto:
            self.__situacao = Pagamento.PARCIAL.name
        elif self.__valor_pago == self.__valor_boleto:
            self.__situacao = Pagamento.PAGO.name
        else:
            raise ValueError()
        return self.__situacao
    
    def __str__(self):
        return f'Código de barras = {self.__barra}; Data de Emissão = {self.__data_emissao}\nData de Vencimento = {self.__data_vencimento}; Data de Pagamento = {self.__data_pagamento}\nValor do Boleto = R${self.__valor_boleto:.2f}; Valor Pago = R${self.__valor_pago:.2f}; Situação = {self.__situacao}'


class UI:
    def main():
        barra = input('Digite o código de barras: ')
        emissao = datetime.strftime(datetime.strptime(input('Digite a data de emissão: '), '%d/%m/%Y'), '%d/%m/%Y')
        vencimento = datetime.strftime(datetime.strptime(input('Digite a data de vencimento: '), '%d/%m/%Y'), '%d/%m/%Y')
        pagamento = datetime.strftime(datetime.strptime(input('Digite a data de pagamento: '), '%d/%m/%Y'), '%d/%m/%Y')
        boleto = float(input('Digite o valor do boleto: '))
        pago = float(input('Digite o valor pago: '))
        situacao = Pagamento(int(input('Digite 1 para Aberto; 2 para Parcial; 3 para Pago: ')))
        x = Boleto(barra, emissao, vencimento, pagamento, boleto, pago, situacao)
        x.situacao()
        print(x)


UI.main()
