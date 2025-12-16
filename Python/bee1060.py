posi = 0
for i in range (6):
    val = float(input())
    
    if val > 0.0:
        posi+=1
        
print(f"{posi} valores positivos")