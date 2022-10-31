import emoji

expr = str(input('Digite sua Expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua Expressão está válida!')
else:
    print('Sua Expressão não é válida!')
print(emoji.emojize(':fox:'))
