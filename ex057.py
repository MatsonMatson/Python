import emoji

sexo = str(input('Informe seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos, por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo \033[31m{}\033[m Registrado com sucesso!!' .format(sexo))
print(emoji.emojize(':fox:'))
