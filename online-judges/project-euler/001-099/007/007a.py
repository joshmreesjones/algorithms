# find the 10,001st prime
# first prime is 2

# Wow, this description is terrible
# increment upwards
# with each new increment, start a sequence of multiples where
# the next one is computed. If the new increment is divisible by any of
# the current factors, don't add it. Skip ahead to the next number which
# isn't a "next number" in any sequence.

# store:
# counter for loop
# multiples
# positions of multiples
# primes

# loop construct
# add current counter to prime
# add current counter to multiples and positions
# go to next position (pass all predetermined positions)
# trim skipped positions
# add new/next positions
# increment counter

# for each number, mark all multiples of that number as composite
# step to the next unmarked number, repeat
# list of multiples will be multiples of primes only
# add new primes to the list of factors

# maintain a list of primes
# for each number, if it is divisible by all previous primes, it is a prime
# add that to the list of primes, continue

# NOTE: the above ramblings are descriptions of an optimization I thought of
# which is not yet implemented. Below is the brute-force method.

import math

def is_prime(n):
	if n == 1 or n == 2:
		return True
	
	if n % 2 == 0:
		return False
	
	for i in range(3, int(math.ceil(math.sqrt(n)) + 1)):
		if n % i == 0:
			return False
	
	return True

def prime_test(n):
	print("is_prime(" + str(n) + "): " + str(is_prime(n)))

def find_prime(n):
	# assume first prime is 2
	index = 1

	while n > 0:
		index += 1
		if is_prime(index):
			n -= 1
	
	return index

print(find_prime(10001))




