# Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e todos os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz, conforme for o caso. A imagem abaixo ilustra o caso da entrada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser considerados na operação.

linhaLida = int(input())
resp = str(input())

matriz = []

for i in range (12):
    linha = []
    for j in range (12):
        num = float(input())
        linha.append(num)
    matriz.append(linha)

valorLinha = matriz[linhaLida]

if resp == 'S':
    resultado = sum(valorLinha)
elif resp == 'M':
    resultado = sum(valorLinha) / 12

print(f'{resultado:.1f}')