km = float(input('Digite quantos quilometros rodados:'))
d = int(input('Digite quantos dias alugados:'))
custototal = (km * 0.15) + (d * 60)
print('Foram rodados {}km, com {} diarias, sendo um custo total do aluguel R${}'.format(km, d, custototal ))
