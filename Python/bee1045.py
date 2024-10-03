# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
# se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

valores = input().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

a, b, c = sorted([a,b,c], reverse=True)

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if a*a == (b*b + c*c):
        print('TRIANGULO RETANGULO')
    if a*a > (b*b + c*c):
        print('TRIANGULO OBTUSANGULO')
    if a*a < (b*b + c*c):
        print('TRIANGULO ACUTANGULO')

    if a == b == c :
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or c == a:
        print('TRIANGULO ISOSCELES')
