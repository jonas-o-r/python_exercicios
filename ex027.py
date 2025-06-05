#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite o nome completo: '))
s = nome.split()
print(len(s))
print(f'Primeiro nome: {s[0]}')
print(f'Último nome: {s[len(s)]}')

