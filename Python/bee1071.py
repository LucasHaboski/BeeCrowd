entrada, saida = map(int, input().split())

if saida < entrada:
    entrada *= 60
    saida *= 60
    saida += 1440
    print(f'O JOGO DUROU {(((saida - entrada)/60)):.0f} HORA(S)')

elif saida > entrada:
    entrada *= 60
    saida *= 60 
    print(f'O JOGO DUROU {((saida-entrada) / 60):.0f} HORA(S)')
else:
    print('O JOGO DUROU 24 HORA(S)')