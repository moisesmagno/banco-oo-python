class Cliente:

    def __init__(self):
        self._estado = None
        self._cidade = None
        self._dt_cadastro = None

    def cadastrar_cliente(self):
        pass

    @property
    def estado(self):
        return self._estado

    @property
    def cidade(self):
        return self._cidade

    @property
    def dt_cadastro(self):
        return self._dt_cadastro