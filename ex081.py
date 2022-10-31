import emoji

valores = []
while True:
    valores.append(int(input('Digite um Número: ')))
    resp = str(input('Você Deseja Continuar?: [S/N]'))
    if resp == 'Nn':
        break
print('-=-' * 30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente é {valores}')
if 5 in valores:
    print('O Valor 5 está na Lista!')
else:
    print('O Valor 5 não está na Lista')