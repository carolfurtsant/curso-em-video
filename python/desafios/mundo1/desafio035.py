# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo. - AULA 10
from time import sleep
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
sleep(1)
r1 = float(input('Seguimento 1: '))
r2 = float(input('Seguimento 2: '))
r3 = float(input('Seguimento 3: '))
print('-=' * 20)
sleep(1)
print('Analisando...')
print('-=' * 20)
sleep(1)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses seguimentos acima PODEM FORMAR um triângulo')
else:
    print('Esses seguimentos acima NÃO PODEM FORMAR um triângulo')