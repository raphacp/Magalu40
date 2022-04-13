import random
import datetime as dt
import os
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

# Original
# matrix = [
#     [1, 0, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 1],
#     [1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 0],
# ]

def gera_matrix(y, x):
    ny = y
    nx = x
    matrix = [[1 if (random.random()>=0.5) else 0 for num in range(nx)] for x in range(ny)]
    return matrix

def mostra_matriz(matriz):
    print('A matriz é:')
    for lista in matriz:
        for elemento in lista:
            print(elemento, end=' ')
        print()

def gera_log(matriz, matriz_adj, lista_rio, visitadas):
    # Usando o Jupyter ele cria o arquivo de log na mesma pasta do arquivo .ipynb, mas usando .py ele gera em outro lugar.
    # Tentei forçar a criação na mesma pasta do arquivo .py mas n funcionou.
    caminho_log = os.path.abspath('.')+os.sep+'Raphael_Prado_Projeto_3.log'
    with open(caminho_log, 'a', encoding='UTF-8') as log:
        log.write(f'#'*100+'\n')
        log.write(f'''Data: {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n''')
        log.write(f'A matriz recebida foi de tamanho {len(matriz)}x{len(matriz[0])}: {matriz}\n')
        log.write(f'A matriz verificada foi de tamanho {len(matriz_adj)}x{len(matriz_adj[0])}: {matriz_adj}\n')
        log.write(f'Os rios identificados foram {len(lista_rio)}: {lista_rio}\n')
        log.write(f'As posições visitadas foram {len(visitadas)}: {visitadas}\n')
    return caminho_log

def percorre_matriz(matriz):
    mostra_matriz(matriz)
    print('\nPercorrendo a matriz...')
    matriz_adj = []
    matriz_aux = []
    lista_rio = []
    visitadas = []
    y = len(matriz)
    x = len(matriz[0])

    def verifica_vizinho(matriz, i, j, lista_rio_aux):
        if tuple((i,j)) not in visitadas:
            if i < 0 or i >= y or j < 0 or j >= x:
                return
            else:
                visitadas.append((i,j))
                if matriz[i][j] == 1:
                    lista_rio_aux.append(matriz[i][j])
                    verifica_vizinho(matriz, i+1, j, lista_rio_aux)
                    verifica_vizinho(matriz, i-1, j, lista_rio_aux)
                    verifica_vizinho(matriz, i, j+1, lista_rio_aux)
                    verifica_vizinho(matriz, i, j-1, lista_rio_aux)
        return lista_rio_aux

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            retorno_lista_rio = verifica_vizinho(matriz, i, j, [])
            matriz_aux.append(matriz[i][j])
            if len(retorno_lista_rio) != 0:
                lista_rio.append(len(retorno_lista_rio))
        matriz_adj.append(matriz_aux)
        matriz_aux = []
    if len(lista_rio) >= 2:
        print(f'Foram encontrados {len(lista_rio)} rios com os tamanhos: {sorted(lista_rio)}')
    else:
        print(f'Foi encontrado {len(lista_rio)} rio com o tamanho: {sorted(lista_rio)}')

    caminho_log = gera_log(matriz, matriz_adj, lista_rio, visitadas)
    print(f'***** Não se esqueça de verificar o log {caminho_log}.')

    cmap = ListedColormap(['g', 'c']) # Queria colocar marrom p as ilhas mas não consegui
    plt.matshow(matriz, cmap=cmap)
    azul = mpatches.Patch(color='c', label='Rio')
    verde = mpatches.Patch(color='g', label='Ilha')
    plt.legend(handles=[azul, verde])
    plt.show()
    
    return lista_rio, visitadas, caminho_log

def solicita_valida_entrada():
    mensagem = '''
    1. Definir tamanho da matriz
    2. Colar matriz pronta(lista)
    3. Ver estatísticas da execução
    4. Ver log
    0. Sair
    '''
    opcao = input(mensagem)
    
    while not opcao.isdigit() or int(opcao) < 0 or int(opcao) > 6:
        print("Opção digitada inválida. Digite novamente.")
        opcao = input(mensagem)
    opcao = int(opcao)

    return opcao

def menu():
    opcao = solicita_valida_entrada()
    while opcao != 0: # Sair
        if opcao == 1: # Definir tamanho da matriz
            y = int(input('Digite um valor inteiro para y: '))
            x = int(input('Digite um valor inteiro para x: '))
            tempo_inicio = dt.datetime.now()
            matriz_gerada = gera_matrix(y, x)
            lista_rio, visitadas, caminho_log = percorre_matriz(matriz_gerada)
            tempo_final = dt.datetime.now()

        elif opcao == 2: # Colar matriz pronta(lista)
            # matriz_colada = [input('Cole a matriz aqui: ')]
            # mostra_matriz(matriz_colada)
            # percorre_matriz(matriz_colada)
            ### Não deu tempo de fazer essa opção.
            print("\nOPS!!! Esta funcionalidade está prevista para a sprint 2.")
            
        elif opcao == 3: # Ver estatísticas da execução
            try: # If
                len(matriz_gerada) == 0
            except: # Caso ela não exista ainda
                print("Você deve executar a opcão 1 primeiro.")
            else:
                print("\nEstatísticas da execução:")
                print(f"\tO menor rio encontrado foi: {min(lista_rio)}")
                print(f"\tO maior rio encontrado foi: {max(lista_rio)}")
                print(f"\tA média do tamanho dos rios é: {round(sum(lista_rio) / len(lista_rio), 2)}")
                print(f"\tA quantidade de 1 encontrado foi: {sum(lista_rio)}")
                print(f"\tA quantidade de posições visitadas foi: {len(visitadas)}")
                print(f"\tO tempo de execução foi de: {tempo_final-tempo_inicio}")
                
        elif opcao == 4: # Ver log
            try:
                arq = open(caminho_log)
            except: #FileNotFoundError:
                print('Erro: Arquivo de log não encontrado.\nExecute a opção 1 ao menos 1 vez.')
            else:
                with open(caminho_log, encoding='UTF-8') as log:
                    print(log.read())
            
        opcao = solicita_valida_entrada()

    print("Tchau, obrigado.\n")

menu()