# Crie um programa que leia o nome completo de uma pessoa e mostre: - aula 09
""" O nome com todas as letras maiúsculas
 O nome com todas as letras minúsculas
 Quantas letras ao td (sem considerar espaços)
 Quantas letras o primeiro nome """
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('O seu nome com todas as letras maiúsculas: {}.'.format(nome.upper()))
print('O seu nome com todas as letras minúsculas: {}.'.format(nome.lower()))
print('O seu nome contém {} letras.'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
