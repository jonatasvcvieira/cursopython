'''
Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI
para configurar cores para os seus programas em Python.
Veja como utilizar o código \033[m com todas as suas principais possibilidades.
'''
'''
print('\033[1;31mOlá Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

'''
'''
nome = 'Jonatas'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
'''
#Cores pré-definidas
nome = 'Jonatas'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá, Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))



