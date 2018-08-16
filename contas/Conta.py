# -*- iso:8859-1 -*-
class Conta:

    def __init__(self):
        self.__agencia = None
        self.__conta = None
        self.__senha = None
        self._saldo = 0.0
        self.__id_cliente = None
        self.__tipo_corrente = None

    def criar_conta(self, agencia, conta, tipo_conta, id_cliente, senha, saldo):
        self.__agencia = agencia
        self.__conta = conta
        self.__senha = senha
        self._saldo = saldo
        self.__id_cliente = id_cliente
        self.__tipo_conta = tipo_conta

    def depositar(self):
        pass

    def sacar(self):
        pass




