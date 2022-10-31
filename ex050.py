import emoji

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: ' .format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num  # += é ele recebe ele + ...
print('Você informou {} números e a soma deles é de {}' .format(cont, soma))
print(emoji.emojize(':fox:'))
