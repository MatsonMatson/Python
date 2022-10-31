import emoji

n = 0
s = 0
tot = 0

while True:
    n = int(input("Digite um Número [999 to Stop]: "))
    if n == 999:
        break
    s += n
    tot += 1

print(f'Todos os {tot} somados dão o valor de {s}')
print(emoji.emojize(':fox:'))
