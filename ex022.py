#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas;
#Quantas letras tem o nome inteiro e quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Nome em maiúsculo: {nome.upper()}.')
print(f'Nome em minúsculo: {nome.lower()}.')
print(f'O nome completo tem: {len(nome) - nome.count(' ')} letras.')
print(f'O primeiro nome tem: {len(nome.split()[0])} letras.')
