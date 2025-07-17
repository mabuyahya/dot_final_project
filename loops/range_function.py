"""
range: generates a sequence of numbers
"""

"""range(start, stop[, step]) -> range object"""

a = range(5)
b = list(a)
# print(b)  # → [0, 1, 2, 3, 4]

a = range(1, 10, 2)
b = list(a)
# print(b)  # → [1, 3, 5, 7, 9]

a = range(10, 1, -2)
b = list(a)
# print(b)  # → [10, 8, 6, 4, 2]

a = range(5, 5)
b = list(a)
# print(b)  # → []

a = range(5, 0, -1)
b = list(a)
# print(b)  # → [5, 4, 3, 2, 1]

alpha = range(ord('a'), ord('z') + 1)
beta = list(alpha)
# print(beta)  # → ['a', 'b', 'c', 'd', 'e', ... 'y', 'z']