a, b, c = map(float, input().split())

A = a * c / 2
B = 3.14159 * pow(c, 2)
C = (a + b) * c / 2
D = b * b
E = a * b

print(f"TRIANGULO: {A:.3f}")
print(f"CIRCULO: {B:.3f}")
print(f"TRAPEZIO: {C:.3f}")
print(f"QUADRADO: {D:.3f}")
print(f"RETANGULO: {E:.3f}")