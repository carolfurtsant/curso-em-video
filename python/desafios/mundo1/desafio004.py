# Faça uma programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

algo = input('Digite alguma coisa: ')
print(type(algo))
print('É palavra?', algo.isalpha())
print('É número?', algo.isalnum())