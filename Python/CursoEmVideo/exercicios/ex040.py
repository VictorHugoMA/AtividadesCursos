nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

if media >= 6:
    print(f'Media: {media:.2f}. Aluno aprovado')
else:
    print(f'Media: {media:.2f}. Aluno reprovado')