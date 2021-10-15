# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os primeiros termos da progressão usando
# a estrutura while. - aula 014
"""
prim = int(input('Primeiro Termo: '))
raz = int(input('Razão: '))
déc = prim + (10 - 1) * raz
for c in range(prim, déc, raz):
    print('{}'.format(c), end=' >> ')
print('FIIIIIM!')
"""
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
termo = primeiro
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    contador += 1
print('FIM!')
