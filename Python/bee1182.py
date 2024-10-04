colLida = int(input())
resp = str(input())

matriz = []

for i in range (12):
    linha = []
    for j in range (12):
        num = float(input())
        linha.append(num)
    matriz.append(linha)

valorColuna = [matriz[i][colLida] for i in range (12)]

if resp == 'S':
    resultado = sum(valorColuna)
elif resp == 'M':
    resultado = sum(valorColuna) / 12

print(f'{resultado:.1f}')