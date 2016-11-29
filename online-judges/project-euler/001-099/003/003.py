number = 600851475143
factors = []

def find_factor(number):
	factor_candidate = 2
	
	while factor_candidate < (number / 2):
		if number % factor_candidate == 0:
			return factor_candidate

		factor_candidate += 1

	return None

def find_prime_factors(number):
	factor = find_factor(number)

	if factor == None:
		return [number]
	else:
		return [factor] + find_prime_factors(number / factor)

print(find_prime_factors(number))
