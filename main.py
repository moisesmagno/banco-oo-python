from contas.Corrente import Corrente
from contas.Poupanca import Poupanca
from clientes.Fisica import Fisica
from clientes.Juridica import Juridica

print('*** Olá, vamos cadastrar o cliente! ***')
tipo_cliente = input('Que tipo de cliente será cadastrado? Física(f) ou Juridica(j)? ').upper()

