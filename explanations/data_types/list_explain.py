"""mutable: You can change the contents of the object without changing its identity (id)."""
"""dynamic: The object can change size — it can grow or shrink."""
"""
list
mutable and dynamic
"""
"""A list is implemented as a resizable array of pointers to Python objects."""
"""So list is more like void*[] in C: an array of references."""

"""methods:"""

a = [1, 2, 3]
# print(a)  # → [1, 2, 3]

a = [1, 2, 3]
a[1] = 4
# print(a)  # → [1, 4, 3]

"""list is dynamic array, so it can grow and shrink as needed. and the id still the same."""
"""list are dynamic because python overallocates memory ,so it can add new elements without reallocating the array."""
a = [1, 2, 3]
a.append(4)
# print(a)  # → [1, 2, 3, 4]

"""Even if Python reallocates memory inside the list to fit more elements, the list object itself does not move."""
"""and a is a reference to the list object, so its id will not change."""
a = [1, 2, 3]
print(id(a))   # id₁
for i in range(1000000):
	a.append(i)
print(id(a))   # Still id₁

a = [1, 2, 3]
a.extend([1, 2, 3])
print(a)  # → [1, 2, 3, 1, 2, 3]



