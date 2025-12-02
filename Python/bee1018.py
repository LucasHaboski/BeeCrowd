prec = int(input())


print(f"{prec}")

c100 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0

while prec >= 100:
    c100 += 1
    prec -= 100

while prec >= 50:
    c50 += 1
    prec -= 50

while prec >= 20:
    c20 += 1
    prec -= 20
    
while prec >= 10:
    c10 += 1
    prec -= 10

while prec >= 5:
    c5 += 1
    prec -= 5

while prec >= 2:
    c2 += 1
    prec -= 2
    
while prec >= 1:
    c1 += 1
    prec -= 1
        

print(f"{c100} nota(s) de R$ 100,00")

print(f"{c50} nota(s) de R$ 50,00")

print(f"{c20} nota(s) de R$ 20,00")

print(f"{c10} nota(s) de R$ 10,00")

print(f"{c5} nota(s) de R$ 5,00")

print(f"{c2} nota(s) de R$ 2,00")

print(f"{c1} nota(s) de R$ 1,00")