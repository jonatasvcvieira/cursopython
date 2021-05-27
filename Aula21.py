# Interactive Help
# Aocstrings
# Argumentos opcionais
# Escopo de variáveis
# Retorno de resultados

# ########## Interactive Help

# help()
# help(print)  acessa as informações da função, manual do comando.

# ######### Docstrings

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na telo.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c =+ p
    print('Fim!')


help(contador)
'''

# ########     Parâmetros opcionais

'''
def somar(a=0, b=0 , c=0):
    """
    -> Faz a soma de três valores e mostra na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(1, 2, 3)
somar(1, 2)
somar(1)
somar()

'''

# ####### Escopo de variáveis

'''
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
    

# Programa principal
n = 2
print(f'No prigrama principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')
'''

'''
def função():
    n1 = 4
    print(f'N1 dentro(variável local) vale {n1}')

n1 = 2
função()
print(f'N1 fora(variável global) vale {n1}')
'''

'''
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')
'''

# ###### Retorno de resultados.

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2}, {r3}')

