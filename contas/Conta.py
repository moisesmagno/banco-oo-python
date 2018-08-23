# -*- iso:8859-1 -*-
class Conta:

    def __init__(self):
        self.__agencia = None
        self.__conta = None
        self.__senha = None
        self._saldo = 0.0
        self.__id_cliente = None
        self.__tipo_conta = None

    def criar_conta(self, agencia, conta, tipo_conta, id_cliente, senha, saldo):
        self.__agencia = agencia
        self.__conta = conta
        self.__senha = senha
        self._saldo = saldo
        self.__id_cliente = id_cliente
        self.__tipo_conta = tipo_conta

    @property
    def agencia(self):
        return self.__agencia

    @property
    def conta(self):
        return self.__conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def tipo_conta(self):
        return 'Corrente' if self.__tipo_conta == 'C' else 'Poupança'

    def depositar(self):
        pass

    def sacar(self):
        pass




