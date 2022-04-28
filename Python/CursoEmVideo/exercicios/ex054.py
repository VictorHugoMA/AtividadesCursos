from datetime import date

anoAtual = date.today().year
maioridade = 0
menoridade = 0

for i in range(1, 8):
    anoNascimento = int(input('Digite o ano de nascimento: '))
    idade = anoAtual - anoNascimento
    if idade>=18:
        maioridade+=1
    else:
        menoridade+=1

print(f'O grupo tem {maioridade} pessoar maiores de 18 e {menoridade} menores de 18')
