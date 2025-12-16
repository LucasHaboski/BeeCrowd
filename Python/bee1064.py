posi = 0
media = 0.0
for i in range (6):
    val = float(input())
    
    if val > 0.0:
        posi+=1
        media+=val
        
print(f"{posi} valores positivos")
print(f"{media/posi:.1f}")