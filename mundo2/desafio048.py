# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.- aula 13
soma = 0
contagem = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        contagem += 1
        soma += cont
print('A soma de todos os {} valores múltiplos de 3 é {}.'.format(contagem, soma))
