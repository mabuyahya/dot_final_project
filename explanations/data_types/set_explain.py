"""mutable: You can change the contents of the object without changing its identity (id)."""
"""dynamic: The object can change size — it can grow or shrink."""
"""
set
mutable and dynamic
"""
"""the key difference between set and the others are the it is unordered. and also it does not allow duplicates."""
"""A set is implemented as a hash table."""
"""So set is more like struct { void* value; }[] in C: an array of unique values."""
"""but it is unordered, so you cannot access elements by index. also only keys are stored, not values."""
"""frozenset is a set that is immutable, so it cannot be changed after it is created."""

"""methods:"""

a = set([1, 2, 3])
# print(a)  # → {1, 2, 3}

a = set([1, 2, 3])
a.add(4)
# print(a)  # → {1, 2, 3, 4}

"""there is no index in set, so you cannot access elements by index. so to get value you need to know the value itself."""
a = set([1, 2, 3])
a.remove(2)
# print(a)  # → {1, 3}

a = frozenset([1, 2, 3])
# print(a)  # → frozenset({1, 2, 3})
