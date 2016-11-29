from math import ceil

def swap(string):
    if len(string) == 1:
        return string
    elif len(string) == 2:
        return string[1] + string[0]
    else:
        middle = ceil(len(string) / 2)
        return swap(string[:middle]) + swap(string[middle:])

string1 = "abcdefgh"
result1 = "badcfehg"

string2 = "abcdefg"
result2 = "badcfeg"

print(swap(string1))
print(result1)

print()

print(swap(string2))
print(result2)
