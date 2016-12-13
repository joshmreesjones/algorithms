"""
Implement a function void reverse(char* str) in C or C++ which reverses a null-terminated string.

1. Ask clarifying questions.
    - Can I write it in Python?
        - Assuming yes
    - Is the string composed of ASCII characters?
        - Assuming yes

2. Design an algorithm.
    - Idea 1: iterate an index over the first half of the string and switch that character with the corresponding opposite character.
        - Time complexity: O(n)
        - Space complexity: O(1)

3. Write pseudocode.
Skipping this step.

4. Write real code.
"""

def reverse(string):
    string = list(string)
    end = len(string) - 1

    for i in range(len(string) / 2):
        temp = string[end - i]
        string[end - i] = string[i]
        string[i] = temp

    return "".join(string)

"""
5. See if we can make it faster, smaller, or cleaner.
Nope, looks good.

6. Check basic correctness.
Looks good.

7. Think of edge cases.
Nothing comes to mind.

8. Postmortem.
That was a very easy problem.
"""
