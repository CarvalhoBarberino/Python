print("\n---- Baskara")
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if b**2 - 4*a*c>=0:
	deltaSq = math.sqrt(b**2 - 4*a*c)
	x1 = (-b + deltaSq)/2
	x2 = (-b - deltaSq)/2
	if deltaSq == 0:
		print("solucao unica ->", x1)
	else:
		print("solucao 1 ->", x1)
		print("solucao 2 ->", x2)
else:
	print("A solução não pertence ao conjunto dos numeros reais")
print("----\n")
