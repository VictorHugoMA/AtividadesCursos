n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divi = n1 // n2
rest = n1 % n2
exp = n1 ** n2

print('\nSoma: {}\nMultiplicação: {}\nDivisão: {:.3f}\nDivisão Inteira: {}\nResto da divisão: {}\nExponenciação: {}'
.format(soma, mult, div, divi, rest, exp))

#juntar dois print
print('Teste', end=' ')
print('Final')