# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.
x = 1
y = 0
while x != y:
    x, y = map(int, input().split())

    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')