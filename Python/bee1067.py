num = int(input())
numLimite = int(input())

if num > numLimite:
    num, numLimite = numLimite, num

soma = 0

for i in range (num + 1, numLimite):
    if i % 2 != 0:
        soma = soma + i
    
print(soma)
