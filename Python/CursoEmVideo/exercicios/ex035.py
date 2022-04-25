reta1 = int (input('Reta 1: '))
reta2 = int (input('Reta 2: '))
reta3 = int (input('Reta 3: '))

if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')