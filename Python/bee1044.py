val = input().split()

x = int(val[0])
y = int(val[1])

divi = x/y
divi2 = y/x


if divi % 1 == 0:
    print("Sao Multiplos")
elif divi2 % 1 == 0:
    print("Sao Multiplos") 
else:
    print("Nao sao Multiplos")
 