from contas.Conta import Conta

class Corrente(Conta):

    def __init__(self,):
        self.__taxa_manutencao = None

    @property
    def taxa_manutencao(self):
        return self.__taxa_manutencao

    @taxa_manutencao.setter
    def taxa_manutencao(self, taxa):
        self.__taxa_manutencao = taxa

