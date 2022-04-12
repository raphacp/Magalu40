import collections
import csv

def copia_cria_arquivo_media(arquivo):
    with open(arquivo, encoding='UTF-8', newline='') as arq:
        alunos = csv.DictReader(arq)
        with open('alunos_media.csv', 'w', encoding='UTF-8', newline='') as arq_1:
            arq_csv = csv.writer(arq_1)
            for linha in alunos:
                media = 0
                media = (float(linha[3]) + float(linha[4]) + float(linha[5]) + float(linha[6])/4)
                arq_csv.writerow(linha)
                print(media)

#copia_cria_arquivo_media('alunos.csv')

copia_cria_arquivo_media('C:\\Python\\Magalu40\\840 Desenvolve 40 Python\\3 -Estruturas de Dados\\alunos.csv')

