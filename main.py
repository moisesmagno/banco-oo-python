from contas.Corrente import Corrente
from contas.Poupanca import Poupanca
from clientes.Fisica import Fisica
from clientes.Juridica import Juridica

print('*** Olá, vamos cadastrar o cliente! ***')
tipo_cliente = input('Que tipo de cliente será cadastrado? Física(f) ou Juridica(j)? ').upper()

#Verificando se o tipo de cliente foi bem escolhido
tipo_resposta = False
while(tipo_resposta == False):
    if(tipo_cliente == 'F'):
        tipo_resposta = True
    elif(tipo_cliente == 'J'):
        tipo_resposta = True
    else:
        tipo_cliente = input('Que tipo de cliente será cadastrado? Física(f) ou Juridica(j)? ').upper()

#Instanciado as classes correspondentes e solicitandos os dados necessários de acordo ao tipo do cliente informado.
if(tipo_cliente == 'F'):
    cliente_fisico = Fisica()
    cliente_fisico.cadastrar_cliente('Moisés', 23239754800, 'SP', 'São Paulo', '14/08/2018')
else:
    cliente_juridico = Juridica()
    cliente_juridico.cadastrar_cliente('Nublei LTDA', 123434324240001, 'SP', 'São Paulo', '14/08/2018')

