import emoji

nome = str(input('Digite seu Nome: ')).strip()
separa = nome.split()

print('Analisando seu Nome...')
print('Seu nome em maíusculas é {}' .format(nome.upper()))
print('Seu nome em minúsculas é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count('  ')))
#print('Seu Primeiro nome tem {} letras' .format(nome.find(' '))) o debaixo é mais simples de compreender
print('Seu Primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))

print('\n')

print(emoji.emojize(':fox:'))
