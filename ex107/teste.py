'''
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10)}')
'''

from moeda import aumentar, diminuir, dobro, metade

p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p:.2f} é R${metade(p):.2f}')
print(f'O dobro de R${p:.2f} é R${dobro(p):.2f}')
print(f'Aumentando 10%, temos R${aumentar(p, 10):.2f}')
print(f'Diminuir 10%, temos R${diminuir(p, 10):.2f}')

