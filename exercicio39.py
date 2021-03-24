'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

sexo = int(input("""Informe o seu sexo: 
[ 1 ] Masculino
[ 2 ] Feminino
Opção: """))
from datetime import date
if sexo == 1:
    anoatual = date.today().year
    nasc = int(input('Digite o ano de nascimento: '))
    idade = anoatual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, anoatual))
    if idade == 18:
        print('Você tem que se alistar Imadiatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento'.format(saldo))
        ano = anoatual + saldo
        print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você ja deveria ter se alistado ha {} anos.'.format(saldo))
        ano = anoatual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
elif sexo == 2:
    print("Você não precisa se alistar.")

