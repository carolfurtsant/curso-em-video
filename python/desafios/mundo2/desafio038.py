# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais - aula 012

print('-=' * 15)
print('===== Comparando números =====')
print('-=' * 15)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior.')
elif n2 > n1:
    print('O SEGUNDO valor é maior.')
else:
    print('Não existe valor maior, os dois são IGUAIS!')