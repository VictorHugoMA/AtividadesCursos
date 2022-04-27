from datetime import date

anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

print(f'Idade: {idade}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você se alistar')
