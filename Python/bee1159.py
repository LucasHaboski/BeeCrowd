# O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.
# Código feio
num = 1


while num != 0:

    num = int(input())

    if num == 0:
        break

    som = 0
    cont_p = 0

    while cont_p < 5: 

        if num % 2 == 0:
            som+=num
            cont_p+=1

        num+=1

    print(som)

    