cidade = input('Digite o nome da cidade: ')

cidadeDividido = cidade.split()

#print('A cidade começa com "Santo"? {}'.format('SANTO' in cidadeDividido[0].upper()))

#maneira mais correta
print('A cidade começa com "Santo"? {}'.format('SANTO' == cidade[:5].upper()))