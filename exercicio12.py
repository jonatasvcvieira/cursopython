prod = float(input('Digite o valor do produto:'))
promo = prod - (prod * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(prod, promo))