class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, o):
        self.stack.append(o)
        self.size += 1

    def pop(self):
        self.size -= 1
        temp = self.stack[self.size]
        del self.stack[self.size]
        return temp

    def is_empty(self):
        return self.size == 0

    def top(self):
        return self.stack[self.size - 1]

    def size(self):
        return self.size

def parentheses_match(string):
    stack = Stack()

    for c in string:
        if c in "([{":
            stack.push(c)
        elif c in ")]}":
            if stack.is_empty():
                return False
            # If stack.pop() is not the corresponding closing character to c:
            if {"(": ")", "[": "]", "{": "}"}[stack.pop()] != c:
                return False
        else:
            raise ValueError("Input string must only have these characters: ()[]{}")

    return stack.is_empty()


tests = [
    ("()(()){([()])}", True),
    ("((()(()){([()])}))", True),
    (")(()){([()])}", False),
    ("({[})}", False),
    ("(", False)
]

passed_tests = True

for t in tests:
    if parentheses_match(t[0]) != t[1]:
        passed_tests = False
        print("Test failed:\n\t%s" % t[0])

print("Tests passed." if passed_tests else "Tests failed.")
