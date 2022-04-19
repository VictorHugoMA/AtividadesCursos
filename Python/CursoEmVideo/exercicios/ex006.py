import math
num = int(input('Digite um número: '))

print('\nDobro: {}\nTriplo: {}\nRaiz Quadrada: {:.3f}'.format(num * 2, num * 3, num ** (1/2)))

#outra maneira de calcular raiz quadrada
print('Raiz Quadrada (Segunda Maneira): {:.3f}'.format(math.sqrt(num)))