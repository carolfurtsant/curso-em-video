# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, - aula 14
# peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sex o [ M / F ]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos! Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso!'.format(sexo))
