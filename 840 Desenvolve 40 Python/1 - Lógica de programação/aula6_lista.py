# Exercícios recomendados: 1, 2, 5, 7, 12, 14

# 1
# Faça uma função que recebe um número e imprime seu dobro.

""" def imprime_dobro(num):
    dobro = num * 2
    print(f"O dobro de {num} é {dobro}.")
num = 2
imprime_dobro(num) """

# 2
# Faça uma função que recebe o valor do raio de um círculo e retorna o valor do comprimento de sua 
# circunferência: C = 2*pi*r.

""" from cmath import pi

def calcula_circunferencia(raio):
    circunferencia = 2 * pi * raio
    return circunferencia

raio = 4
print(f"\nO comprimento da circunferência do raio {raio} é {calcula_circunferencia(raio)}.\n") """

# 3
# Faça uma função para cada operação matemática básica (soma, subtração, multiplicação e divisão). 
# As funções devem receber dois números e retornar o resultado da operação.

""" def soma(num1, num2):
    conta = num1 + num2
    return conta

def subtrai(num1, num2):
    conta = num1 - num2
    return conta

def multiplica(num1, num2):
    conta = num1 * num2
    return conta

def divide(num1, num2):
    conta = num1 / num2
    return conta

numero1 = int(input("Digite o primeiro número da operação: "))
numero2 = int(input("Digite o segundo número da operação: "))

entrada = 0 # Começa a variável num valor que entra no loop
while entrada != 5:
    print()
    print("As opções são:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    entrada = int(input("Escolha uma opção: "))
    print()
    if entrada == 1:
        print("Somando")
        print(f"A soma de {numero1} com {numero2} é = {soma(numero1, numero2)}.")
        
    elif entrada == 2:
        print("Subtraindo")
        print(f"A subtração de {numero1} com {numero2} é = {subtrai(numero1, numero2)}.")

    elif entrada == 3:
        print("Multiplicando")
        print(f"A multiplicação de {numero1} com {numero2} é = {multiplica(numero1, numero2)}.")

    elif entrada == 4:
        print("Dividindo")
        print(f"A divisão de {numero1} com {numero2} é = {divide(numero1, numero2)}.")     """

# 4
# Faça uma função que recebe um nome e imprime “olá, [nome]”.

""" def imprime_saudacao(nome):
    print(f"Olá, {nome}.")

imprime_saudacao('Rapha') """

# 5
# Faça uma função que recebe um nome e um horário e imprime “Bom dia, [nome]”, caso seja antes de 12h, 
# “Boa Tarde, [nome]”, caso seja entre 12h e 18h e “Boa noite, [nome]” se for após às 18h.

""" def saudacao (nome, hora):
    if hora < 12:
        print(f"Bom dia {nome}.")
    elif hora < 18:
        print(f"Boa tarde {nome}.")
    else:
        print(f"Boa noite {nome}.")

nome = input("Digite seu nome: ")
hora = int(input("Digite a hora: "))

saudacao(nome, hora) """

# 6
# Faça uma função que recebe um número e retorna True se ele é par ou False, se ele é ímpar.

""" def par_impar(num):
    
    par = (num % 2 == 0)
    return par

numero = int(input("Digite um número: "))
par = (par_impar(numero))
if par == True:
    print("O número digitado é par.")
else:
    print("O número digitado é ímpar.") """

# 7
# Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e retorna o maior entre eles.

""" import random

def sorteia_num(num):
    numeros = []
    for i in range(num):
        num_sorteado = random.randint(0, 100)
        numeros.append(num_sorteado)
    print(f"\nOs números sorteados foram: {numeros}.\n")
    return max(numeros)

quantidade = 10
print(f"E o maior número sorteado foi {sorteia_num(quantidade)}.\n") """

# 8
# Faça uma função que recebe um número n de entrada, sorteia n números aleatórios entre 0 e 100 e retorna 
# a média deles.

""" import random

def sorteia_media_num(num):
    numeros = []
    for i in range(num):
        numeros.append(random.randint(0, 100))
    print('Números sorteados: ', numeros)
    return sum(numeros) / len(numeros)

print('Média: ', sorteia_media_num(int(input('Digite a quantidade de números a serem sorteados: ')))) """

# 9
# Faça uma função que recebe uma lista de palavras e retorna uma lista contendo as mesmas palavras da 
# lista anterior, porém escritas em caixa alta.

""" def maiusculas(lista):
        maiusculas = str(lista).upper()
        return maiusculas

lista_palavras = ['rapha', 'Karen', 'HENRy']
print(maiusculas(lista_palavras)) """

# 10
# Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.
# Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], 
# então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].

