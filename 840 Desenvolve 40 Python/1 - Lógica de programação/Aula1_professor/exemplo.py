# - Imagine que você vai fazer uma viagem entre duas cidades 
# e irá parar um certo tempo para descanso e almoço. 
# Faça um programa que calcule o tempo total de viagem, levando em conta a distância
# entre as cidades, velocidade do carro e tempo de descanso.

# Distância (km)
# Velocidade (km/h)
# Tempo de descanso (h)

distancia = float(input("Digite a distância entre as cidades(km): "))
velocidade = float(input("Digite a velocidade do veículo(km/h): "))
tempo_de_descanso = float(input("Digite o tempo de descanso(h): "))

tempo_total = distancia/velocidade + tempo_de_descanso 

horas = int(tempo_total)

#minutos = int((tempo_total - int(tempo_total)) * 60)
minutos = int((tempo_total % int(tempo_total)) * 60)
print(horas)
print(minutos)
#print("O tempo total de viagem será", tempo_total, "horas")
print(f"O tempo total de viagem será {tempo_total:.2f} horas")
print(f"O tempo total de trajeto será de {horas}h e {minutos}min")