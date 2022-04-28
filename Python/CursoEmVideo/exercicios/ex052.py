num = int(input('Digite um número: '))
totalDivisao = 0

for i in range(1, num+1):
    if num%i==0:
        print('\033[32m', end='')
        totalDivisao+=1
    else:
        print('\033[31m', end='')
    print(f'{i}', end=' ')

print('\033[m\n', end='')
if totalDivisao==2:
    print(f'O numero {num} eh primo')
else:
    print(f'O numero {num} nao eh primo')




