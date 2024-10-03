# Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

x = int(input())
y = int(input())

if x > y:
    x, y = y, x

for i in range (x+1, y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)