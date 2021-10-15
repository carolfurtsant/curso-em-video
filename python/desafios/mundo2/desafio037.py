# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. - aula 012

print('-=' * 20)
print('===== Conversor de base numéricas ======')
print('-=' * 20)

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
      [ 1 ] Converter para BINÁRIO
      [ 2 ] Converter para OCTAL
      [ 3 ] Converter para HEXADECIMAL)''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')
