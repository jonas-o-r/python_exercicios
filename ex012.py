#Faça um programa que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.
x = float(input('Qual o preço do produto?'))
print(f'Preço original: R${x:.2f}')
print(f'Preço com desconto: R${x*0.95:.2f}')

