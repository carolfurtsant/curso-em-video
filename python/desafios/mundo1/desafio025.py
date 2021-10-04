#  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. aula - 09

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}.'.format('silva' in nome.lower()))

