'''
# num = (2, 5, 9, 1) exe tuplas
# num[2] = 3
num = [2, 5, 9, 1]
num[2] = 3
# num[4] = 7 forma errada de adicionar
num.append(7) #forma correta de adicionar no final
num.sort() # colocar a lista em ordem crescente
# num.sort(reverse=True) coloca a lista em ordem reversa
num.insert(2 , 0) # inserir 0 na posição 2 da lista
num.pop() # elimina o último posição da lista
num.pop(2)  # elimina a posição 2 da lista
num.insert(2, 2)
num.remove(2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Esta lista tem {len(num)} elementos.')
'''

#valores = []
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

# for v in valores:
#    print(f'{v}...', end='')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
