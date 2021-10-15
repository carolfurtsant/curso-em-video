# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. - aula 13
prim = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
déc = prim + (10 - 1) * raz
for c in range(prim, déc, raz):
    print('{}'.format(c), end=' >> ')
print('FIIIIIM!')