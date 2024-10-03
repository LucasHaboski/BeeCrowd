# Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

vezes = int(input())
x = 0
y = 0

for i in range (vezes):
    x, y = map(int, input().split())

    if y == 0:
        print('divisao impossivel')
    else:
        print(x/y) 

