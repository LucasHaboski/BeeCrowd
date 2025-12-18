x =  1000000

while x > 10000:
    x = int(input())
    
for i in range(x):
    y = int(input())
    
    if y % 2 == 0 and y > 0:
        print("EVEN POSITIVE")
    elif y % 2 == 0 and y < 0:
        print("EVEN NEGATIVE")
    elif y % 2 != 0 and y > 0:
        print("ODD POSITIVE")
    elif y % 2 != 0 and y < 0:
        print("ODD NEGATIVE")
    else:
        print("NULL")