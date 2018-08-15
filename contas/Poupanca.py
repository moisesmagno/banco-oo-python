from contas.Conta import Conta

class Poupanca(Conta):

    def __init__(self):
        self.__juros = None

    @juros_rendimentos.setter
    def juros_rendimentos(self, juros):
        self.__juros = juros

    @property
    def juros_rendimentos(self):
        return self.__juros

    @property
    def rendimento(self):
        return self.__juros * self._saldo