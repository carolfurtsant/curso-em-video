# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.- aula 013
sumIdade = 0
medIdade = 0
maiorIdadeM = 0
nomeVelho = ''
mulheres_20 = 0
for pessoa in range(1, 5):
    print('====== {}ª PESSOA ====='.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [ M / F ]: ')).strip()
    sumIdade += idade
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeM = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeM:
        maiorIdadeM = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_20 += 1
medIdade = sumIdade / 4
print('A média de idade do grupo é de {} anos.'.format(medIdade))
print('O homem mais velho é:'
      '\n {} e tem {} anos.'.format(nomeVelho, maiorIdadeM))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulheres_20))
