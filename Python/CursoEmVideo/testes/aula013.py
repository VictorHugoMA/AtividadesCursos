for i in range(0,10):
    print(i)
print('FIM')

for c in range(5, 0, -1):
    print(c)

n = int(input('Digite um numero de fim: '))

for i in range(0, n+1):
    print(i)

soma = 0
for i in range(0, 4):
    num = int(input('Digite um numero a ser somado: '))
    soma += num
print('A soma dos numeros é: {}'.format(soma))