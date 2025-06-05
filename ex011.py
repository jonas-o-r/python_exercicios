#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade necessária de tinta para pintá-la, sabendo que 1L de tinta rende 2m².
a = float(input('Qual a altura da parede?'))
l = float(input('Qual a largura da parede?'))
area = a * l
tinta = area/2
print(f'Você irá precisar de {tinta:.2f}L de tinta para pintar a parede!')
