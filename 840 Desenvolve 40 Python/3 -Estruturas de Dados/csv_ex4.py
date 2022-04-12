import csv

with open('alunos.csv', encoding='UTF-8') as orig, open('alunos_media.csv', 'w', encoding='UTF-8') as novo:
    # a conversão para lista na linha abaixo é para facilitar uma "jogada" que usaremos
    alunos = list(csv.DictReader(orig))

    arq_novo = csv.writer(novo)

    # essa é a jogada! vamos pegar as *chaves* de um aluno qualquer da lista
    cabecalhos = list(alunos[0].keys()) + ['Média']
    # dessa maneira podemos escrever os cabecalhos das colunas na primeira 
    # linha da tabela
    arq_novo.writerow(cabecalhos)

    for aluno in alunos:        
        # cálculo da média para o aluno
        media = (float(aluno['Prova_1']) + float(aluno['Prova_2']) + float(aluno['Prova_3']) + float(aluno['Prova_4']))/4

        # adiciona um par chave-valor ao dicionário do aluno
        aluno.update({'Média': media})

        # por fim escrevemos os *valores* do dicionário 'aluno' no arquivo
        arq_novo.writerow(aluno.values())