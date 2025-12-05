#Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

#Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

val = input().split()

hora_ini = int(val[0])
min_ini = int(val[1])
hora_fim = int(val[2])
min_fim = int(val[3])

inicioMinutos = (hora_ini*60) + min_ini
fimMinutos = (hora_fim*60) + min_fim

if hora_fim <= hora_ini:
    if hora_fim == hora_ini and min_fim > min_ini:
        diferencaMinutos = fimMinutos - inicioMinutos
    else:
        diferencaMinutos = 1440 - (inicioMinutos - fimMinutos)
else:
    diferencaMinutos = fimMinutos - inicioMinutos
    
diffHorasFim = diferencaMinutos // 60
diffMinutosFim = diferencaMinutos - (diffHorasFim * 60)

if diferencaMinutos > 0 and diferencaMinutos <= 1440:
    
    if hora_ini == hora_fim and min_ini == min_fim:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    else: 
        print(f"O JOGO DUROU {diffHorasFim} HORA(S) E {diffMinutosFim} MINUTO(S)")
