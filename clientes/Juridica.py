from clientes.Cliente import Cliente

class Juridica(Cliente):

    def __init__(self):
        self.razao_social = None
        self.cnpj = None

