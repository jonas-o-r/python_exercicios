#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a 1250, aumento de 10%, para inferiores o aumento é de 15%
sal = float(input('Informe o salário: '))
if sal <= 1250:
    print(f'O aumento será de R${sal * 0.15:.2f} e o novo salário será R${sal * 1.15:.2f}.')
else:
    print(f'O aumento será de R${sal * 0.1:.2f} e o novo salário será R${sal * 1.1:.2f}.')
