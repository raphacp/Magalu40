# import pathlib
# import os
# #print(f'\nCaminho: \"{pathlib.Path.cwd()}\"')

# # path1 = pathlib.Path.cwd()
# # print('\nCaminho: ', path1)
# # path1.joinpath('Rapha.txt')
# # print('\nCompleto: ', path1)
# # path1 = str(path1)+'Rapha.txt'
# # print('\nCompleto 2: ', path1)

# caminho = os.path.abspath('.')
# arquivo = 'Rapha.txt'

# comp = os.path.abspath('.')+os.sep+'Rapha.txt'
# print(comp)
# # caminho_completo = caminho+os.sep+arquivo
# # print(caminho_completo)
# #print(f'{path1}{os.sep}Rapha.txt')



import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

cmap = ListedColormap(['g', 'c'])
plt.matshow(matrix, cmap=cmap)
azul = mpatches.Patch(color='c', label='Rio')
verde = mpatches.Patch(color='g', label='Ilha')
plt.legend(handles=[azul, verde])
plt.show()
