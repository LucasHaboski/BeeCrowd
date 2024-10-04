# Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa, seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

qnt = int(input())
mult = 0

for i in range (qnt):
    i1 = (i+1) ** 1
    i2 = (i+1) ** 2
    i3 = (i+1) ** 3

    print(f'{i1} {i2} {i3}')
    print(f'{i1} {i2+1} {i3+1}')