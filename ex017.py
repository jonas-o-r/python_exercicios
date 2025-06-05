#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo e calcule a hipotenusa
import math
from math import hypot

co = float(input('Qual o comprimento do Cateto Oposto? '))
ca = float(input('Qual o comprimento do Cateto Adjacente? '))
'''hip = math.sqrt((math.pow(co, 2)) + (math.pow(ca, 2)))
print(f'A hipotenusa mede: {hip:.2f}.')'''
hi = math.hypot(co, ca)
print(f'A hipotenusa mede: {hi:.2f}')
