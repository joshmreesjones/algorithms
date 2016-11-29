# Euler's method implementation
# Made by Josh Rees-Jones

def euler(diff_eqn, x_init, y_init, step, n, output_points=False):
	"""Perform Euler's method with the specified differential
	equation, initial condition, and number of iterations.

	Keyword arguments:
	diff_eqn -- differential equation with signature diff_eqn(x, y)
	x_init   -- initial x
	y_init   -- initial y
	step     -- step size
	n        -- number of iterations to perform
	output_points -- output a list of points rather than the final value (boolean value)

	Returns:
	if output_points == False (default):
		outputs the final approximation
	if output_points == True:
		outputs a list of points generated by Euler's method
	"""

	output = []

	x = x_init
	y = y_init

	# perform n iterations
	while n > 0:
		y += diff_eqn(x, y) * step
		# x is calculated after y because y depends on the previous x
		x += step

		output.append((x, y))

		n -= 1
	
	return output if output_points else output[-1][1]





def diff_eqn1(x, y):
	return 1 - (x * y)

def diff_eqn2(x, y):
	return x - (x * y)





# webassign 7.2 #4
print(euler(diff_eqn1, 0, 0, .2, 1/.2))

# webassign 7.2 #5a
print(euler(diff_eqn2, 1, 0, .2, 2))

# webassign 7.2 #5b
print(euler(diff_eqn2, 1, 0, .1, 4))