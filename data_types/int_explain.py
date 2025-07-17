"""mutable: You can change the contents of the object without changing its identity (id)."""
"""dynamic: The object can change size — it can grow or shrink."""
"""
int 
Not Dynamic: An int or float holds a single value, not a container. So there's no size to grow or shrink — it’s just one number.
Immutable: You cannot modify the value of an int or float in place.
no overflow in python
"""

"""methods:"""

a = 2**1000
# print(a)

a = 254
b = a.bit_length() 
# print(b) # → 8

a = 255
b = a.to_bytes(2, 'big') 
# print(b) # → b'\x00\xff'

a = 256
b = int.from_bytes(b, 'big')
# print(b) # → 256

"""type checking"""

a = 10
b = type(10)
# print(b) # → <class 'int'>

a =  10
b = isinstance(a, int)
# print(b) # → True

"""Type Conversion"""

a = int(True)      # → 1
a = int(False)     # → 0
a = int(3.6)       # → 3
a = int("100")     # → 100

"""address checking"""
"""the id() function returns the identity of an object (its memory address &a in c-like languages)"""
"""in python int are immutable, which means that when you create a new int object, it will never change its value"""

a = 12
b = 13
# print(id(a)) # 140737488346144
# print(id(b)) # 140737488346176

"""In this case, both a and b are assigned the same literal constant in your code.
Because Python sees this at compile time, it may optimize by pointing both a and b to the same object in memory."""
a = 100000000000
b = 100000000000
# print(id(a)) # 140737488346144
# print(id(b)) # 140737488346144

"""here i did not let the interpreter optimize the code by using int() to create new int objects."""
a = int("100000000000")
b = int("100000000000")
# print(id(a) == id(b))  # Likely False

"""dont forget that the int is immutable, so when you change the value of a, it creates a new object in memory."""
a = 50
# print(id(a))  # e.g., 140737488346144
a = a + 1
# print(id(a))  # e.g., 140737488346176


