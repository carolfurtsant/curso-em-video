# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. - aula 10
from datetime import date
from time import sleep
ano = int(input('Digite o ano que você quer analisar ou digite 0 para analisar o ano atual: '))
print('Analisando...')
sleep(1)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))
