#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
import math
num = int(input('Informe um número: '))
if (num / 2) == (num // 2):
    print('O número é PAR!')
else:
    print('O número é ÍMPAR!')