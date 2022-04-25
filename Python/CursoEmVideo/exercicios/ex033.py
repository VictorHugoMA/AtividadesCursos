num1 = int (input('Número 1: '))
num2 = int (input('Número 2: '))
num3 = int (input('Número 3: '))

if(num1>num2):
    if(num1>num3):
        maior = num1
    else:
        maior = num3
else:
    if(num2>num3):
        maior = num2
    else:
        maior = num3

if(num1<num2):
    if(num1<num3):
        menor = num1
    else:
        menor = num3
else:
    if(num2<num3):
        menor = num2
    else:
        menor = num3

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))