# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Qual seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
print('O IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('CUIDADO! ABAIXO DO PESO NORMAL.')
elif 18.5 <= imc < 25:
    print('PARABÉNS! VOCÊ ESTÁ COM PESO IDEAL.')
elif 25 <= imc < 30:
    print('CUIDADO! VOCÊ ESTÁ COM SOBREPESO.')
elif 30 <= imc < 40:
    print('CUIDADO! VOCÊ ESTÁ EM OBSIDADE!')
else:
    print('CUIDADO! VOCÊ ESTÁ EM OBESIDADE MÓRBIDA.')