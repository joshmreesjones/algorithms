def power(y, n):
    """Raise y to the power of n."""
    if n == 0:
        if y == 0:
            raise Exception("0^0 is undefined.")
        return 1
    else:
        temp = power(y, n // 2) # Integer division
        if (n % 2 == 0):
            return temp * temp
        else:
            return y * temp * temp

y = 1.00000001

print(power(y, 3))
print(power(y, 31))
print(power(y, 2**31))
