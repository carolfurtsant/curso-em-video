# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com pausa de 1 segundo entre eles. - aula 013
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('FIM!')