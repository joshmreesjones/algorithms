# When adding integers, the parity of the result is the same whether you
# add or subtract them.

# S = 1 + 2 + 3 + ... + n
# S = even numbers + odd numbers

# When evaluating the sum of numbers from 1 to n, adding even numbers is
# always even, so we look at the number of odd numbers in the sum (n_odd).
# If n_odd is even, then the sum is even. If n_odd is odd, then the sum is
# even. n_odd = (n + 1) // 2

n = int(input())

n_odd = (n + 1) // 2

if (n_odd % 2) == 0:
    # n_odd is even, so sum is even
    print("black")
else:
    # n_odd is odd, so sum is odd
    print("grimy")
