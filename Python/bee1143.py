# Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

vezes = int(input())

for i in range (1,vezes+1):
    print(i, i**2, i**3)

# ================ jeito mais legal ===============================

#vezes = int(input())

#for i in range (1,vezes+1):
#    for j in range (1,4):
#        print(i**j, end=' ')
