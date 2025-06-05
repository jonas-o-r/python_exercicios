#Faça um programa que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento.
sal = float(input('Qual o salário atual?'))
print(f'O salário com aumento será de: R${sal+(sal*0.15):.2f}')