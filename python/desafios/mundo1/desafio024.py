# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO". - aula 09

cidade = str(input('Digite a cidade em que você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')