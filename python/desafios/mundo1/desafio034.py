# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. - aula 10
from time import sleep

sal = float(input('Digite o salário do funcionário: R$'))
print('=*' * 15)
sleep(1)
print('Calculando...')
sleep(1)
print('Aguarde!')
sleep(1)
print('...')
sleep(1)
print('=*' * 35)
sleep(1)
print('PRONTO!')
if sal <= 1250.00:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('O funcionário que ganhava R${:.2f} passa a receber R${:.2f}.'.format(sal, novo))
