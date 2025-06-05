#Crie um algoritmo que leia um número e mostre seu dobro, triplo e a raiz quadrada.
num = int(input('Digite um número:'))
print(f'Número: {num}')
print(f'Dobro: {num*2}')
print(f'Triplo: {num*3}')
print(f'Raiz quadrada: {num**(0.5):.2f}')
print(f'Raiz quadrada: {pow(num,(1/2)):.2f}')
