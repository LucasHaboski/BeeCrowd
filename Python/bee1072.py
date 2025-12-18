x = int(input())

den= 0
fora = 0

for i in range(x):
    y = int(input())
    
    if y >= 10 and y <= 20:
        den += 1
    else:
        fora += 1
        
print(f"{den} in")
print(f"{fora} out")