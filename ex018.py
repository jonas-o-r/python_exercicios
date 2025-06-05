#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.
from math import radians, sin, cos, tan
x = float(input('Informe um ângulo em grausº: '))
xr = radians(x)
print(f'Seno: {sin(xr):.2f}')
print(f'Cosseno: {cos(xr):.2f}')
print(f'Tangente: {tan(xr):.2f}')

