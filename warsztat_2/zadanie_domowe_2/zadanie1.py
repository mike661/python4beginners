# Zadanie 1
# Napisz funkcję power, która dla danego n i p zwraca w wyniku n podniesione do potęgi p.
# Domyślna wartość argumentu p to 2.
# Niech n i p będą liczbami całkowitymi >= 0.

def power(n, p=2):
	return n ** p
	

assert power(5) == 25
assert power(5, 3) == 125