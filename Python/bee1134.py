# Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.

x = 2
contA = 0
contG = 0
contD = 0

while x != 4:
    x = int(input())
    while x < 1 or x > 4:
        x = int(input())
    
    if x == 1:
        contA += 1
    elif x == 2:
        contG += 1
    elif x == 3:
        contD += 1

print('MUITO OBRIGADO')
print(f'Alcool: {contA}')
print(f'Gasolina: {contG}')
print(f'Diesel: {contD}')