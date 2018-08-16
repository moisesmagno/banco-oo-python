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

    cliente = Fisica()
    cliente.cadastrar_cliente(nome, cpf, estado, cidade, data)

    #Criando conta
    # agencia = int(input('Agencia: '))
    # conta = int(input('Conta: '))
    # tipo_conta = input('Tipo de conta Corrente(c) - Pupança(p): ').upper()
    # id_cliente = cliente_fisico.cpf
    # senha = input('Senha: ')
    # saldo = float(input('Saldo: '))
    #
    # if(tipo_conta == 'C'):
    #     conta = Corrente()
    # else:
    #     conta = Poupanca()
    #
    # conta.criar_conta(agencia, conta, tipo_conta, id_cliente, senha, saldo)

else:

    #Cadastrando a empresa
    razao_social = input("Razão social: ")
    cnpj = int(input("CNPJ: "))
    estado = input("Estado: ")
    cidade = input("Cidades: ")
    data = input("Data atual: ")

    cliente = Juridica()
    cliente.cadastrar_cliente(razao_social, cnpj, estado, cidade, data)

# Criando conta
agencia = int(input('Agencia: '))
numero_conta = int(input('Conta: '))
tipo_conta = input('Tipo de conta Corrente(c) - Pupança(p): ').upper()
id_cliente = cliente.cnpj if tipo_cliente == 'J' else cliente.cnpj
senha = input('Senha: ')
saldo_inicial = float(input('Valor do depósito inicial: '))

if (tipo_conta == 'C'):
    conta = Corrente()
    conta.criar_conta(agencia, numero_conta, tipo_conta, id_cliente, senha)
    conta.taxa_manutencao = 23.00
    conta.depositar(saldo_inicial)
else:
    conta = Poupanca()
    conta.criar_conta(agencia, numero_conta, tipo_conta, id_cliente, senha)
    conta.juros_rendimentos = 0.07
    conta.depositar(saldo_inicial)

#Exibindo dados da conta e que foram guardados nos atributos.
if (tipo_cliente == 'F'):
    print('Nombe: {0} \n '
          'CPF: {1} \n '
          'Estado: {2} \n'
          'Cidade: {3} \n'
          'Data de Cadastro: {4}'.format(cliente.nome, cliente.cpf, cliente.estado, cliente.cidade, cliente.dt_cadastro))
else:
    print('Razão Social: {0} \n '
          'CNPJ: {1} \n '
          'Estado: {2} \n'
          'Cidade: {3} \n'
          'Data de Cadastro: {4}'.format(cliente.razao_social, cliente.cnpj, cliente.estado, cliente.cidade, cliente.dt_cadastro))

# if(tipo_conta == 'C')
# else:
