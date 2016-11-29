from random import randint

lines = 65535
bound = 2**31 - 1

f = open("1209-test.txt", "w")
f.write(str(lines))
f.write("\n")

for i in range(lines):
    f.write(str(randint(1, bound)))
    f.write("\n")

f.close()
