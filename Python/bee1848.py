# Como se sabe, existe um corvo com três olhos. O que não se sabia é que o corvo com três olhos pode prever o resultado da loteria de Westeros. Enquanto todos os outros corvos coletam as apostas, o corvo de três olhos já sabe o resultado, e quando Bran sonha com o corvo, o corvo conta o resultado. O problema é que Bran apesar de lembrar do sonho, não consegue interpretá-lo sozinho em tempo hábil. A sua tarefa é fazer um programa para interpretar o sonho de Bran e calcular o resultado da loteria.
# Durante o sonho, o corvo pisca diversas vezes e grita apenas 3 vezes. A cada grito um número do resultado da loteria é calculado.
# Cada piscada do corvo comunica um número em binário. Um olho aberto significa 1 e um olho fechado significa 0. O olho da esquerda é o mais significativo e o da direita é o menos significativo. A cada piscada, este número deve ser somado, e quando o corvo grita, essa soma é um resultado.

for i in range (3):

    numeroLoteria = 0
    corvo = 'comeco'

    while corvo != 'caw caw':
        corvo = str(input())

        if corvo == '--*':
            numeroLoteria+=1
        elif corvo == '-*-':
            numeroLoteria+=2
        elif corvo == '-**':
            numeroLoteria+=3
        elif corvo == '*--':
            numeroLoteria+=4
        elif corvo == '*-*':
            numeroLoteria+=5
        elif corvo == '**-':
            numeroLoteria+=6
        elif corvo == '***':
            numeroLoteria+=7
    
    print(numeroLoteria)