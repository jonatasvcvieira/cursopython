'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''

nome = str(input('Qual é o seu nome completo? '))
print('Verificando se seu nome tem Silva....')
print('{}'.format('silva' in nome.lower()))
#print('Seu nome te Silva? {}'.format('SILVA' in nome.upper()))
