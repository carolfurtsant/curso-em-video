# Crie um programa que eia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag). - aula 14
n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Acabou!'
      '\nVocê digitou {} números e a soma entre eles foi {}.'.format(cont, soma))