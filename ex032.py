#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Informe um ano: '))
if (ano % 4) == 0 and (ano % 400) == 0 or (ano % 100) != 0:
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')
