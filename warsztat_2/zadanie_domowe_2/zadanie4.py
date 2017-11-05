# Zadanie 4
# Napisz funkcję factorial, która dla danego n obliczy rekurencyjnie silnię

def factorial(n):
	if n == 1 or n == 0:
		return 1
	elif n < 0:
		return None
	return n * factorial(n-1)


assert factorial(5) == 120
