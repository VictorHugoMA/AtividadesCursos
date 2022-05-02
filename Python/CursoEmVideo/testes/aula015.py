soma = 0
while True:
    num = int(input('Digite um numero: '))
    if num == 0:
        break
    soma += num

print('A soma dos numeros é: {}'.format(soma))
print('FIM')

# f String Format teste - interpolacao de string
teste = 3.1415
print(f'Teste f String: {teste:.2f} e {teste}')