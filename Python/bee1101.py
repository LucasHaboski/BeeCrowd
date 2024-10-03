# Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

while True:

    soma = 0 

    x, y = map(int, input().split())

    if x <= 0 or y <= 0:
        break
    elif x < y:
        for i in range (x, y+1):
            print (i, end=' ')
            soma = soma + i
    else:
        for i in range (y, x+1):
            print (i, end=' ')
            soma = soma + i

    print(f'Sum={soma}')

    