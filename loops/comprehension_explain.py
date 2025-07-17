"""
comprehensions
"""
"""comprehensions are a way to create lists, sets, and dictionaries in a more concise way than using loops"""

"""examples :"""
a = [x for x in range(10)]
print(a)  # → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = {x for x in range(10)}
print(b)  # → {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
c = {x: x for x in range(10)}
print(c)  # → {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

a = [x for x in range(10) if x % 2 == 0]
print(a)  # → [0, 2, 4, 6, 8]
b = {x for x in range(10) if x % 2 == 0}
print(b)  # → {0, 2, 4, 6, 8}
c = {x: x for x in range(10) if x % 2 == 0}
print(c)  # → {0: 0, 2: 2, 4: 4, 6: 6, 8: 8}

a = [x + 1 for x in range(10) if x % 2 == 0]
print(a)  # → [1, 3, 5, 7, 9]
b = {x + 1 for x in range(10) if x % 2 == 0}
print(b)  # → {1, 3, 5, 7, 9}
c = {x + 1: x for x in range(10) if x % 2 == 0}
print(c)  # → {1: 0, 3: 2, 5: 4, 7: 6, 9: 8}