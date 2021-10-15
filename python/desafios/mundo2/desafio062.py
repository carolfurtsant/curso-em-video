# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele quer mostrar 0 (zero) termos. - aula 14
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        contador += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finaliazada com {} termos mostrados.'.format(total))

