num1 = int(input('Primeiro Número'))
num2 = float(input('Segundo Numero'))
a = num1 + num2
#print('A Soma entre', type(num1), num1, 'e', type(num2), num2, 'é de', type(soma), soma)
print('A Soma entre {} e {} é de {}' .format(num1, num2, a))
print('É um número?', type(a))
