media = 0
mulher20 = 0
idadeHomemVelho = 0
contHomem = 0

for p in range(1, 5):
    print(f'---- {p}ª pessoa ----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').upper()
    media += idade

    if sexo == 'F':
        if idade < 20:
            mulher20 += 1

    if sexo == 'M':
        contHomem += 1
        if idade > idadeHomemVelho:
            idadeHomemVelho = idade
            nomeVelho = nome

media = media/4

print(f'A média de idade é de {media:.2f} anos')
if mulher20 == 0:
    print(f'Nao tem mulheres com menos de 20 anos')
else:
    print(f'Ao todo são {mulher20} mulheres com menos de 20 anos.')

if contHomem == 0:
    print('Nao tem homens no grupo')
else:
     print(f'O homem mais velho se chama {nomeVelho} e tem {idadeHomemVelho} anos.')