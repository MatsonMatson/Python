import emoji
from math import cos, tan, sin, radians

angulo = float(input('Digite o Ângulo que você deseja: '))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print('O Ângulo de {} tem o Cosseno de {:.2f}' .format(angulo, cosseno))
print('O Ângulo de {} tem o Seno de {:.2f}' .format(angulo, seno))
print('O Ângulo de {} tem a Tangente de {:.2f}' .format(angulo, tangente))

print(emoji.emojize(":fox:"))
