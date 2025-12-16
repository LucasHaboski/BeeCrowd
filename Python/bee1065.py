par = 0
for i in range (5):
    val = int(input())
    
    if val % 2 == 0:
        par+=1
        
print(f"{par} valores pares")