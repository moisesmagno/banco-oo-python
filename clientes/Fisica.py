from clientes.Cliente import Cliente

class Fisica(Cliente):

    def __init__(self):
        self.__nome = None
        self.__cpf = None

    def cadastrar_cliente(self, nome, cpf, estado, cidade, dt_cadastro):
        self.__nome = nome
        self.__cfp = cpf
        self._estado = estado
        self._cidade = cidade
        self._dt_cadastro = dt_cadastro


    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf
