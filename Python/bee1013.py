x, y, z = map(int, input().split())


maiorxy = int((x+y+abs(x-y))/2)
maioryz = int((y+z+abs(y-z))/2)

if(maiorxy > maioryz):
    print(f"{maiorxy} eh o maior")
else:
    print(f"{maioryz} eh o maior")