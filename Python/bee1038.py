valores = input().split()

x = int(valores[0])

y = int(valores[1])


if x == 1:
    print(f"Total: R${4.0*y:.2f}")
    
elif x == 2:
    print(f"Total: R${4.5*y:.2f}")
    
elif x == 3:
    print(f"Total: R${5.0*y:.2f}")
    
elif x == 4:
    print(f"Total: R${2.0*y:.2f}")
    
elif x == 5:
    print(f"Total: R${1.5*y:.2f}")
