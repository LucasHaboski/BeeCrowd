#Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
#Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.


from math import sqrt #Não sei se precisa, mas para usar o sqrt


valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

delta = pow(b, 2) - 4 * a * c


if a != 0 and delta > 0:
    
    x1 =  (-b + sqrt(delta)) / (2 * a)
    x2 =  (-b - sqrt(delta)) / (2 * a)
    
    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")
else: 
    print("Impossivel calcular")