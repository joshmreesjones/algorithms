"""
Check if a singly-linked list contains a cycle.
"""

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def contains_cycle(node):
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast: return True

    return False

root1 = Node()
root1.next = Node()
root1.next.next = Node()
root1.next.next.next = Node()
root1.next.next.next.next = Node()
root1.next.next.next.next = root1

root2 = Node()
root2.next = Node()
root2.next.next = Node()
root2.next.next.next = Node()
root2.next.next.next.next = Node()
root2.next.next.next.next = root2.next.next

root3 = Node()
root3.next = Node()
root3.next.next = Node()
root3.next.next.next = Node()
root3.next.next.next.next = Node()
root3.next.next.next.next.next = root3.next.next.next.next

root4 = Node()
root4.next = root4

root5 = Node()
root5.next = Node()
root5.next.next = root5

tests = [
    (None, False),

    (Node(), False),
    (Node(next=Node()), False),
    (Node(next=Node(next=Node())), False),

    (root1, True),
    (root2, True),
    (root3, True),
    (root4, True),
    (root5, True)
]

count = 0
for test in tests:
    count += 1
    print("Running test %d." % count)

    root = test[0]
    expected = test[1]
    assert contains_cycle(root) == expected

print("All tests passed.")
