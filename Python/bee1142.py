# Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

contPum = 1
qnt = int(input())

for i in range(qnt):
    for j in range (3):
        print(f'{contPum}', end=' ')
        contPum += 1
    print('PUM')
    contPum += 1