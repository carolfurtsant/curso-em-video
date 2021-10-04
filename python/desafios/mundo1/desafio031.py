# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas. - aula 10
from time import sleep
distância = float(input(' Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
sleep(1)
print('Calculando...')
sleep(2)
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}!'.format(preço))
