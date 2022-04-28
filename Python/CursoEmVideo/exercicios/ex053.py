frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juncao = ''.join(palavras)
inverso = ''

for i in range(len(juncao)-1, -1, -1):
    inverso+=juncao[i]

if juncao==inverso:
    print('Eh um Palindromo')
else:
    print('Nao eh um Palindromo')


