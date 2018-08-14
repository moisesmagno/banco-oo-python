from clientes.Cliente import Cliente

class Juridica(Cliente):

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None

    def cadastrar_cliente(self, razao_social, cnpj, estado, cidade, dt_cadastro):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self._estado = estado
        self._cidade = cidade
        self._dt_cadastro = dt_cadastro