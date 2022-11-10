from Uteis.Arquivo import *
from time import sleep

arq = 'pessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Cadastrar nova Pessoa', 'Ver Pessoas cadastradas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastra uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        cabecalho('Saindo do Sistema... Até Logo!')
        break
    else:
        # Digitou uma opção errado no menu.
        print('\033[31mERRO! Por Favor, digite uma opção válida.\033[31m')
    sleep(1)
