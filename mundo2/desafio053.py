# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. - aula 13
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
td = ''.join(palavras)
invers = td[::1]  # fatiamento
'''for letra in range(len(td) - 1, -1, -1):
    invers += td[letra]'''
print('O inverso de {} é {}.'.format(td, invers))
if invers == td:
    print('A frase digitada É palíndromo!!')
else:
    print('A frase NÃO É um palíndromo!!')