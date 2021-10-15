# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. - aula 13
n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;32m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\033[m\nO número {} foi divisível {} vezes.'.format(n, total))
if total == 2:
    print('E por isso ele \033[1;33mÉ PRIMO!!\033[m')
else:
    print('E por isso ele \033[1;31mNÃO É PRIMO!!\033[m')
