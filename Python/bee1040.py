notas = input().split()

n1 = float(notas[0]) * 2.0
n2 = float(notas[1]) * 3.0
n3 = float(notas[2]) * 4.0
n4 = float(notas[3]) * 1.0

media = (n1 + n2 + n3 + n4) / 10.0

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
    
elif media < 5.0:
    print("Aluno reprovado.")
    
elif media >= 5.0 and media < 7.0:
    print("Aluno em exame.")
    
    exame = float(input())
    
    print(f"Nota do exame: {exame:.1f}")
    
    mediaFinal = (media + exame) / 2.0
    
    if mediaFinal >= 5.0:
        print("Aluno aprovado.")
        
    elif mediaFinal < 5.0:
        print("Aluno reprovado.")
        
    print(f"Media final: {mediaFinal:.1f}")