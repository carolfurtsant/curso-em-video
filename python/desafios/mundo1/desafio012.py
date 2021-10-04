# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. - aula 07

prod = float(input('Qual é o preço do prdouto? R$'))
desc = float(input('Quanto será o desconto (%)? '))
novo = prod - (prod * desc / 100)
print('O produto que custava R${}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(prod, desc, novo))
