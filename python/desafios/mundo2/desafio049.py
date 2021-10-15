# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for. - aula 13
n = int(input('Digite um número para ver sua tabuada: '))
for tab in range (0, 11):
    print('{} x {:1} = {}'.format(n, tab, n*tab))