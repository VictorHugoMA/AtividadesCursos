preco = float(input('Digite o preco da compra: '))

print("""FORMAS DE PAGAMENTO:
[ 1 ] à Vista Dinheiro / Cheque
[ 2 ] à Vista no Cartão de Crédito
[ 3 ] 2x no Cartão de Crédito
[ 4 ] 3x ou mais no Cartão de Crédito""")

opcao = int(input('Qual a sua opcao: '))

if opcao == 1:
    print(f'Valor R${preco*0.9:.2f}')
elif opcao == 2:
    print(f'Valor R${preco*0.95:.2f}')
elif opcao == 3:
    print(f'Valor R${preco:.2f}')
elif opcao == 4:
    print(f'Valor R${preco*1.2:.2f}')
else:
    print('Opcao Invalida')