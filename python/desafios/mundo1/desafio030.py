# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR. - aula 10

n = int(input('Digite um número: '))
resultado = n % 2
if resultado == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é IMPAR.'.format(n))
