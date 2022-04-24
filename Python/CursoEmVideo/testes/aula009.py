frase = 'Curso em Vídeo Python'

print(frase[4])
print(frase[4:10])
print(frase[::2])

print("""Atuando no desenvolvimento de soluções front-end utilizando, principalmente, as seguintes tecnologias: ReactJS, HTML5 e CSS3.
Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus alias vero sit veniam ipsam eaque optio dolorem elit voluptas.
Lorem ipsum dolor sit amet, consectetur adipisicing elit. A perferendis error voluptas alias, expedita voluptatum esse pariatur.""")

print(frase.title())
print('Letra O: {}'.format(frase.upper().count('O')))

frase = frase.replace('Python', 'HTML')
print(frase)
print('Curso' in frase)
print('Posição: {}'.format(frase.find('Curso')))

print(frase.split()) #cria uma lista
dividido = frase.split()
print(dividido[0])
print(dividido[0][0])
