salario = float(input('Digite o salario: '))

if salario>1250:
    print('O novo salario com aumento de 10% é R${:.2f}'.format(salario*1.1))
else:
    print('O novo salario com aumento de 15% é R${:.2f}'.format(salario*1.15))