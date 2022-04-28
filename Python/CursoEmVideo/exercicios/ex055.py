for i in range(1, 6):
    peso = float(input('Digite o peso da pessoa {}: '.format(i)))
    if i==1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior peso eh {maior:.2f} e o menor peso eh {menor:.2f}')
