"""
loops
"""
"""for loops in python are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects."""
"""if you want to use a loop but with a condition, you can use a while loop."""

"""examples :"""



for a in range(5) :
    print(a)

"""the else block in a for loop is executed when the loop completes normally (i.e., not terminated by a break statement)."""
a = 0
while a < 5:
    print(a)
    a += 1
else:
    print("Loop finished")

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']

"""you can use the zip function to iterate over two or more sequences in parallel."""
for x, y in zip(a, b):
    print(x, y)

a = [1, 2, 3, 4, 5]
for i, x in enumerate(a):
    print(i, x)