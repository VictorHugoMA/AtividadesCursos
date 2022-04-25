import random

numAleatorio = random.randint(0,5)
numEscolhido = int(input('Digite um numero de 0 a 5: '))

if numAleatorio==numEscolhido:
    print('Acertou!')
else:
    print('Errou!')
    print('O numero correto era {}'.format(numAleatorio))