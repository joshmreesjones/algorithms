"""
Write a braces/brackets/parentheses validator. Given a string, do the
braces/brackets/parentheses match up (in order and opened then closed)?
"""

def validate(string):
    pairs = {"(": ")", "{": "}", "[": "]"}
    stack = []

    for char in string:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack) == 0 or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0

tests = [
    ("", True),

    ("()", True),
    ("{}", True),
    ("[]", True),

    ("(){}[]", True),
    ("((()))", True),
    ("({[]})", True),
    ("([][])", True),

    ("(", False),
    (")", False),
    ("{", False),
    ("}", False),
    ("[", False),
    ("]", False),

    ("(()", False),
    ("{}}", False),
    ("{]", False),
    ("({[})]", False)
]

count = 0
for test in tests:
    count += 1
    print("Running test %d." % count)

    string = test[0]
    expected = test[1]
    assert validate(string) == expected

print("All tests passed.")
