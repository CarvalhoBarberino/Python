def fatorial(i):
	if i == 1:
		return(1)
	elif i == 0:
		return(1)
	else:
		return(fatorial(i-1) * i)
print('\n\n****Digite um numero para calcularmos o fatorial')
i = int(input('digite: '))
print('O fatorial de {} eh:{}'.format(i, fatorial(i)))
