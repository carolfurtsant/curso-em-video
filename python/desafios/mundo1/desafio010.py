# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. - aula 07

# Considere US$1,00 = R$5,37

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.37
euro = real / 6.22

print('Com R${:.2f} você pode comprar: '
      '\nUS${:.2f}'
      '\nEUR${:.2f}'.format(real, dolar, euro))
