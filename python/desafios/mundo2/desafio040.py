# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO - aula 012

print('*' * 29)
print('**********  Média  **********')
print('*' * 29)
nome = str(input('Digite o nome do aluno: '))
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
m = (nota_1 + nota_2) / 2
if m >= 7:
    print('{} está APROVADO!'.format(nome))
    print('Sua média é {:.1f}!'.format(m))
elif m < 5:
    print('{} está REPROVADO!'.format(nome))
    print('Sua média é {:.1f}!'.format(m))
else:
    print('{} está de RECUPREAÇÃO!'.format(nome))
    print('Sua média é {:.1f}!'.format(m))
