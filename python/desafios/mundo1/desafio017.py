# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa. - aula 08

import math

c_o = float(input('Digite o cateto oposto: '))
c_a = float(input('Digite o cateto adjacente: '))
hi = math.hypot(c_o, c_a)
print('Valor da hipotenusa é {:.2f}.'.format(hi))
