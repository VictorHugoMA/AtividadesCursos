peso = float(input('Digite o peso (kg): '))
altura = float(input('Digite a altura (m): '))

imc = peso/(altura**2)

print(f'IMC: {imc:.2f}')

if imc<18.5:
    print('Classificacao: Magreza')
elif imc<25:
    print('Classificacao: Normal')
elif imc<30:
    print('Classificacao: Sobrepeso')
elif imc<40:
    print('Classificacao: Obesidade')
else:
    print('Classificacao: Obesidade Grave')