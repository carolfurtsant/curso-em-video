#  Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
Menor = 0
Maior = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        Maior = peso
        Menor = peso
    else:
        if peso > Maior:
            Maior = peso
        if peso < Menor:
            Menor = peso
print('O maior peso lido foi de {}Kg.'.format(Maior))
print('O menor peso lido foi de {}kg.'.format(Menor))
