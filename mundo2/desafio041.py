# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER - aula 012
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

# categorias:
mirim = 9
infantil = 14
júnior = 19
sênior = 25

# condicionais:
if idade <= mirim:
    print('O atleta tem {} anos e está na categoria MIRIM!'.format(idade))
elif idade <= infantil:
    print('O atleta tem {} anos e está na categoria INFANTIL!'.format(idade))
elif idade <= júnior:
    print('O atleta tem {} anos e está na categoria JÚNIOR!'.format(idade))
elif idade <= sênior:
    print('O atleta tem {} anos e está na categoria SÊNIOR!'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria MASTER!'.format(idade))
