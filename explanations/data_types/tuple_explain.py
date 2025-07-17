"""mutable: You can change the contents of the object without changing its identity (id)."""
"""dynamic: The object can change size — it can grow or shrink."""
"""
float not dynamic and not mutable
"""
"""in C terms: tuple is like a const struct or a fixed record of pointers."""
"""In CPython, a tuple is implemented as a fixed-size array of const object pointers (PyObject*)"""
"""so tuple is like list but it is not dynamic and and not mutable."""

"""methods:"""

a = (2, 1, 2, 3)
# print(a)  # → (2, 1, 2, 3)

a = (1, 2, 3)
b = a[1]
# print(b)  # → 2

a = (1, 2, 3)
b = a.index(2)
# print(b)  # → 1

a = (1, 2, 3)
b = a.count(2)
# print(b)  # → 1