""" def soma_itens(lista1, lista2):
    
    lista_somas = []
    indice = 0
    while indice < len(lista1):
        soma = lista1[indice] + lista2[indice]
        lista_somas.append(soma)
        indice +=1
    return lista_somas

lista1 = [1,4,3]
lista2 = [3,5,1]

print(soma_itens(lista1, lista2)) """

# 11
# Faça uma função que receba duas listas e retorne o produto item a item dessas listas.
# Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], 
# então a função deve retornar [1x3, 4x5, 3x1] = [3, 20, 3].

""" def multiplica_itens(lista1, lista2):
    
    lista_produtos = []
    indice = 0
    while indice < len(lista1):
        produto = lista1[indice] * lista2[indice]
        lista_produtos.append(produto)
        indice +=1
    return lista_produtos

lista1 = [1,4,3]
lista2 = [3,5,1]

print(multiplica_itens(lista1, lista2)) """

# 12
# Faça uma função que recebe um número x e uma lista numérica e retorna uma lista cujos elementos são os 
# itens da lista de entrada multiplicado por x.
# Exemplo:
# Se a função receber o número 5 e a lista [3,5,1], 
# então a função deve retornar [5x3, 5x5, 5x1] = [15, 25, 5].

""" def multiplica_lista (num, lista):
    lista_produtos = []
    produto = 0
    for i in range (len(lista)):
        produto = num * lista[i]
        lista_produtos.append(produto)
    return lista_produtos

lista = [3,5,1]
numero = 5

print(multiplica_lista(numero, lista)) """

# 13
# Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.

""" def soma(lista):
    soma = sum(lista)
    return soma

lista = [15, 30, 5]

print(f"A soma da lista {lista} é {soma(lista)}.") """

# 14
# Faça uma função que recebe uma lista de números e retorna a média aritmética dos elementos dessa lista.

""" def media(lista):
    media = sum(lista) / len(lista)
    return media

lista = [15, 30, 5]

print(f"A média da lista {lista} é {media(lista):.2f}.") """

# 15
# Desafio 1 - Faça uma função que receba um número e calcule seu fatorial.

""" def calcula_fatorial(numero):
    fatorial = 1
    for i in range(1, numero+1):
        fatorial = fatorial * i
    return fatorial

numero = int(input("Digite um número para calcularmos o seu fatorial: ")) 
print(f"O fatorial de {numero} é {calcula_fatorial(numero)}.") """

# 16
# Desafio 3 - A sequência Fibonacci é a sequência cujos dois primeiros termos são 1 e os demais são 
# obtidos através da soma de seus dois antecessores, isso é:
# a. Fibonacci(1) = 1 e Fibonacci(2) = 2;
# b. dado qualquer número n >= 3, Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
# Assim, os 10 primeiros termos da sequência Fibonacci são:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
# Faça uma função que receba um número n e calcule o termo de número n da sequência Fibonacci.

""" def calcula_fibonacci(num):
    lista_fibo = [1, 1]
    fibo = 0
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        for i in range(3, num+1):
            fibo = lista_fibo[i-2] + lista_fibo[i-3]
            lista_fibo.append(fibo)
        return fibo

numero = int(input('Digite um número: '))
print(f"O Fibonacci de {numero} termos é {calcula_fibonacci(numero)}.") """

# 17
# Super Desafio! - Repita o exercício anterior usando recursão, ou seja, uma função que chame ela mesma, 
# lembrando que 3! = 3*2!, que 2! = 2*1!, que 1! = 1*0! e que 0! = 1.

""" def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

num = int(input("Digite um número: "))
print(f"O fatorial de {num} é {fatorial(num)}.") """

# 18
# Desafio 2 - Faça uma função que recebe duas entradas: um input dado pelo usuário e um string que 
# informa o tipo de dado ("idade", "salário" ou "sexo"), e verifica se os dados digitados foram válidos, 
# usando os seguintes critérios:
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro.

""" def valida_dados(valor1, valor2):
    if valor2 == 'idade':
        if valor1 < 0 or valor1 > 150:
            return False
        else:
            return True
    elif valor2 == 'salario':
        if valor1 <= 0:
            return False
        else:
            return True
    elif valor2 == 'sexo':
        if valor1 != "M" and valor1 != "F" and valor1 != "Outro":
            return False
        else:
            return True    

idade = int(input("Digite a idade: "))
if valida_dados(idade, 'idade') == True:
    print('O dado digitado está válido.')
else:
    print('O dado digitado está inválido.')

salario = float(input("Digite o salário: "))
if valida_dados(salario, 'salario') == True:
    print('O dado digitado está válido.')
else:
    print('O dado digitado está inválido.')

sexo = input("Digite o sexo: ")
if valida_dados(sexo, 'sexo') == True:
        print('O dado digitado está válido.')
else:
    print('O dado digitado está inválido.') """

