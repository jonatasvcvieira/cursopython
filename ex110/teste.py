from ex110 import moeda

p = float(input('Digite o preço: R$ '))
#moeda.resumo(p)
moeda.resumo(p, 20, 12)

'''
print(f'A metade de R${moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de R${moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 10%, temos {moeda.diminuir(p, 10, True)}')
'''
