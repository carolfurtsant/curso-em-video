# Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer. - aula 14
"""
Desafio 028:
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
"""
from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em número entre 0 e 10'
      '\nSerá que você consegue acertar?')
acerto = False
palpites = 0
while not acerto:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acerto = True
    else:
        if jogador < computador:
            print('Mais...')
        elif jogador > computador:
            print('Menos...')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))