# Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. Calcule e imprima a média semestral. O programa só deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.
# No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que informe um código 
# (1 ou 2) indicando se ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for informado o código 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, caso contrário o programa deve ser encerrado.

resp = 1

while resp == 1:
    nota1 = float(input())

    while nota1 < 0 or nota1 > 10:
        print('nota invalida')
        nota1 = float(input())

    nota2 = float(input())

    while nota2 < 0 or nota2 > 10:
        print('nota invalida')
        nota2 = float(input())

    media = (nota1 + nota2)/2

    print(f'media = {media:.2f}')

    print('novo calculo (1-sim 2-nao)')
    resp = int(input())

    while resp < 1 or resp > 2:
        print('novo calculo (1-sim 2-nao)')
        resp = int(input())
