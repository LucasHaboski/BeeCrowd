valor = float(input())
n100 = 0
n50 = 0 
n20 = 0
n10 = 0 
n5 = 0
n2 = 0

m1 = 0
m05 = 0
m025 = 0
m010 = 0
m005 = 0
m001 = 0   

while valor >= 100:
    n100+=1
    valor -= 100

while valor >= 50:
    n50+=1
    valor -= 50

while valor >= 20:
    n20+=1
    valor -= 20

while valor >= 10:
    n10+=1
    valor -= 10

while valor >= 5:
    n5+=1
    valor -= 5

while valor >= 2:
    n2+=1
    valor -= 2


while valor >= 1:
    m1+=1
    valor -= 1

while valor >= 0.5:
    m05+=1
    valor -= 0.5

while valor >= 0.25:
    m025+=1
    valor -= 0.25

while valor >= 0.10:
    m010+=1
    valor -= 0.10

while valor >= 0.05:
    m005+=1
    valor -= 0.05

while valor > 0.001:
    m001+=1
    valor -= 0.01

print("NOTAS:")
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n5} nota(s) de R$ 5.00')
print(f'{n2} nota(s) de R$ 2.00')

print("MOEDAS:")
print(f'{m1} moeda(s) de R$ 1.00')
print(f'{m05} moeda(s) de R$ 0.50')
print(f'{m025} moeda(s) de R$ 0.25')
print(f'{m010} moeda(s) de R$ 0.10')
print(f'{m005} moeda(s) de R$ 0.05')
print(f'{m001} moeda(s) de R$ 0.01')