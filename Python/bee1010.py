c1, n1, p1 = input().split()
c1, n1, p1 = int(c1), int(n1), float(p1)

c2, n2, p2 = input().split()
c2, n2, p2 = int(c2), int(n2), float(p2)

pf1 = n1 * p1
pf2 = n2 * p2 

f = pf1 + pf2

print(f"VALOR A PAGAR: R$ {f:.2f}")