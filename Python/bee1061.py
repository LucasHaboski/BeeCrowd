# Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.
# Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

entrada = input().split()
diaEntrada = str(entrada[0])
numEntrada = int(entrada[1])

horaEntrada = input().split()
horaE = int(horaEntrada[0])
trava1E = str(horaEntrada[1])
minutosE = int(horaEntrada[2])
trava2E = str(horaEntrada[3])
segundosE = int(horaEntrada[4])

saida = input().split()
diaSaida = str(saida[0])
numSaida = int(saida[1])

horaSaida = input().split()
horaS = int(horaSaida[0])
trava1S = str(horaSaida[1])
minutosS = int(horaSaida[2])
trava2S = str(horaSaida[3])
segundosS = int(horaSaida[4])

contSegundosEntrada = (numEntrada*86400) + (horaE*3600) + (minutosE*60) + segundosE 
contSegundosSaida = (numSaida*86400) + (horaS*3600) + (minutosS*60) + segundosS

diferencaSegundos = contSegundosSaida - contSegundosEntrada

diasEvento = diferencaSegundos // 86400
diferencaSegundos %= 86400

horasEvento = diferencaSegundos // 3600
diferencaSegundos %= 3600

minutosEvento = diferencaSegundos // 60

segundosEvento = diferencaSegundos % 60

print(f'{diasEvento} dia(s)')
print(f'{horasEvento} hora(s)')
print(f'{minutosEvento} minuto(s)')
print(f'{segundosEvento} segundo(s)')


