print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cédula = 50
totalcédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totalcédula += 1
    else:
        if totalcédula > 0:
            print(f'Total de {totalcédula} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalcédula = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um excelente dia!')









