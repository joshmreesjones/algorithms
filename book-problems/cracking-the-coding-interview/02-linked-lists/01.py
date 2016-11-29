"""
Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?

1. Ask clarifying questions.
    - Is the linked list singly linked or doubly linked?
        - Assuming singly linked
    - What kind of data does the linked list contain?
        - Assuming numbers
    - Should the function return the head of the linked list?
        - Assuming yes
    ----------------
    - Does the function have to return the list in the same order?
        - Assuming no, order doesn't matter

2. Design an algorithm.
    - Sort the list (mergesort), then iterate through and remove duplicates by looking at the current node and next node, and unlink all of the duplicates.
        - Time complexity: O(nlog(n))
        - Space complexity: O(nlog(n)) due to the mergesort call stack
    - Make a hashset. Iterate through the linked list and put items into the hashset. Then either build a new linked list with the hashset's items or iterate through the linked list again to remove duplicates.
        - Time complexity: O(n)
        - Space complexity: O(n)

3. Write pseudocode.

function remove_duplicates(node)
    items_set = hashset()
    for item in linked list
        add item to items_set

    remove first linked list item from item set
    for item in linked list
        if next item in item_set, unlink it

    return the list

4. Write real code.
"""

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def remove_duplicates(root):
    items_set = set()
    node = root
    while node != None:
        items_set.add(node.data)
        node = node.next

    node = root
    if node: items_set.remove(node.data)
    while node != None and node.next != None:
        if node.next.data in items_set:
            node.next = node.next.next
        else:
            node = node.next

    return root

"""
5. Test code.
"""

# That would take a lot of work.

"""
Postmortem:
I could have maintained the hashset and removed duplicates along the way, which would save a pass over the linked list.
I forgot to figure out how to do this without a temporary buffer. Strategy:
    - Maintain two pointers, p1 and p2. p1 iterates through every element once. For each location of p1, p2 iterates through the remaining elements to check for duplicates. If at any point p1 and p2 point to duplicates, remove the one at p2.
        - Time complexity: O(n^2)
        - Space complexity: O(1)
"""
