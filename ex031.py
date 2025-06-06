#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, corando R$0,50 por Km para viagens de até 200km e R$0,45 para mais longas.
dist = float(input('Qual a distância da viagem? '))
if dist <= 200:
    print(f'O preço da passagem será: R${dist * 0.5:.2f}.')
else:
    print(f'O preço da passagem será: R${dist * 0.45:.2f}.')
