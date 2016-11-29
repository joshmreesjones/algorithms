# Efficient

import time

start = time.time()

# generate all prime numbers less than or equal to n
n = 1000000

# list of generated primes
primes = []

# no empty set literal; must use set()
marked = set()

index = 2

while index <= n:
	primes.append(index)

	# add all multiples of index from index to n to marked
	counter = index
	while counter <= n:
		marked.add(counter)
		counter += index
	
	while index in marked:
		marked.remove(index)
		index += 1

print("Computation took " + str(time.time() - start) + " seconds.")
print(len(primes))
