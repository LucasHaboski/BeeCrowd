# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

n1 = 11
n2 = 11

while n1 < 0 or n1 > 10:
    n1 = float(input())

    if n1 < 0 or n1 > 10:
        print('nota invalida')

while n2 < 0 or n2 > 10:
    n2 = float(input())

    if  n2 < 0 or   n2 > 10:
        print('nota invalida')

print('media = {:.2f}'.format((n1+n2)/2))
