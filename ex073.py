import emoji

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
            'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
            'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
            'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
            'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('\033[31m-=-\033[m' * 93)
print(f'Os Primeiros 5 Times são {times[:5]}')
print('\033[31m-=-\033[m' * 93)

print('\033[34m-=-\033[m' * 93)
print(f'Os 4 Últimos Times são {times[-4:]}')
print('\033[34m-=-\033[m' * 93)

print('\033[36m-=-\033[m' * 93)
print(f'Os Times em Ordem Alfabética {sorted(times)}')
print('\033[36m-=-\033[m' * 93)

print('\033[36m-=-\033[m' * 93)
print(f'O Chapecoense está na Posição {times.index("Chapecoense")+1}')
print('\033[36m-=-\033[m' * 93)
# O +1 serve para arrumar o Index, pois tem a posição 0 que tá o Corinthians e o certo seria posição 1 e 8
print(emoji.emojize(':fox:'))