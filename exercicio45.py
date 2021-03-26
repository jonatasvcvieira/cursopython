'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('{:=^22}'.format(' Jokenpô '))
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada? '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('pô!!!')
sleep(1)
if computador == 0: #computador jogou Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Jogador vence')
    else:
        print('Jogada inválida!')

elif computador == 1: # computador jogou Papel
    if jogador == 0:
        print('Computador Vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada inválida!')

elif computador == 2: # computador jogou Tesoura
    if jogador == 0:
        print('Jogador Vence')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida!')




