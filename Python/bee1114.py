# Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". 
# Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002. 

senha = 2002
resp = 0

while resp != senha:
    resp = int(input())

    if resp != senha:
        print('Senha Invalida')
    else:
        print('Acesso Permitido')
