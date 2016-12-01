"""
Describe how you could use a single array to implement three stacks. p. 202

1. Ask clarifying questions.
    - What kind of data is in the stacks?
        - Assume numbers
    - How big are the stacks?
        - Assume that they can be big, but there will be plenty of memory left
    - Are the stacks different sizes?
        - Assume yes, but not different enough to optimize based on size
    - What operations do we need to perform on the stack?
        - Assume create, push, pop, peek
    - How do we specify which stack to operate on?

2. Design an algorithm.

Idea 1: internal array where the ith stack (i = 0, 1, or 2) has entries in positions (3k + i)
    - Advantages: could theoretically generalize to n stacks (though at some point it might not be worthwhile)
    - Disadvantages: if one stack is a lot bigger, there's a lot of wasted space

3. Write pseudocode.

Seems like a waste of time here.

4. Write real code.
"""

class 3Stack:
    stack_sizes = [0, 0, 0]
    array = [None] * 1024

    def _top_index(self, stack):
        return 3 * self.stack_sizes[stack] + stack

    def _set(self, stack, index, data):
        index = self._top_index(stack)
        if index >= len(self.array):
            self.array += [None] * len(self.array)
        self.array[index] = data

    def push(self, stack, data):
        stack_sizes[stack] += 1
        self._set(stack, index, data)

    def pop(self, stack):
        stack_sizes[stack] -= 1
        self._set(stack, index, None)

    def peek(self, stack):
        index = self._top_index(stack)
        return self.array[index]

"""
5. See if we can make improvements to the code.

Done. Refactored duplicate code into _set.

6. Test the code.

That would take a while.

7. Postmortem

The solution was to divide the stack into 3 continuous parts. This is very similar to my implementation, but easier to visualize.
"""
