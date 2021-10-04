# Faça um programa que leia três números e mostre qual é o maior e qual é o menor. - aula 10

from time import sleep

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
print('-==-' * 10)
print('Analisando...')
print('-==-' * 10)
sleep(2)
# Analisando menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Analisando maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número digitado foi {}!'.format(menor))
print('O maior número digitado foi {}!'.format(maior))
