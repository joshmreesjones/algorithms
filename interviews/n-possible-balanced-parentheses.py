"""
Print all possible n pairs of balanced parentheses.

For example, for n = 2:
    (())
    ()()
"""

def balanced_parentheses(n):
    if n == 0:
        return [""]
    elif n == 1:
        return ["()"]
    else:
        previous = balanced_parentheses(n - 1)
        result = []
        for i in range(len(previous)):
            result.append("()" + previous[i])
            result.append("(" + previous[i] + ")")
            result.append(previous[i] + "()")
        return result

def print_all(list_of_strings):
    for string in list_of_strings:
        print(string)

print_all(balanced_parentheses(1))
print("\n")
print_all(balanced_parentheses(2))
print("\n")
print_all(balanced_parentheses(3))
print("\n")
print_all(balanced_parentheses(4))
