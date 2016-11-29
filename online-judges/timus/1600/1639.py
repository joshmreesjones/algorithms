m, n = input().split();

m = int(m)
n = int(n)

# even breaks: going second wins
# odd breaks: going first wins

# The number of breaks is m * n. No matter how you break the
# chocolate, there will always be the same number of breaks.

breaks = m * n
if breaks % 2 == 0:
    print("[:=[first]")
else:
    print("[second]=:]")
