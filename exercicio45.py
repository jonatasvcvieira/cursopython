'''
 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
'''

print(' {:=^40}'.format(' Lojas Vasconcelos '))
preço = float(input('Preço das compras: R$'))
print('''' FOrmas de Pagamento
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão de crédito
[ 3 ] 2x no cartão de crédito
[ 4 ] 3x ou mais no cartão de crédito
''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - ( preço * 10 / 100)
elif opção == 2:
    total = preço - ( preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(preço, total))
elif opção == 4:
    total = preço + (preço * 20 /100)
    totalparc = int(input('Quantas parcelas: '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totalparc, parcela))
else:
    total = 0
    print('Opção inválida de pagamento. Tenete novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))



