# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

vezes = int(input())

for i in range (vezes):

    notas = input().split()
    n1 = float(notas[0])*2
    n2 = float(notas[1])*3
    n3 = float(notas[2])*5

    print('{:.1f}'.format((n1+n2+n3)/10))

