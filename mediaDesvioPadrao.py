import math
print("\n---- Media e Desvio Padrao")
print("Ola. Este programa calcula a media e o desvio padrao de um")
print("conjunto de dados. Para terminar digite \"fim\"")
fim = False
n = 0
soma = 0
somaQ = 0
xString = input("\nDigite um float ")
x = float(xString)
while fim == False:
	soma = soma + x
	somaQ = somaQ + x * x
	n = n + 1
	media = soma / n
	mediaQ = somaQ / n
	var = mediaQ - media * media
	dp = math.sqrt(var)
	print("\n	Media = " ,media)
	if n - 1 != 0:
		dp = dp * n / (n-1)
		print("	Desvio Padrao = ", dp)
	else:
		print("	Desvio Padrao = 0")
	xString = input("\nDigite um float ")
	if xString == "fim" or xString == "FIM" or xString == "":
		fim = True
	else:
		x = float(xString)
print("----\n")
