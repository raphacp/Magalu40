# possível solução do super desafio

'''
Super desafio! Faça um sistema de cadastro de clientes. Modele cada cliente como uma lista de três elementos: nome, CPF e e-mail.

a. Faça uma função que peça o nome, o CPF e o e-mail da pessoa e retorne uma lista contendo esses elementos nessa ordem.

b. Os clientes cadastrados devem ser armazenados em uma lista (uma lista de listas, já que cada cliente será uma lista tal como produzido no item a).

c. Faça uma função que recebe a lista do item b) e um CPF e, se esse cliente estiver na lista de cadastro, sua função deve devolver a lista de dados desse cliente; caso contrário, sua função deve imprimir “não encontrado”.

d. Enquanto não for digitado 0, o seu programa deve continuar rodando. Se digitado 1, seu programa deve cadastrar um novo cliente; se digitado 2, seu programa deve pedir um CPF e procurá-lo na lista de clientes (item c); se digitado 3, seu programa deve imprimir todos os clientes cadastrados.
'''

def lista_cliente(nome, cpf, email):
    lista_cliente = []

    lista_cliente.append(nome)
    lista_cliente.append(cpf)
    lista_cliente.append(email)

    return lista_cliente

def dados(clientes, cpf):
    for cliente in clientes:
        # como os dados dos clientes nas listas estão na mesma ordem,
        # sabemos que o cpf do cliente está na posição 1 da lista
        if cliente[1] == cpf: 
            return cliente

        print('não encontrado')

#d. Enquanto não for digitado 0, o seu programa deve continuar rodando. Se digitado 1, seu programa deve cadastrar um novo cliente; se digitado 2, seu programa deve pedir um CPF e procurá-lo na lista de clientes (item c); se digitado 3, seu programa deve imprimir todos os clientes cadastrados.

clientes = []

comando = int(input('digite o comando que deseja executar: '))

while comando != 0:
    if comando == 1:
        nome = input('digite o nome do cliente: ')
        cpf = input('digite o cpf do cliente: ')
        email = input('digite o email do cliente: ')

        novo_cliente = lista_cliente(nome, cpf, email)

        clientes.append(novo_cliente)

    elif comando == 2:
        cpf = input('digite o cpf do cliente: ')

        cliente = dados(clientes, cpf)
        print(cliente)

    # se digitado 3, seu programa deve imprimir todos os clientes cadastrados.
    elif comando == 3:
        print('lista de clientes:')
        for cliente in clientes:
            print(cliente)

    comando = int(input('digite o comando que deseja executar: '))
