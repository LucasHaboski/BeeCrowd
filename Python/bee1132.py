# Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

x = int(input())
y = int(input())
soma = 0

if x > y:
    x, y = y, x

for i in range (x, y+1):
    if i % 13 != 0:
        soma += i

print(soma)