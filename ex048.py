import emoji

soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
       cont += 1
       soma += c # += é ele recebe ele + ...
print('A Soma de todos os {} valores solicitados é de {}' .format(cont, soma))
print(emoji.emojize(':fox:'))
