#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Informe um ano: '))
if (ano / 4) == (ano // 4) and (ano / 400) == (ano // 400):
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')
