def print_binary(x, digits):
    fmt_string = "{0:0" + str(digits) + "b}"
    print(fmt_string.format(x))

def power_binary(x, t):
    """Visualize the computation of a power in binary.

    Compute x^t by starting with 1 and multipling x into
    it t times. For each iteration, print the binary
    representation of the number. It's cool to see the
    1's propagate outwards.

    Keyword arguments:
         x -- the base in x^t
         t -- the power in x^t
    """

    digits = len(bin(x ** t))

    result = 1
    while t > 0:
        result *= x
        t -= 1

        print_binary(result, digits)



def print_many(n, t):
    for i in range(1, n + 1):
        print("=" * 80)
        print("Computing %d^%d" % (i, t))
        power_binary(i, t)

def print_big_example():
    power_binary(6, 45)



#print_many(10, 45)
#print_big_example()
power_binary(12 ** .5, 45)
