# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. - aula 09

nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}!'.format(n[0]))
print('Seu último nome é {}!'.format(n[len(n) - 1]))
