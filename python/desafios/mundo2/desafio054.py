# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores. - aula - 013
from datetime import date
atual = date.today().year
toMaior = 0
toMenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em qual ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        toMaior += 1
    else:
        toMenor += 1
print('Ao todo tivemos:'
      '\n {} pessoas maiores de idade.'.format(toMaior))
print('E tivemos:'
      '\n {} pessoas menores de idade.'.format(toMenor))

