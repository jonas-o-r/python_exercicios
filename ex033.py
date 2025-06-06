#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = float(input('Informe o 1ª número: '))
b = float(input('Informe o 2ª número: '))
c = float(input('Informe o 3ª número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
