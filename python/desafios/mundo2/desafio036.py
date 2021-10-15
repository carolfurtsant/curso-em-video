# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. - aula 12
from time import sleep

print('-=' * 20)
casa = float(input('Insire o valor da casa: R$'))
sal = float(input('Insire o valor do salário: R$'))
anos = int(input('Insere os anos de financiamento? '))
print('-=' * 20)
sleep(1)

prestação = casa / (anos * 12)
mínimo = sal * 30 / 100

print('Calculando...')
sleep(2)

print('-=' * 40)
sleep(1)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}.'.format(prestação))
sleep(1)
print('-=' * 40)

print('Aguarde o resultado...')
sleep(2)
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
