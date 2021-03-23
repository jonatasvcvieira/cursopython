'''
Nessa aula, vamos aprender como criar estruturas condicionais aninhadas,
usando os comandos if.. elif.. else em programas Python.
'''

nome = str(input('Quel é o seu nome? '))
if nome == 'Jonatas':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}'.format((nome)))
