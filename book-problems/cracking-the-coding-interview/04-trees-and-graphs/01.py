"""
Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that heights of the two subtrees of any node never differ by more than one. p. 220

1. Ask clarifying questions.
    - What kind of data is in the tree?
        - Assuming numbers

2. Design an algorithm.

Idea 1: make a helper function that returns a tuple (balanced, height) and use it to recursively check if subtrees are balanced while keeping track of height.
    - Time complexity: O(n)
    - Space complexity: O(n) due to the recursive call stack

3. Write pseudocode.

My code ended up looking a lot like Python, so I put it in the real code section.

4. Write real code.
"""

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def differ_by_one(a, b):
    return abs(a - b) <= 1

def balanced(root):
    return balanced_helper(root)[0]

def balanced_helper(node):
    if not node: return True, 0

    left = balanced_helper(node.left)
    right = balanced_helper(node.right)

    balanced = left[0] and right[0] and differ_by_one(left[1], right[1])
    height = max(left[1], right[1]) + 1

    return balanced, height

"""
5. See if we can make it faster, smaller, or cleaner.

Fixed some problems and removed duplicate code.

6. Test code.

Binary tree problems are hard to test.

7. Postmortem.

My code is similar to the solution in that it traverses each node in the tree once. I think it would be good to be prepared to avoid returning tuples, as that is a Python feature (it's easy to return a tuple of two values).

When designing the algorithm, the brute force solution crossed my mind, but I didn't think it was worth writing down. I should always write the brute force solution down.
"""
