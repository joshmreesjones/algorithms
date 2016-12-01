"""
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height. p. 222

1. Ask clarifying questions.

2. Design an algorithm.

Idea 1: use a balanced tree data structure and simply insert elements in order. This isn't a great idea because we can take advantage of the fact that the array is sorted.

Idea 2: Implement a binary search tree insertion such that the algorithm simply adds a leaf node where it sees fit. Then recurse over the array in the same way as a binary search would and insert elements to the binary search tree in that order.
    - Time complexity: O(nlog(n)): O(n) to binary search over the array, O(nlog(n)) to insert into the binary tree n times
    - Space complexity: O(n): n nodes are taken up by the binary tree

3. Write pseudocode.

Python is pseudocode.

4. Write real code.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root:
        if data < root.data:
            if root.left:
                insert(root.left, data)
            else:
                root.left = Node(data)
        elif data > root.data:
            if root.right:
                insert(root.right, data)
            else:
                root.right = Node(data)
    else:
        root = Node(data)

    return root

def build_bst(array)
    return build_bst_helper(array, 0, len(array) - 1, None)

def build_bst_helper(array, start, end, root):
    halfway = (end - start) / 2 + start
    root = insert(root, array[halfway])

    if halfway != start:
        build_bst_helper(array, start, halfway - 1, root)
    if halfway != end:
        build_bst_helper(array, halfway + 1, end, root)

    return root

"""
5. See if we can make it faster, smaller, or cleaner.

Nope, looks good.

6. Test code.

Binary trees are hard to test.

7. Postmortem.

This problem took a long time to solve.

The textbook solution is O(n). Instead of repeatedly calling insert (O(log(n))), the tree is built during the recursion over the array.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_bst(array):
    return build_bst_helper(array, 0, len(array) - 1)

def build_bst_helper(array, start, end):
    if (end < start): return None

    halfway = (end - start) / 2 + start
    node = Node(array[halfway])

    node.left = build_bst_helper(array, start, halfway - 1)
    node.right = build_bst_helper(array, halfway + 1, end)

    return node
