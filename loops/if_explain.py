"""
if conditional statements: if, elif, else
"""
"""the if condition is a boolean expression that evaluates to True or False."""
"""
these are considered False in Python:
0, 0.0
None
False
'' (empty string)
[], {}, set(), tuple(), etc.
"""
"""
Comparison Operators
 == , < , > , <= , >= , != , is , in .
Logical Operators
 and , or , not .
"""

"""examples :"""

a = 5
if a in [1, 2, 3, 5]:
	print("Found")

"""one line if statement"""
a = 5
if a > 0: print("positive") 

"""the pass statement is a null operation; it does nothing when executed.
the only use of the pass statement is to create a block of code that does nothing, but is syntactically correct."""
a = 5
if a < 4:
    pass