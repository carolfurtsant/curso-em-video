# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. - aula 07

sal = float(input('Qual é o salário do funcionário? R$'))
porc = int(input('Aumento de quantos porcentos (%)? '))
novo = sal + (sal * porc / 100)

print('O funcionário que recebia R${:.2f}, com {}% de aumento, passa a receber R${:.2f}.'.format(sal, porc, novo))

dif = novo - sal

print('Diferença de R${:.2f}.'.format(dif))
