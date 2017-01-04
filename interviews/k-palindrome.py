"""
A k-palindrome is a string which transforms into a palindrome on removing at most k characters.
Given a string s, and an interger k, print "YES" if S is a k-palindrome; otherwise print "NO".

Constraints:
    s has at most 20,000 characters.
    0 <= k <= 30

Sample Test Case #1:
    Input - abxa 1
    Output - YES

Sample Test Case #2:
    Input - abdxa 1
    Output - NO
"""

def is_k_palindrome(s, k):
    if k <= 0: return s == s[::-1]
    if len(s) < 2: return True

    while s and s[0] == s[-1]:
        s = s[1:-1]

    return is_k_palindrome(s[1:], k - 1) or is_k_palindrome(s[:-1], k - 1)

tests = [
    # s, k, expected
    ["abxa", 1, True],
    ["abdxa", 1, False],
    ["aaabbbaaaaaa", 2, False],
    ["aaabbbaaaaaa", 3, True],
    ["aaabbbaaaaaa", 4, True],
    ["", 1, True],
    ["a" * 10000 + "bbb" + "a" * 9990, 2, False],
    ["a" * 10000 + "bbb" + "a" * 9990, 3, True],
    ["a" * 10000 + "bbb" + "a" * 9990, 4, True],
]

for i, test in enumerate(tests):
    s, k, expected = test
    print("Running test case %d" % i)
    assert is_k_palindrome(s, k) == expected

print("All tests passed.")
