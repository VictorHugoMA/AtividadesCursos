a = int (input('Segmento 1: '))
b = int (input('Segmento 2: '))
c = int (input('Segmento 3: '))

if a<b+c and b<a+c and c<a+b:
    print('É possível formar um triângulo', end=' ')
    if a==b==c:
        print('Equilatero')
    elif a!=b!=c!=a:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Não é possível formar um triângulo')