# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

n = int(input())
fib = 0
nat = 1
aux = 0

for i in range (n-1):
    print(f'{fib}', end=' ')

    aux = nat
    nat += fib
    fib = aux
print(f'{fib}')