"""
Faça um programa que sorteia um número N e peça para o usuário adivinhar o número sorteado. 
A cada resposta errada, o seu programa deve imprimir um aviso dizendo que a resposta está 
errada e pedir novamente uma resposta ao usuário.

Para a realização desse exercício, utilize alguma função da biblioteca 
random (e.g. randint()).

EXTRA: implemente o programa de maneira que o usuário tenha um número máximo de tentativas.
Se o número for ultrapassado, imprima uma mensagem informando que as tentativas acabaram.
"""

# importando a biblioteca ("caixa de ferramentas") random
import random

# usando a "ferramenta" randint() pra gerar um número inteiro aleatorio
numero_sorteado = random.randint(0,5)

# caso queira ajuda em "debuggar", ou seja, ver o que está errado
# com o código, descomentar (isto é, tirar o "#") a linha abaixo pode ajudar
#print(numero_sorteado)

# lendo a resposta dada pelo usuário (string) e convertendo-a 
# em número inteiro (int)
resposta = int(input('Adivinhe o número sorteado: '))

# número de vezes que o usuário tentou
qtd_tentativas = 0

# adicionando um limite máximo de tentativas
max_tentativas = 3

# enquanto a quantidade de tentativas for menor que o limite E (and)
# enquanto a resposta for diferente do número sorteado, execute o código
while qtd_tentativas < max_tentativas and resposta != numero_sorteado:
    print('Resposta errada!')
    resposta = int(input('Adivinhe o número sorteado: '))

    # incrementando a quantidade de tentativas ("variável de controle").
    # o que será que acontece se nós não incrementarmos a variável?
    qtd_tentativas = qtd_tentativas + 1

# caso o limite de tentativas tenha sido ultrapassado
if qtd_tentativas >= max_tentativas:
    print('Acabaram suas tentativas')

# caso o usuário tenha acertado a resposta
elif resposta == numero_sorteado:
    # caso o programa chegue até aqui,
    print('Resposta certa!')