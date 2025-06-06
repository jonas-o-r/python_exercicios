#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Informe o 1ª número: '))
n2 = float(input('Informe o 2ª número: '))
n3 = float(input('Informe o 3ª número: '))
lst = [n1, n2, n3]
print(f'Maior número: {max(lst)}')
print(f'Menor número: {min(lst)}')
