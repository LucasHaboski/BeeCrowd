# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

n = int(input())

for _ in range(n):
    x, y = map(int, input().split()) #ler x e y na mesma linha, separados por espaço, tíco do beecrowd

    if x > y:
        x, y = y, x

    soma = 0

    for i in range(x + 1, y):
        if i % 2 != 0:
            soma += i

    print(soma)

