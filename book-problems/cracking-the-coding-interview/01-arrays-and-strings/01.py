# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def check_unique(string):
    if len(string) > 128:
        return False

    flags = [0 for i in range(128)]

    for character in string:
        index = ord(character)

        if flags[index] > 0:
            return False
        else:
            flags[index] += 1

    return True


test_strings = [
    "abcdefghijklmnopqrstuvwxyz",
    "abbc",
    "abcb",
    "aabc",
    "abcc",
    "",
    "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "\n",
    "a"
]

test_results = [
    True,
    False,
    False,
    False,
    False,
    True,
    False,
    True,
    True
]

tests = zip(test_strings, test_results)
successes = 0
failures = 0

for test in tests:
    print("Testing string '%s'" % test[0])

    expected = test[1]
    result = check_unique(test[0])

    print("\tExpected: %s" % expected)
    print("\tResult: %s" % result)

    if expected == result:
        print("\tTest passed.")
        successes += 1
    else:
        print("\tTest failed.")
        failures += 1

print("Successes: %i" % successes)
print("Failures: %i" % failures)
