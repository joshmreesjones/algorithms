def is_palindrome(num):
	number = str(num)
	length = len(number)

	index = 0
	while index < length:
		# index of 0 corresponds to opposite index of -1
		if number[index] != number[-(index + 1)]:
			return False
		index += 1
	return True



palindromes = []

digits = 3

# largest number with the specified number of digits
num1 = (10 ** digits) - 1

# only compute products of 3-digit numbers
while num1 >= (10 ** (digits - 1)):
	# largest number with the specified number of digits
	num2 = (10 ** digits) - 1

	while num2 >= num1:
		product = num1 * num2

		if is_palindrome(product):
			palindromes.append(product)

		num2 -= 1
	num1 -= 1

print(max(palindromes))

# Let n = number of digits of each factor (equal)
# Q. It seems that for n > 2, this method does not produce
#    palindromes with strictly decreasing magnitude. Is there
#    any way to prove this using some sort of computational
#    notation/system (is this lambda calculus?)?
