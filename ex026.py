#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
fr = str(input('Digite uma frase: ')).strip()
print(f'Quantidade de letras "A": {fr.lower().count('a')}')
print(f'Posição do primeiro "A": {fr.lower().find('a')+1}')
print(f'Posição do último "A": {fr.lower().rfind('a')+1}')



