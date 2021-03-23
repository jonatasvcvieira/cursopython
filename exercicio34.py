'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salário = float(input('Qual é o salário do funcionário? '))
if salário <= 125:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('O funcionário que ganhava R${:.2f} passará a ganhar R${:.2f}'.format(salário, novo))
