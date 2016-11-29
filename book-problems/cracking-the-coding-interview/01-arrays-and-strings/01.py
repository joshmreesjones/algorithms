"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

1. Ask clarifying questions.
    - How long can the string be?
        - Assuming it can fit in memory with lots of room to spare.
    - Is the string composed of ASCII characters?
        - Assuming yes.

2. Design an algorithm.
    - Brute force: iterate through every pair of characters and see if any match. If any pair does, return False. Otherwise, return True.
        - Time complexity: O(n^2)
        - Space complexity: O(1)
    - Sorting: sort the string by character. Iterate through each pair of characters and if any match, return False. Otherwise, return True.
        - Time complexity: O(nlog(n))
        - Space complexity: O(1), unless sorting takes extra space
    - Small hash map: initialize an array of size 256 to all 0s. For every character, check if there is a 1 in that character's position in the array. If yes, return False. If no, change it to a 1.
        - Time complexity: O(n)
        - Space complexity: O(n)

3. Write pseudocode.

function unique(string)
    if string length > 256
        return false
    else
        array = [0] * 256
        for character in string
            if array[character] is 1
                return false
            else
                array[character] = 1
        return true

4. Write real code.
"""

def unique(string):
    if len(string) > 256:
        return False
    else:
        array = [0] * 256
        for character in string:
            index = ord(character)
            if array[index] == 1:
                return False
            else:
                array[index] = 1
        return True

"""
5. Test code.
"""

tests = [
    ("", True),
    ("a", True),
    ("aA", True),
    ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
    ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZa", False),
    ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZA", False),
    ("  ", False)
]

for test in tests:
    assert unique(test[0]) == test[1]

print("Tests passed.")
