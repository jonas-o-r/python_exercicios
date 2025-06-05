#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = str(input('Informe um número: '))
print(f'Número: {num}')
print(f'Milhares: {num[len(num)-4]}')
print(f'Centenas: {num[len(num)-3]}')
print(f'Dezenas: {num[len(num)-2]}')
print(f'Unidades: {num[len(num)-1]}')

