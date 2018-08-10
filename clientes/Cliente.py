class Cliente:

    def __init__(self, nome = None, sexo = None, data_nascimento = None):
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento

    def cadastrar_cliente(self, nome, sexo, data_nascimento):
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento