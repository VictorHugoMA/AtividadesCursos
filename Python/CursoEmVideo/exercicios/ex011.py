larguraParede = float(input('Largura da parede: '))
alturaParede = float(input('Altura da parede: '))

areaParede = alturaParede * larguraParede

print('Em uma parede de {}m² será necessário {:.2f} litros de tinta para pintar'.format(areaParede, areaParede/2))