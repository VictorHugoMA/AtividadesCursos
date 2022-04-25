distanciaKM = float(input('Digite a distância em KM: '))

if distanciaKM <=200:
    preco = distanciaKM * 0.5
else:
    preco = distanciaKM * 0.45

print('O preço da passagem é R${:.2f}'.format(preco))