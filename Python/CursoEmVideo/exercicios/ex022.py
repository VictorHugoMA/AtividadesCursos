nomeCompleto = input('Digite seu nome completo: ')

print(nomeCompleto.upper())
print(nomeCompleto.lower())
print(len(nomeCompleto.replace(' ', '')))

nomePartes = nomeCompleto.split()
print(len(nomePartes[0]))