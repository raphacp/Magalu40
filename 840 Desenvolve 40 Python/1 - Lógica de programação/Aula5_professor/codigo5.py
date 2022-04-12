frutas = {
    0: 'uva',
    1: 'maçã'
}

print(frutas[1])

alunos = {
    'paulo': {
        'nota': 8,
        'presença': 80
    },
    'matheus':{
        'nota': 9,
        'presença': 70
    }
}

#            nota      presença
# paulo        8          80
# matheus      9          70
#
print(alunos['matheus']['presença'])

alunos['matheus']['média'] = 8.7
print(alunos)