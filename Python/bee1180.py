# Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N]. A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor e a sua posição dentro do vetor, mostrando esta informação.

n = int(input())
numeros= list(map(int, input().split()))

menorValor = min(numeros)
posicaoMenor = numeros.index(menorValor)

print(f'Menor valor: {menorValor}')
print(f'Posicao: {posicaoMenor}')