'''
Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”,
que é uma estrutura versátil e simples de entender. Por exemplo:

for c in range(0, 4):

print(c)

print(‘Acabou’)
'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))

