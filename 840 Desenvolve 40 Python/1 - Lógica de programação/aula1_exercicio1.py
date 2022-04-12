# - Imagine que você vai fazer uma viagem entre duas cidades 
# e irá parar um certo tempo para descanso e almoço. 
# Faça um programa que calcule o tempo total de viagem, levando em conta a distância
# entre as cidades, velocidade do carro e tempo de descanso.

# Distância (km)
# Velocidade (km/h)
# Tempo de descanso (h)

distanica = float(input("Digite a distância entre as cidades(km): "))
velocidade = float(input("Digite a velocidade do veículo (km/h): "))
tempo_descanso = float(input("Digite o tempo de descanso(h): "))

tempo_total = distanica/velocidade + tempo_descanso

print("O tempo total de viagem será:", tempo_total)
print (f"O tempo total de viagem será: {tempo_total:.2f} horas")

# o round arredonda o número e guarda ele assim. O :.2f arredonda só na mensagem, o número é armazenado completo

# exibir em hh:mm

horas = int(tempo_total)
minutos = int((tempo_total - horas) *60)
#print(horas)
#print(minutos)
print(f"O tempo total da viagem será de {horas} horas e {minutos} minutos.")