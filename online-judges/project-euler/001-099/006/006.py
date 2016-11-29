n = 100

# Summation formula (squared)
sum1 = ((n ** 2 + n) / 2) ** 2

# TODO derive a summation formula for n**2 for n=1 to n=n
sum2 = 0
for i in range(1, n + 1):
	sum2 += i ** 2

print(sum1 - sum2)
