"""
Implement an algorithm to find the kth to last element of a singly linked list.

1. Ask clarifying questions.
    - Can we assume k is less than or equal to the size of the linked list?
        - Assuming yes
    - Can we assume k is > 0?
        - Assuming yes
    - Can we assume there is at least one node in the linked list?
        - Assuming yes

2. Design an algorithm.
    - Idea 1: add the linked list to a stack, then pop k elements off. The kth element popped is the kth to last element.
        - Time complexity: O(n)
        - Space complexity: O(n)
    - Idea 2: maintain two pointers starting at 0, called 'first' and 'second'. Move 'second' ahead k elements. Then, move 'first' and
      'second' ahead in parallel until 'second' is at the end. Then, the element at 'first' is the kth from last element.
        - Time complexity: O(n)
        - Space complexity: O(1)
    - Idea 3: iterate a pointer over the whole list to get the length. Then iterate another pointer over the first n - k elements. This
      pointer is now pointing at the kth to last element.
        - Time complexity: O(n)
        - Space complexity: O(1)

Ideas 2 and 3 both iterate n + (n - k) times. Idea 3 is simpler to understand and implement, so I'd go with that solution.

3. Write pseudocode.
Python is pseudocode.

4. Write real code.
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_length(root):
    length = 0
    while root:
        root = root.next
        length += 1
    return length

def kth_to_last(root, k):
    length = get_length(root)

    i = length - k
    while i > 0:
        root = root.next
        i -= 1

    return root.data

"""
5. See if we can make it faster, smaller, or cleaner.
Don't think so.

6. Check correctness and think of edge cases.
Looks good.

7. Postmortem.
I should have asked if we know the length of the linked list. If so, it would be more trivial - iterate the pointer length - k times and return the data there. It's unlikely that this is what the interviewer would want though because it's so trivial.
"""
