n = 4

while n < 5 or n > 2000:
    n = int(input())
    

for i in range (n+1):
    if i % 2 == 0 and i != 0:
        res= pow(i,2)
        print(f"{i}^2 = {res}")