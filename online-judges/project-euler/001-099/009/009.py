# Project Euler Problem 9
# Josh Rees-Jones
# https://projecteuler.net/problem=9

def transform1(a, b, c):
	return [
		1*a - 2*b + 2*c,
		2*a - 1*b + 2*c,
		2*a - 2*b + 3*c
	]

def transform2(a, b, c):
	return [
		1*a + 2*b + 2*c,
		2*a + 1*b + 2*c,
		2*a + 2*b + 3*c
	]

def transform3(a, b, c):
	return [
		-1*a + 2*b + 2*c,
		-2*a + 1*b + 2*c,
		-2*a + 2*b + 3*c
	]

def check_triple(a, b, c):
	return a + b + c == 1000
	#return (a**2 + b**2 == c**2) and (a + b + c == 1000)



first_triple = [3, 4, 5]

triples = []

def generate_triples(a, b, c):
	if (a >= 1000): return [a, b, c]

	t1 = transform1(a, b, c)
	t2 = transform2(a, b, c)
	t3 = transform3(a, b, c)

	triples.append([a, b, c])
	generate_triples(t1[0], t1[1], t1[2])
	generate_triples(t2[0], t2[1], t2[2])
	generate_triples(t3[0], t3[1], t3[2])
	
	return


generate_triples(3, 4, 5)

for triple in triples:
	a = triple[0]
	b = triple[1]
	c = triple[2]

	if check_triple(a, b, c):
		print(triple)

