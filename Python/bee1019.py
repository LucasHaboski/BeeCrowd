temp = int(input())

min = 0
hr = 0

while temp >= 60:
    min+=1
    temp -= 60

while min >= 60:
    hr += 1
    min -= 60
    
print(f"{hr}:{min}:{temp}")