frase = input('Digite uma frase: ')

print('Quantas vezes aparece a letra "A": {}'.format(frase.upper().count('A')))
print('A primeira letra "R" esta na posição {}'.format(frase.upper().find('A')))
print('A ultima letra "R" esta na posição {}'.format(frase.upper().rfind('A')))