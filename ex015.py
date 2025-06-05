#Escreva um programa que pergunte a qtd de Km rodados por um carro alugado e a qtd de dias.
#Calcule o preço a pagar pela locação sabendo que a diária custa R$60 e o kM rodado R$0.15.
dia = int(input('Quantos dias o carro foi utilizado? '))
km = float(input('Quantos Km o carro percorreu? '))
print(f'O valor a ser pago pela locação é de: R${((dia*60) + (km*0.15)):.2f}')
