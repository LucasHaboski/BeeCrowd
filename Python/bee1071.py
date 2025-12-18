entrada = int(input())
saida = int(input())


num = 0
soma = 0
i=0

if saida < entrada:
    temp = entrada
    entrada = saida
    saida = temp

while entrada < saida:
    if entrada % 2 != 0 and i != 0:
        soma+=entrada
    entrada+=1
    i+=1
    
print(soma)