# 19
# Super Desafio! - Refaça o desafio 3 usando recursão.

""" def calcula_fibonacci(num):
    lista = []
    if num == 1:
        return 1
    elif num == 2:
        return 1
    else:
        return calcula_fibonacci(num-1) + calcula_fibonacci(num-2)

num = int(input("Digite um número: "))
print(f"O Fibonacci de {num} termos é {calcula_fibonacci(num)}.") """


# 20
# Super Desafio! - Faça um jogo de BlackJack usando funções: o BlackJack, ou Vinte e Um, é um jogo em que 
# os jogadores podem comprar cartas livremente, enquanto tiverem menos de 21 pontos. No nosso jogo, 
# o Ás vale um ponto; as cartas de 2 a 10 valem o número de pontos que elas representam; e Valete, 
# Dama e Rei valem 10 pontos cada. Ganha o jogador que tiver o maior número de pontos, desde que este 
# seja menor ou igual a 21. Nosso jogo deve ter as seguintes funções:
# a. Função principal: a função que vamos chamar para iniciar o jogo. Essa função não irá receber nem 
# retornar nenhuma variável. Ela deve perguntar o número de jogadores participantes e o nome de cada um. 
# Em seguida ela chama as outras funções do jogo.
# b. Função para criar o baralho: essa função deve criar um baralho (uma lista) com as cartas do baralho.
# c. Função para a jogada: essa função deve receber o nome do jogador que irá realizar a jogada e, caso 
# ele ainda esteja ativo (tenha menos de 21 pontos e ainda não tenha desistido de comprar cartas) deve 
# perguntar se ele quer comprar uma carta. Se ele responder que sim, a função deve chamar a próxima 
# função para sortear uma carta e somar o valor retornado na pontuação do jogador; se ele responder que 
# não, a função deve desativar o jogador para que ele não possa mais comprar cartas; Essa função só deve 
# ser chamada enquanto houver jogadores ativos.
# d. Função para o sorteio: essa função retira uma carta aleatória do baralho e retorna o número de pontos 
# que essa carta vale.
# e. Função verificação: verifica e indica qual/quais jogador/jogadores tem o maior número de pontos, que 
# seja menor ou igual a 21.

# a. Função principal: a função que vamos chamar para iniciar o jogo. Essa função não irá receber nem 
# retornar nenhuma variável. Ela deve perguntar o número de jogadores participantes e o nome de cada um. 
# Em seguida ela chama as outras funções do jogo.
""" def inicia_jogo():
    lista_jogadores = []
    qtd_jogadores = int(input("Digite a quantidade de jogadores: "))

    for i in range(qtd_jogadores):
        lista_jogadores.append(input(f"Digite o nome do jogador {i+1}: "))
    print(qtd_jogadores)
    print(lista_jogadores)

inicia_jogo() """

# b. Função para criar o baralho: essa função deve criar um baralho (uma lista) com as cartas do baralho.

def cria_baralho ():
    baralho = []
    copas = []
    ouros = []
    espadas = []
    paus = []
    posicao = 0

    baralho.append("AS")
    for i in range (2,11):
        if i < 10:
            baralho.append(str(i))
        else:
            baralho.append(str(i))
            baralho.append("J")
            baralho.append("Q")
            baralho.append("K")
            #copas = baralho.copy()
            #ouros = baralho.copy()
            #espadas = baralho.copy()
            #paus = baralho.copy()
    #print(copas)
    #print(ouros)
    #print(espadas)
    #print(paus)
    #print(baralho)

    for i in range(len(baralho)):
        posicao = baralho[i] + 'c'
        #print(posicao)
        copas.insert(i, posicao)
        #print(copas)

    print(copas)
    return baralho

print(cria_baralho())

# c. Função para a jogada: essa função deve receber o nome do jogador que irá realizar a jogada e, caso 
# ele ainda esteja ativo (tenha menos de 21 pontos e ainda não tenha desistido de comprar cartas) deve 
# perguntar se ele quer comprar uma carta. Se ele responder que sim, a função deve chamar a próxima 
# função para sortear uma carta e somar o valor retornado na pontuação do jogador; se ele responder que 
# não, a função deve desativar o jogador para que ele não possa mais comprar cartas; Essa função só deve 
# ser chamada enquanto houver jogadores ativos.



# d. Função para o sorteio: essa função retira uma carta aleatória do baralho e retorna o número de pontos 
# que essa carta vale.



# e. Função verificação: verifica e indica qual/quais jogador/jogadores tem o maior número de pontos, que 
# seja menor ou igual a 21.





# Resposta do professor

import random
def cria_baralho():
    baralho = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q", "J", "K"]*4
    print("Baralho criado!")
    return baralho

