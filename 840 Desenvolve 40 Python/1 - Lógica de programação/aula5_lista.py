# 1
# Crie um dicionário cujas chaves são os meses do ano e os valores são a duração (em dias) 
# de cada mês.

""" meses = {
    'Janeiro': 31,
    'Fevereiro': 28,
    'Março': 31,
    'Abril': 30,
    'Maio': 31,
    'Junho': 30,
    'Julho': 31,
    'Agosto': 31,
    'Setembro': 30,
    "Outubro": 31,
    'Novembro': 30,
    'Dezembro': 31
}

for mes in meses:
    print(mes, meses[mes]) """

# 2
# Imprima as chaves seguidas dos seus valores para dicionário criado no exercício anterior.
# Exemplo:
# Janeiro - 31
# Fevereiro - 28
# Março - 31
# Etc...

""" meses = {
    'Janeiro': 31,
    'Fevereiro': 28,
    'Março': 31,
    'Abril': 30,
    'Maio': 31,
    'Junho': 30,
    'Julho': 31,
    'Agosto': 31,
    'Setembro': 30,
    "Outubro": 31,
    'Novembro': 30,
    'Dezembro': 31
}

for mes in meses:
    print(f"{mes} - {meses[mes]}") """

# Resposta do professor
# for k, v in meses.items():
#     print("%s - %d" %(k, v))


# 3
# Crie um dicionário para as seguintes relações:
# ‘Banana’: 3.0
# ‘Cebola’: 4.0
# ‘Maçã’: 5.7
# ‘Abacaxi’: 8.0

""" frutas = {
    'Banana': 3.0,
    'Cebola': 4.0,
    'Maçã': 5.7,
    'Abacaxi': 8.0
}

for fruta in frutas:
    print(f"{fruta} - {frutas[fruta]}") """

# 4
# Altere o valor da chave ‘Maçã’ no dicionário do exercício anterior para 8.6.

""" frutas = {
    'Banana': 3.0,
    'Cebola': 4.0,
    'Maçã': 5.7,
    'Abacaxi': 8.0
}
frutas ['Maçã'] = 8.6
for fruta in frutas:
    print(f"{fruta} - {frutas[fruta]}") """

# 5
# Crie uma função que receba os valores do nome, idade e e-mail de uma pessoa e guarde-os em um 
# dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. 
# Sua função deve retornar esse dicionário.

""" usuarios = {}

def cadastra_usuario(nome, idade, email):

    usuarios['nome'] = nome
    usuarios['idade'] = idade
    usuarios['email'] = email
    return usuarios

nome = input("Digite o nome do usuário: ")
idade = input("Digite a idade do usuário: ")
email = input("Digite o email do usuário: ")

cadastra_usuario(nome, idade, email)

for campo in usuarios:
    print(campo, ": ", usuarios[campo]) """

# 6
# Como você armazenaria a seguinte tabela usando apenas dicionários? Tente imprimir o valor correspondente 
# da linha Pedro x Coluna B.
# Coluna  A	    Coluna B
# Maria	1	    5
# Pedro	0.5	    3
# João	3.2	    1

""" alunos = {
    'Maria': {
        'coluna_A': 1,
        'coluna_B': 5
    },
    'Pedro':{
        'coluna_A': 0.5,
        'coluna_B': 3
    },
    'João':{
        'coluna_A': 3.2,
        'coluna_B': 1
    }
}

print(alunos['Pedro']["coluna_B"]) """

# 7
# Faça um programa que conte quantas vezes cada elemento aparece em uma lista (pode criar 
# uma lista na mão). 
# Esse programa deverá guardar os dados em um dicionário no qual as chaves são os elementos 
# da lista e 
# os valores são a contagem de quantas vezes esse elemento aparece.

""" elementos = ['banana', 'morango', 'uva', 'morango', 'uva', 'uva', 'banana', 'morango']
contador_lista = {}

for i in elementos:
    contador_lista[i] = elementos.count(i)
print(contador_lista) """

### Resposta do professor
""" def contaElementos(lista):
    contagem = {}
    for e in lista:
        if e not in contagem.keys():
            contagem[e] = 1
        else:
            contagem[e] += 1
    return contagem
lista_teste = ["Banana", "Maçã", "Banana", "Abacaxi"]
print(contaElementos(lista_teste)) """

