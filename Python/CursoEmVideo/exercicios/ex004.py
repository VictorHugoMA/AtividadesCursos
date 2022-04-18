var = input('Digite algo: ')

print('{} é {}, Numerico: {}, Letra: {}, Minúsculo: {}'
.format(var, type(var), var.isnumeric(), var.isalpha(), var.islower()))