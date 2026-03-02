# Faça um programa que leia a altura e a lagura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pita uma area de 2m²

altura = float(input('Qual a altura da parede em metros: '))
largura = float(input('Qual a largura em metros: '))

area = altura * largura

qtinta = area / 2

print('A parede tem {:.2f}m² e vai precisar de {:.2f}L de tinta para pinta-la'.format(area, qtinta))