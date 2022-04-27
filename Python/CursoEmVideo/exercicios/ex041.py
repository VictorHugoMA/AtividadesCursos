from datetime import date

anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

print(f'Idade: {idade}')

if idade<=9:
    print('Categoria: Mirim')
elif idade<=14:
    print('Categoria: Infantil')
elif idade<=19:
    print('Categoria: Junior')
elif idade<=25:
    print('Categoria: Senior')
else:
    print('Categoria: Master')