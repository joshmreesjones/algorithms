"""
Write a function to find the 2nd largest element in a binary search tree.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def largest(node):
    while node and node.right != None:
        node = node.right
    return node

def second_largest(node):
    most_recent = node
    while node.right:
        most_recent = node
        node = node.right
    return largest(node.left) if node.left else most_recent



a1 = Node(1)
a2 = Node(2)

a1.right = a2

a = a1



b1 = Node(1)
b2 = Node(2)

b2.left = b1

b = b2



c1 = Node(1)
c2 = Node(2)
c3 = Node(3)

c1.right = c2
c2.right = c3

c = c1



d1 = Node(1)
d2 = Node(2)
d3 = Node(3)

d1.right = d3
d3.left = d2

d = d1



e1 = Node(1)
e2 = Node(2)
e3 = Node(3)

e3.left = e1
e1.right = e2

e = e3



f1 = Node(1)
f2 = Node(2)
f3 = Node(3)
f4 = Node(4)

f4.left = f1
f1.right = f2
f2.right = f3

f = f4



tests = [
    (a, a1),
    (b, b1),
    (c, c2),
    (d, d2),
    (e, e2),
    (f, f3)
]

for test in tests:
    root = test[0]
    expected = test[1]
    assert second_largest(root) == expected
print("All tests passed.")
