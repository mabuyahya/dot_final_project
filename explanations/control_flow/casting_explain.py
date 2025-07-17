"""casting"""
"""to cast to a certain type, use the type name as a function"""
"""call the constructor of the type you want to cast to and give it the value you want to cast """
"""and the constructor will return an object cast to that type"""
""""""


"""example:"""

"""int: integer number"""
"""anything can be converted to an integer, but it must be a whole number"""
a = int("5")
# print(a)  # → 5
a = int(5.5)
# print(a)  # → 5
a = int(True)
# print(a)  # → 1
a = int(False)
# print(a)  # → 0
# a = int("5.5")  # raises ValueError: invalid literal for int()
a = int('4')
print(a)  # → 4

"""float: floating point number"""
"""anything can be converted to a float, but it must be a whole number"""
a = float("5")
# print(a)  # → 5.0
a = float(5.5)
# print(a)  # → 5.5
a = float(True)
# print(a)  # → 1.0
a = float(False)
# print(a)  # → 0.0
# a = float("5.5")  # raises ValueError: could not convert string
a = float('4')
print(a)  # → 4.0

"""str: string"""
"""anything can be converted to a string"""
a = str(5)
# print(a)  # → '5'
a = str(5.5)
# print(a)  # → '5.5'
a = str(True)
# print(a)  # → 'True'
a = str(False)
# print(a)  # → 'False'
a = str('4')
print(a)  # → '4'

"""bool: boolean"""
"""anything that is not empty, zero, or False is True"""
a = bool(1)
# print(a)  # → True
a = bool(0)
# print(a)  # → False
a = bool(5)
# print(a)  # → True
a = bool(5.5)
# print(a)  # → True
a = bool("True")
# print(a)  # → True
a = bool("False")
# print(a)  # → True
a = bool("")
# print(a)  # → False

"""list: list"""
"""anything can be converted to a list, but it must be iterable"""
a = list("hello")
# print(a)  # → ['h', 'e', 'l', 'l', 'o']
a = list((1, 2, 3))
# print(a)  # → [1, 2, 3]
a = list(range(5))
# print(a)  # → [0, 1, 2, 3, 4]
a = list({1, 2, 3})
# print(a)  # → [1, 2, 3]
a = list({1: 'one', 2: 'two', 3: 'three'})
# print(a)  # → [1, 2, 3]
a = list(True)
# print(a)  # → [True]
a = list(False)
# print(a)  # → [False]
a = list('4')
print(a)  # → ['4']
"""tuple: tuple"""
"""anything can be converted to a tuple, but it must be iterable"""
a = tuple("hello")
# print(a)  # → ('h', 'e', 'l', 'l', 'o')
a = tuple((1, 2, 3))
# print(a)  # → (1, 2, 3)
a = tuple(range(5))
# print(a)  # → (0, 1, 2, 3, 4)
a = tuple({1, 2, 3})
# print(a)  # → (1, 2, 3)
a = tuple({1: 'one', 2: 'two', 3: 'three'})
# print(a)  # → (1, 2, 3)
a = tuple(True)
# print(a)  # → (True,)
a = tuple(False)
# print(a)  # → (False,)
a = tuple('4')
# print(a)  # → ('4',)    
"""set: set"""
"""anything can be converted to a set, but it must be iterable"""
a = set("hello")
# print(a)  # → {'h', 'e', 'l', 'o'}
a = set((1, 2, 3))
# print(a)  # → {1, 2, 3}
a = set(range(5))
# print(a)  # → {0, 1, 2, 3, 4}
a = set({1, 2, 3})
# print(a)  # → {1, 2, 3}
a = set({1: 'one', 2: 'two', 3: 'three'})
# print(a)  # → {1, 2, 3}
a = set(True)
# print(a)  # → {True}
a = set(False)
# print(a)  # → {False}
a = set('4')
# print(a)  # → {'4'}
"""dict: dictionary"""
"""anything can be converted to a dictionary, but it must be iterable"""
a = dict([('a', 1), ('b', 2), ('c', 3)])
# print(a)  # → {'a': 1, 'b': 2, 'c': 3}
a = dict({'a': 1, 'b': 2, 'c': 3})
# print(a)  # → {'a': 1, 'b': 2, 'c': 3}
a = dict([(1, 'one'), (2, 'two'), (3, 'three')])
# print(a)  # → {1: 'one', 2: 'two', 3: 'three'}
a = dict({1, 2, 3})
# print(a)  # → {1: None, 2: None, 3: None}
a = dict(True)
# print(a)  # → {True: None}
a = dict(False)
# print(a)  # → {False: None}
a = dict('4')
# print(a)  # → {'4': None}