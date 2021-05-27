'''
def lin():
    print('-' * 30)


#Progrma principal
lin()
print('   Cruso em Vídeo   ')
lin()
print('   Aprenda Python   ')
lin()
print('   Jonatas Vasconcelos   ')
lin()
'''

'''
def título(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)
    
    
#Programa Principal
título('   Curso em Vídeo   ')
título('   Python é muito bom'   )
título('   Oi   ')
'''
'''
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
'''

'''
def soma(a, b):
    s = a + b
    print(s)


#Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
'''

'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


#Programa principal
soma(4, 5)
'''

'''
def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('Fim')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

'''
def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''

'''
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
        

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)

