import time

start_time = time.time()

lower_bound = 1
upper_bound = 1000

sum = 0

for i in range(lower_bound, upper_bound):
	if (i % 3 == 0 or i % 5 == 0):
		sum += i

print("The sum is " + str(sum))
print("This calculation took %s seconds." % (time.time() - start_time))