# 8
# Faça um programa que fique pedindo uma resposta do usuário, entre 1, 2 e 3. Se o usuário digitar 1, o 
# programa deve cadastrar um novo usuário e guardar esse cadastro num dicionário cuja chave será o CPF da 
# pessoa. Quando o usuário digitar 2, o programa deve imprimir os usuários cadastrados; e se o usuário 
# digitar 3, o programa deve fechar.
# Exemplo do dicionário:
# ‘987.654.321-00’: {‘nome’: Maria, ‘idade’: 20, ‘email’: maria@mail.com}

""" usuarios = {}
opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n"))


while opcao != 3:
    if opcao == 1:
        cpf = input('Digite o cpf do novo usuário: ')
        nome = input('Digite o nome do novo usuário: ')
        idade = input('Digite a idade do novo usuário: ')
        email = input('Digite o email do novo usuário: ')
       
        novo_usuario = {}
        novo_usuario['nome'] = nome
        novo_usuario['idade'] = idade
        novo_usuario['email'] = email
        usuarios[cpf] = (novo_usuario)
    elif opcao == 2:
        for usuario in usuarios:
            print(usuario, usuarios[usuario])

    opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n")) """

### Resposta do professor

""" def cadastraPessoa(nome, idade, email): #função do exercício 5
    return { "nome": nome, "idade": idade, "email": email }

usuarios = {}
entrada = 0 # Começa a variável num valor que entra no loop
while entrada != 3:
    print()
    print("As opções são:")
    print("1 - Cadastrar novo usuário")
    print("2 - Mostrar usuários cadastrados")
    print("3 - Fechar programa")
    entrada = int(input("Escolha uma opção: "))
    print()
    if entrada == 1:
        print("Cadastro de usuário")
        CPF = input("CPF: ")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("Email: ")
        usuarios[CPF] = cadastraPessoa(nome, idade, email) 
        print("Usuário Cadastrado")

    elif entrada == 2:
        if len(usuarios) == 0:
            print("Não há usuários cadastrados")
        else:
            print("Lista de usuários cadastrados")
            for i in usuarios.items():
                print(i) """

# 9
# Implemente um sistema de busca para o programa do exercício anterior. Isto é, se o usuário digitar 4, 
# procure um determinado usuário pelo seu CPF.

""" usuarios = {}
opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n4. Buscar usuário\n"))

while opcao != 3:
    if opcao == 1:
        cpf = input('Digite o cpf do novo usuário: ')
        nome = input('Digite o nome do novo usuário: ')
        idade = input('Digite a idade do novo usuário: ')
        email = input('Digite o email do novo usuário: ')
       
        novo_usuario = {}
        novo_usuario['nome'] = nome
        novo_usuario['idade'] = idade
        novo_usuario['email'] = email
        usuarios[cpf] = (novo_usuario)
    elif opcao == 2:
        for usuario in usuarios:
            print(usuario, usuarios[usuario])
    elif opcao == 4:
        cpf = input('Digite o cpf do usuário: ')
        #print(usuarios[cpf])
        print(cpf, usuarios[usuario])

    opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n4. Buscar usuário\n"))
 """

### Resposta do professor

""" def cadastraPessoa(nome, idade, email): #função do exercício 5
    return { "nome": nome, "idade": idade, "email": email }

usuarios = {}
entrada = 0 # Começa a variável num valor que entra no loop
while entrada != 3:
    print()
    print("As opções são:")
    print("1 - Cadastrar novo usuário")
    print("2 - Mostrar usuários cadastrados")
    print("3 - Fechar programa")
    print("4 - Pesquisar usuário")
    entrada = int(input("Escolha uma opção: "))
    print()
    if entrada == 1:
        print("Cadastro de usuário")
        CPF = input("CPF: ")
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        email = input("Email: ")
        usuarios[CPF] = cadastraPessoa(nome, idade, email) 
        print("Usuário Cadastrado")

    elif entrada == 2:
        if len(usuarios) == 0:
            print("Não há usuários cadastrados")
        else:
            print("Lista de usuários cadastrados")
            for i in usuarios.items():
                print(i)

    elif entrada == 4:
        print("Pesquisa de usuário")
        CPF = input("CPF: ")
        if CPF in usuarios.keys():
            print(usuarios[CPF])
        else:
            print("Esse usuário não existe") """

