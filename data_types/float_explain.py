"""mutable: You can change the contents of the object without changing its identity (id)."""
"""dynamic: The object can change size — it can grow or shrink."""
"""
float
Not Dynamic: An int or float holds a single value, not a container. So there's no size to grow or shrink — it’s just one number.
Immutable: You cannot modify the value of an int or float in place.
overflow (because it is just a double in c-like languages)
"""

"""methods:"""

a = 2.0**100000000
# print(a)  # → inf

a = 2.0
b = a.is_integer()
# print(b)  # → True

a = 2.5
b = a.hex()
# print(b)  # → '0x1.4p+1'

a = 2.5
b = float.fromhex('0x1.4p+1')
# print(b)  # → 2.5

a = 2.5
b = a.as_integer_ratio()
# print(b)  # → (5, 2)