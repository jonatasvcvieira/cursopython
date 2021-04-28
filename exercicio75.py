print('-=' * 20)
print('Digite 4 números.')
print('-=' * 20)
num = (int(input('Digite primeiro número:')),
      int(input('Digite segundo número:')),
      int(input('Digite terceiro número:')),
      int(input('Digite quarto número:')))
print(f'Você digitou os valores {num}')
print(f'O valor nove apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhume posição.')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
