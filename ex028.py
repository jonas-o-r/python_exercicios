#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu o perdeu.
import random
srt = random.randint(0,5)
print('Um número de 0 a 5 foi sorteado! Consegue adivinhar?')
bet = int(input('Qual foi o número sorteado? '))
if bet == srt:
    print('Parabéns! Você acertou!')
else:
    print(f'Não foi dessa vez, o número era: {srt}.')
print('Obrigado por jogar!')
