'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

'''
distância = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua viagem será de R${:.2f}'.format(preço))
'''
distância = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua viagem será de R${:.2f}'.format(preço))
