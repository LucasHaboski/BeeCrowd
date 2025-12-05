val = float(input())


if val > 0 and val <= 400.0:
    final = val + (val*0.15)
    
    print(f"Novo salario: {final:.2f}")
    print(f"Reajuste ganho: {(val*0.15):.2f}")
    print("Em percentual: 15 %")
    
elif val > 400.0 and val <= 800.0:
    final = val + (val*0.12)
    
    print(f"Novo salario: {final:.2f}")
    print(f"Reajuste ganho: {(val*0.12):.2f}")
    print("Em percentual: 12 %")
    
elif val > 800.0 and val <= 1200.0:
    final = val + (val*0.10)
    
    print(f"Novo salario: {final:.2f}")
    print(f"Reajuste ganho: {(val*0.10):.2f}")
    print("Em percentual: 10 %")
    
elif val > 1200.0 and val <= 2000.0:
    final = val + (val*0.07)
    
    print(f"Novo salario: {final:.2f}")
    print(f"Reajuste ganho: {(val*0.07):.2f}")
    print("Em percentual: 7 %")
    
elif val > 2000.0:
    final = val + (val*0.04)
    
    print(f"Novo salario: {final:.2f}")
    print(f"Reajuste ganho: {(val*0.04):.2f}")
    print("Em percentual: 4 %")