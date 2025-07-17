"""mutable: You can change the contents of the object without changing its identity (id)."""
"""dynamic: The object can change size — it can grow or shrink."""
"""
dictionary 
mutable and dynamic
"""
"""A dictionary is implemented as a hash table."""
"""So dict is more like struct { void* key; void* value; }[] in C: an array of key-value pairs."""
"""dictionary is like a list but with keys instead of indices."""

"""methods:"""

a = {"x": 1, "y": 2, "z": 3}
# print(a)  # → {'x': 1, 'y': 2, 'z': 3}

a = {"x": 1, "y": 2, "z": 3}
a["y"] = 4
# print(a)  # → {'x': 1, 'y': 4, 'z': 3}

a = {"x": 1, "y": 2}
a["z"] = 3
# print(a)  # → {'x': 1, 'y': 2, 'z': 3}

