import urllib.request
import emoji


try:
    site = urllib.request.urlopen('https://github.com/MatsonMatson')
except:
    print('Deu Erro!')
else:
    print('Tudo Ok!')
print(emoji.emojize(':fox:'))
