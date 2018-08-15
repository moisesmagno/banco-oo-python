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

    #Cadastrando o cliente
    nome = input("Nome do cliente: ")
    cpf = int(input("CPF: "))
    estado = input("Estado: ")
    cidade = input("Cidades: ")
    data = input("Data atual: ")

    cliente_fisico = Fisica()
    cliente_fisico.cadastrar_cliente(nome, cpf, estado, cidade, data)

    #Criando conta
    agencia = int(input('Agencia: '))
    conta = int(input('Conta: '))
    tipo_conta = input('Tipo de conta Corrente(c) - Pupança(p): ').upper()
    id_cliente = cliente_fisico.cpf
    senha = input('Senha: ')
    saldo = float(input('Saldo: '))

    if(tipo_conta == 'C'):
        conta = Corrente()
    else:
        conta = Poupanca()

    conta.criar_conta(agencia, conta, tipo_conta, id_cliente, senha, saldo)

else:

    #Cadastrando a empresa
    razao_social = input("Razão social: ")
    cnpj = int(input("CNPJ: "))
    estado = input("Estado: ")
    cidade = input("Cidades: ")
    data = input("Data atual: ")

    cliente_juridico = Juridica()
    cliente_juridico.cadastrar_cliente(razao_social, cnpj, estado, cidade, data)

    # Criando conta
    agencia = int(input('Agencia: '))
    conta = int(input('Conta: '))
    tipo_conta = input('Tipo de conta Corrente(c) - Pupança(p): ').upper()
    id_cliente = cliente_juridico.cnpj
    senha = input('Senha: ')

    if (tipo_conta == 'C'):
        conta = Corrente()
    else:
        conta = Poupanca()

    conta.criar_conta(agencia, conta, tipo_conta, id_cliente, senha)

