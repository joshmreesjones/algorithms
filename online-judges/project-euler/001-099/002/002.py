sum = 0

a = 1
b = 2

while a <= 4000000:
	temp = a + b
	a = b
	b = temp

	if a % 2 == 0:
		sum += a

print(sum)
