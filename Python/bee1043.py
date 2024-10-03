# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
# Perimetro = XX.X
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
# Area = XX.X

valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if abs(a-b) < c < a + b and abs(a-c) < b < a + c and abs(b-c) < a < b + c :
    print('Perimetro = {:.1f}'.format(a+b+c))
else:
    print('Area = {:.1f}'.format((a+b)/2 * c))
