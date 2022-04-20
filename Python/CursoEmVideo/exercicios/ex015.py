qtdDias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
qtdKM = float(input('Digite a quantidade de KM rodados: '))

precoTotal = qtdDias*60 + qtdKM*0.15

print('O preço total do aluguel é de R${:.2f}'.format(precoTotal))