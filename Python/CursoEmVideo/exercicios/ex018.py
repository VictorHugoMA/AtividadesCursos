import math

angulo = float(input('Digite o ângulo: '))

sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print('Dado o ângulo {:.2f}º, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(angulo, sen, cos, tan))