def ficha(jog='<desconhecido>', gol=0):
    print(f'Ojogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
n = str(input('Nome do Jogador:'))
g = str(input('Número de gols:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

