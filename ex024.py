#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cit = str(input('Informe o nome da cidade: '))
print(f'{'santo' in cit.lower().split()[0]}')

