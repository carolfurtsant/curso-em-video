# Escreva um programa que leia um valor em metros e exiba convertido em centímetro e milímetros.

#km hm dam m dm cm mm

medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a:\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm.'.format(medida, km, hm, dam, dm, cm, mm))
