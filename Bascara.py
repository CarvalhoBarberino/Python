print("\n---- Baskara")
import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if b**2 - 4*a*c>=0:
	deltaSq = math.sqrt(b**2 - 4*a*c)
	x1 = (-b + deltaSq)/2/a
	x2 = (-b - deltaSq)/2/a
	if deltaSq == 0:
		print("solucao unica ->", x1)
	else:
		print("solucao 1 ->", x1)
		print("solucao 2 ->", x2)
else:
	deltaSqImg = math.sqrt(4*a*c - b**2)	
	print("solucao 1 ->", -b/2/a, " + i *", deltaSqImg/2/a)
	print("solucao 2 ->", -b/2/a, " - i *", deltaSqImg/2/a)
print("----\n")
