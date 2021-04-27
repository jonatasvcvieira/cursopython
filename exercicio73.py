times = ('América', 'Athletico-MG', 'Atlético-GO', 'Atletico-MG',
         'Bahia', 'Bragantino', 'Ceará', 'Corinthians', 'Cuiabá',
         'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional',
         'Juventude', 'Palmeiras', 'Santos', 'São Paulo', 'Sport')
print('-=' * 15)
print(f'Lista de times de Brasileirão: {times}')
print('-=' * 15)
print(f'Os cinco primeiros são {times[:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Fluminense está na {times.index("Fluminense")+1}ª posição.')
print('-=' * 15)