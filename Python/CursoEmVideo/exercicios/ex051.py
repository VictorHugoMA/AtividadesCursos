print('10 PRIMEIROS TERMOS DE UMA PA')
primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = primeiroTermo+(10-1)*razao

for i in range(primeiroTermo, decimo+razao, razao):
    print(f'{i}', end=' -> ')

print('FIM')