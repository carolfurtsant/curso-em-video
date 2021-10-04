# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu. - aula 10
from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador "PENSAR"
print('-==-' * 20)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('-==-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS!!! Você conseguiu me vencer!')
else:
    print('GANHEI!!! Eu pensei no número {} e não no número {}!'.format(computador, jogador))
