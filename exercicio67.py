while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    print('-' * 30)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont} = {n*cont}')
    print('-'*30)
print('Programa tabuada encerrado.')
