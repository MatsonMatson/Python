import emoji

palavras = (str(input('Digite sua Palavra: ')), str(input('Digite outra Palavra: ')),
            str(input('Digite mais uma Palavra: ')), str(input('Digite sua última Palavra: ')))
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')