def jogo(jogadores, baralho):
    existem_ativos = True # Variável que controla o fluxo do jogo. Começa em true para entrar no loop
    while existem_ativos:
        existem_ativos = False # Em cada iteração do loop, começa como falsa,
                               # e se encontrar qualquer jogador ativo, é atualizada
        for jogador in jogadores:
            jogada(jogador, baralho)
            if jogador[2] == True:  # Verifica após a jogada se ele ainda está ativo
                existem_ativos = True

def jogada(jogador, baralho):
    if jogador[2] == True: # Jogador está ativo
        print("Jogada de", jogador[0], "com", jogador[1], "pontos.")
        pergunta = input("Você que comprar 1 carta? ")
        if pergunta == "sim":
            carta = sorteio(baralho)
            jogador[1] += carta
            print("Você agora tem", jogador[1], "pontos.")
            if jogador[1] > 21:
                print("Que azar!")
                jogador[2] = False # Desativa o jogador
        else:
            print("Ok, você parou de comprar.")
            jogador[2] = False
    print()

def sorteio(baralho):
    carta = random.choice(baralho)
    baralho.remove(carta)
    if carta == 'A':
        pontos = 1
    elif carta == 'Q' or carta == 'J' or carta == 'K':
        pontos = 10
    else:
        pontos = int(carta)
    print("Você comprou um", carta, "que vale", pontos, "pontos")
    return pontos

def verificacao(jogadores):
    vencedor = None
    empate = False
    maximo_pontos = 0
    for jogador in jogadores:
        pontos = jogador[1]
        if pontos <= 21:
            if pontos > maximo_pontos:
                vencedor = jogador
                maximo_pontos = pontos
                empate = False
            elif pontos == maximo_pontos:
                vencedor = None
                empate = True

    if empate:
        print("Temos um empate!")
    elif vencedor == None:
        print("Todos estouraram 21!")
    else:
        print("O vencedor foi", jogador[0], "com", jogador[1], "pontos.")

def main():
    no_jogadores = int(input("Quantos jogadores irão participar? "))
    jogadores = []
    for i in range(no_jogadores):
        nome = input("Qual o nome do jogador? ")
        pontos = 0
        ativo = True
        jogador = [nome, pontos, ativo]
        jogadores.append(jogador)

    baralho = cria_baralho()
    jogo(jogadores, baralho)
    verificacao(jogadores)

main()


# 21
# Super desafio! Faça um sistema de cadastro de clientes. Modele cada cliente como uma lista de três elementos: 
# nome, CPF e e-mail.
# a. Faça uma função que peça o nome, o CPF e o e-mail da pessoa e retorne uma lista contendo esses elementos 
# nessa ordem.
# b. Os clientes cadastrados devem ser armazenados em uma lista (uma lista de listas, já que cada cliente será 
# uma lista tal como produzido no item a).
# c. Faça uma função que recebe a lista do item b) e um CPF e, se esse cliente estiver na lista de cadastro, 
# sua função deve devolver a lista de dados desse cliente; caso contrário, sua função deve imprimir 
# “não encontrado”.
# d. Enquanto não for digitado 0, o seu programa deve continuar rodando. Se digitado 1, seu programa deve 
# cadastrar um novo cliente; se digitado 2, seu programa deve pedir um CPF e procurá-lo na lista de clientes 
# (item c); se digitado 3, seu programa deve imprimir todos os clientes cadastrados.


def cadastraPessoa(nome, idade, email): #função do exercício 5
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
            print("Esse usuário não existe")


# Resposta do professor

def cadastroCliente():
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    email = input("Digite o email: ")
    return [nome, cpf, email]

def pedeComando():
    print()
    print("Escolha uma ação")
    print("0 - Sair do programa")
    print("1 - Cadastrar cliente")
    print("2 - Procurar cliente")
    print("3 - Mostrar todos clientes")
    comando = int(input())
    return comando

def procuraCliente(lista, cpf):
    for cliente in lista:
        if cliente[1] == cpf:
            return cliente
    print("Não encontrado")

def imprimeClientes(lista):
    #Função para imprimir todos os clientes cadastrados no sistema
    print("Lista de clientes")
    for cliente in lista:
        print(cliente)

listaClientes = [] # Lista com todos os clientes
comando = pedeComando()
while comando != 0:
    if comando == 1:
        listaClientes.append(cadastroCliente())
        print("Cliente cadastrado!")
    elif comando == 2:
        cpf = input("Qual o CPF do cliente? ")
        cliente = procuraCliente(listaClientes, cpf)
        if cliente != None: # Verifica se a função retornou algo
            print("As informações do cliente são: ")
            print(cliente)
    elif comando == 3:
        imprimeClientes(listaClientes)
    else:
        print("Comando inválido.")

    comando = pedeComando() # Pede uma nova entrada

