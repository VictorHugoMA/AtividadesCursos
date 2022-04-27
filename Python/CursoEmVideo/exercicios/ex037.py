num = int(input('Digite um número: '))
print('Digite a base de conversao: \n1 - Binário \n2 - Octal \n3 - Hexadecimal')
escolha = int(input('Sua opcao: '))

if escolha == 1:
    print(f'Binario: {bin(num)[2:]}')
elif escolha == 2:
    print(f'Octal: {oct(num)[2:]}')
elif escolha == 3:
    print(f'Hexadecimal: {hex(num)[2:]}')
else:
    print('Opção inválida')