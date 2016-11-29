lock1 = int(input())
lock2 = int(input())

# lock1 will be tested with even numbers (including 0000)
# lock2 will be tested with odd numbers

print("yes" if lock1 % 2 == 0 or lock2 % 2 == 1 else "no")
