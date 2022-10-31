largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {} x {} e sua área total é de {}m/2' .format(largura, altura, area))
tinta = area / 2
print('Para pintar sua parede, você precisara de {}l de tinta' .format(tinta))
