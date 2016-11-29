# 1-1 Comparison of running times
# For each function f(n) and time t in the following table, determine the largest size n of a problem that can be solved in time t, assuming that the algorithm to solve the problem takes f(n) microseconds.
# 
# 1 second = 1,000,000 microseconds
# For each cell, solve f(n) <= time for n.
# 
#           +----------+----------+--------+-------+---------+--------+-----------+
#           | 1 second | 1 minute | 1 hour | 1 day | 1 month | 1 year | 1 century |
# +---------+----------+----------+--------+-------+---------+--------+-----------+
# | lg(n)   | 2^(10^6) |          |        |       |         |        |           |
# | sqrt(n) | (10^6)^2 |          |        |       |         |        |           |
# | n       | 10^6     |          |        |       |         |        |           |
# | n lg(n) | 62746    |          |        |       |         |        |           |
# | n^2     | 1000     |          |        |       |         |        |           |
# | n^3     | 100      |          |        |       |         |        |           |
# | 2^n     | 19       |          |        |       |         |        |           |
# | n!      | 9        |          |        |       |         |        |           |
# +---------+----------+----------+--------+-------+---------+--------+-----------+

# I could continue this, but it would be a waste of time. See below for a script that generates these values.

import math

# times in microseconds
SECOND  = 1000000
MINUTE  = SECOND * 60
HOUR    = MINUTE * 60
DAY     =   HOUR * 24
MONTH   =    DAY * 30
YEAR    =    DAY * 365
CENTURY =   YEAR * 1000

times = [SECOND, MINUTE, HOUR, DAY, MONTH, YEAR, CENTURY]



def log2(n):
    return math.log(n, 2)

def sqrt(n):
    return math.sqrt(n)

def n(n):
    return n

def nlogn(n):
    return n * log2(n)

def n2(n):
    return n ** 2

def n3(n):
    return n ** 3

def exp2n(n):
    return 2 ** n

def factorial(n):
    return math.factorial(n)

# log2 omitted because it exceeds the maximum recursion depth
functions = [sqrt, n, nlogn, n2, n3, exp2n, factorial]



def find_max_runtime(f, time):
    n = 2
    n_old = 1

    while f(n) <= time:
        n_old = n
        n *= 2

    return find_max_runtime_helper(f, time, n_old, n)

def find_max_runtime_helper(f, time, lower_n, upper_n):
    if lower_n + 1 == upper_n:
        return lower_n
    else:
        middle_n = lower_n + ((upper_n - lower_n) // 2)

        if f(middle_n) <= time:
            return find_max_runtime_helper(f, time, middle_n, upper_n)
        else:
            return find_max_runtime_helper(f, time, lower_n, middle_n)



[([print(find_max_runtime(f, time)) for f in functions], print()) for time in times]
