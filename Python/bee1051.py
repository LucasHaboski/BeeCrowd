# Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo.
# Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser impresso com duas casas decimais.

salario = float(input())

if salario <= 2000.00:
    print('Isento')
else:
    imposto = 0.0
    if salario > 2000.00 and salario <= 3000.00:
        imposto += (salario - 2000.00)*0.08
    elif salario > 3000.00 and salario <= 4500.00:
        imposto += (1000 * 0.08)
        imposto += (salario - 3000.00) * 0.18
    elif salario > 4500.00:
        imposto += (1000.00 * 0.08)
        imposto += (1500.00 * 0.18)
        imposto += (salario - 4500.00) * 0.28

    print(f'R$ {imposto:.2f}')