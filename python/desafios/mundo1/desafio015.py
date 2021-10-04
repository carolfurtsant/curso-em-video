# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. - aula 07

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
precoDiarias = float(input('Qual valor da diária? R$'))
precoKm = float(input('Qual é o valor por Km rodado? R$'))
pago = (dias * precoDiarias) + (km * precoKm)

print('O total do valor a pagar é de R${:.2f}'.format(pago))
