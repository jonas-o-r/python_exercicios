#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
#que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 = str(input('Informe o nome do aluno 1: '))
a2 = str(input('Informe o nome do aluno 2: '))
a3 = str(input('Informe o nome do aluno 3: '))
a4 = str(input('Informe o nome do aluno 4: '))
lista = random.sample([a1, a2, a3, a4],4)
print(f'A ordem de apresentação dos trabalhos será: {lista}')

