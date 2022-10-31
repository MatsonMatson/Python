import emoji

num = cont = soma = 0
num = int(input('Digite um Número [999 para parar]: '))
while num != 999:
    soma += num
    cont +=1
    num = int(input('Digite um Número [999 para parar]: '))
print('Você digitou {} Números e a soma deles é de {} ' .format(cont, soma))
print(emoji.emojize(':fox:'))