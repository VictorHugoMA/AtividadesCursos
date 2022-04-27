valorCasa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
anos = int(input('Digite em quantos anos deseja pagar: '))

prestacao = valorCasa/(anos*12)
limite = salario*0.3

print(f'Para pagar uma casa de R${valorCasa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}')
print(f'Limite da prestacao R$ {limite:.2f}')

if limite>=prestacao:
    print('Empréstimo pode ser concedido')
else:
    print('Empréstimo não pode ser concedido')