# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. - aula 07

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parde: '))
área = larg * alt

print('Sua parede tem a dimensão de {:.1f}x{:.2f} e a sua área é de {:.1f}m².'.format(larg, alt, área))

tinta = área / 2

print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
