# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
# Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento. 

vezes = int(input())
qntC = 0
qntR = 0
qntS = 0
totAnimais = 0

for i in range (vezes):
    
    respostas = input().split()
    qnt = int(respostas[0])
    resp = str(respostas[1])

    if resp == 'C':
        qntC += qnt
    elif resp == 'R':
        qntR += qnt
    else:
        qntS += qnt

    totAnimais += qnt

print(f'Total: {totAnimais} cobaias')
print(f'Total de coelhos: {qntC}')
print(f'Total de ratos: {qntR}')
print(f'Total de sapos: {qntS}')
print('Percentual de coelhos: {:.2f} %'.format((qntC/totAnimais)*100))
print('Percentual de ratos: {:.2f} %'.format((qntR/totAnimais)*100))
print('Percentual de sapos: {:.2f} %'.format((qntS/totAnimais)*100))
