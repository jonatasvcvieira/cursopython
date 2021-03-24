'''
Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
'''

num = int(input('Digite um número: '))
print('''Escolha uma das bases número inteiro:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida. Tente novamente.')




