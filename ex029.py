#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 para cada Km/h acima do limite.
lim = int(80)
spd = int(input('Velocidade: '))
if spd > 80:
    print(f'Você foi multado em R${(spd - 80) * 7}.')
