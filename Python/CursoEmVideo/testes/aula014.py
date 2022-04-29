c = 0
while c<5:
    print(c)
    c += 1
print('FIM')

num = int(input('Digite um numero (0 para finalizar): '))
while num != 0:
    print(num)
    num = int(input('Digite um numero: '))
print('FIM')

numPI = 1
par = impar = 0
while numPI != 0:
    numPI = int(input('Digite um numero: '))
    if numPI != 0:
        if numPI%2==0:
            par += 1
        elif numPI%2!=0:
            impar += 1
print('Voce digitou {} numeros pares e {} numeros impares'.format(par, impar))
print('FIM')