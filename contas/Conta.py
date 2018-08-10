# -*- iso:8859-1 -*-

from clientes.Cliente import Cliente

class Conta:

    def __init__(self, agencia = None, conta = None, senha = None):
        self._agencia = agencia
        self._conta = conta
        self._senha = senha
        self._saldo = 0.0
        self._tipo_corrente = False
        self._tipo_poupanca = False

    def criar_conta(self, agencia, conta, senha):
        self._agencia = agencia
        self._conta = conta
        self._senha = senha


