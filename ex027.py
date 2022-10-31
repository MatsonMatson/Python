import emoji

n = str(input('Digite seu Nome Completo: ')).strip()
nome = n.split()

print('Muito Prazer em te conhecer!!')
print('Seu primeiro nome é {}' .format(nome[0]))
print('Seu ultimo nome é {}' .format(nome[len(nome)-1]))

print(emoji.emojize(':fox:'))
