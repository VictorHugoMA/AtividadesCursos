velocidade = float(input('Velocida do carro: '))

if velocidade>80:
    print('Voce foi multado!')
    multa = (velocidade-80)*7
    print('Valor da multa: R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')