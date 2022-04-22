import math

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

#hip = (ca ** 2 + co ** 2) ** (1/2) ou com math.hypot(ca, co)
hip = math.hypot(co, ca)

print('No triângulo retângulo de cateto oposto {} e adjacente {} temos a hipotenusa igual a {:.2f}'.format(co, ca, hip))	