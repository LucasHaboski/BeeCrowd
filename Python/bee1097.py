min = 5
max = 7
for i in range (1, 10, 2):
    for j in range (max, min-1, -1):
        print(f'I={i} J={j}')
    min += 2
    max += 2