# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. - aula 08

import math

an = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tang = math.tan(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(an, seno))
print('O ângulo de {} tem o COSENO de {:.2f}.'.format(an, cos))
print('O ângulo de {} tem o TANGENTE de {:.2f}.'.format(an, tang))
