import math

x, y = map(float, input().split())
x2, y2 = map(float, input().split())


res = math.sqrt(pow(x2-x, 2) + pow(y2-y, 2))

print(f"{res:.4f}")