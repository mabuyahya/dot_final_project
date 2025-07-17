"""mutable: You can change the contents of the object without changing its identity (id)."""
"""dynamic: The object can change size — it can grow or shrink."""
"""
strings
immutable and not dynamic
"""
"""strings are just a sequence of characters"""
"""strings are immutable, meaning once created, they cannot be changed."""
"""so you cannot change a character in a string, but you can create a new string based on the old one."""
"""using slicing, you can create a new string from parts of the original string."""
"""slicing is done using the syntax str[start:end:step]"""

"""methods:"""

a = "hello, world!"
b = a.split()
# print(b)  # → ['hello,', 'world!']

a = ["hello", "world"]
b = "$".join(a)
# print(b) # → hello$world

a = "hello, world!"
b = a.find('$')
# print(b)  # → -1  

a = "hello, world!"
# b = a.index('$')
# print(b)  # → ValueError: substring not found

""" (in) keyword can work with any sequence type, including strings"""
a = "hello, world!"
b = 'r' in a
# print(b)  # → True

a = "hello, world!"
b = a.rsplit('l', 1)
# print(b)  # → ['hello, worl', '!']