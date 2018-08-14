from contas.Conta import Conta

class Corrente(Conta):

    def __init__(self):
        self.taxa_manutencao = None

    def criar_conta(self, agencia, conta, saldo, tipo_conta, id_cliente, senha):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        self._tipo_conta = tipo_conta
        self._id_cliente = id_cliente
        self._senha = senha