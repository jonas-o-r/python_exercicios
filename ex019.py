#Um professor quer sortear um de seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome escolhido.
import random
a1 = str(input('Informe o nome do aluno 1: '))
a2 = str(input('Informe o nome do aluno 2: '))
a3 = str(input('Informe o nome do aluno 3: '))
a4 = str(input('Informe o nome do aluno 4: '))
s = random.choice([a1, a2, a3, a4])
print(f'O aluno sorteado para apagar o quadro foi: {s}!')
