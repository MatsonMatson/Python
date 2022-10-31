import emoji

while True:
    n = int(input('Quer ver a Tabuada de qual \033[31mNúmero\033[m?: '))
    if n < 0:
        break
    print('-' * 20)
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}' )
    print('-' * 20)
print('PROGRAMA ENCERRADO, VOLTE SEMPRE!!')