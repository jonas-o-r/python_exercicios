#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Informe o nome completo: '))
print(f'Nome: {nome}')

print(f'{'silva' in nome.lower()}')
