import random
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

print("""Opcoes
[1] Pedra
[2] Papel
[3] Tesoura""")
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
sleep(1)
jogador = int(input('Sua escolha: '))
comp = random.randint(0,2)

print(f'Voce escolheu: {itens[jogador]}')
print(f'Computador escolheu: {itens[comp]}')

if comp == jogador:
    print('Empate')
if comp == jogador-1:
    print('GANHOU')
if comp == 3 and jogador == 1:
    print('GANHOU')
if comp == jogador+1:
    print('PERDEU')
if jogador == 3 and comp == 1:
    print('PERDEU')
