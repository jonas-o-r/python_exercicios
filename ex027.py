#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite o nome completo: ')).strip()
s = nome.split()
print('-.-' * 10)
print(f'Primeiro nome: {s[0]}')
print(f'Último nome: {s[len(s)-1]}')
print('-.-' * 10)
