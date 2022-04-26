#dicionario
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m'
}

print('\033[1;30;42mOla Mundo!\033[m')
print('\033[4;31mOla Mundo!\033[m')
print('\033[0;30;45mOla Mundo!\033[m')
print('\033[7mOla Mundo!\033[m')

a = 5

print('Valor = \033[4;31m{}\033[m'.format(a))
print('Valor = {}{}{}'.format('\033[4;31m',a, '\033[m'))
print('Valor = {}{}{}'.format(cores['amarelo'],a, cores['limpa']))
