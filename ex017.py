import emoji
from math import hypot

oposto = float(input('Comprimento do Cateto Oposto: '))
adjacente = float(input('Comprimento do Cateto Adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('A Hipotenusa vai medir {:.2f}' .format(hipotenusa))
print(emoji.emojize(":fox:"))
