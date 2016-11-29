import time

start = time.time()

def is_prime(n):
	index = 2
	while index ** 2 <= n:
		if n % index == 0:
			return False
		index += 1
	return True

# generate all primes up to n
n = 100000
primes = []
index = 2

while index <= n:
	if is_prime(index):
		primes.append(index)

	index += 1

print("Computation took " + str(time.time() - start) + " seconds.")
print(len(primes))
