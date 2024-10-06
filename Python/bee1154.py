# Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

idade = 1
m = 0.0
cont = 0
while idade > 0:

    idade = int(input())
    if idade > 0:
        m += idade
        cont += 1

print(f'{(m/cont):.2f}') 
