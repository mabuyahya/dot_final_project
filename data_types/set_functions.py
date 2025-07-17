"""
set functions.
"""

"""fucntions :"""

"""add function"""
a = set([1, 2, 3])
a.add(4)
print(a)

"""remove function"""
a = set([1, 2, 3])
a.remove(2)
print(a)

"""discard function"""
"""The difference between remove and discard is that
remove will raise a KeyError if the element is not found, while discard will not."""
a = set([1, 2, 3])
a.discard(2)
print(a)

"""copy function"""
"""The copy() method returns a shallow copy of the set."""
"""shallow means that it creates a new set with the same elements as the original set."""
a = set([1, 2, 3])
b = a.copy()
b.add(4)
print(a)

"""clear function"""
a = set([1, 2, 3])
a.clear()
print(a) 

""""pop function"""
"""The pop() method removes and returns an arbitrary element from the set."""
"""If the set is empty, it raises a KeyError."""
a = set([1, 2, 3])
popped_element = a.pop()
print(popped_element)
print(a)

"""union function"""
"""The union() method returns a new set that contains all the elements from both sets."""
a = set([1, 2, 3])
b = set([3, 4, 5])
c = a.union(b)
print(c) # 1,2,3,4,5

"""intersection function"""
"""The intersection() method returns a new set that contains only the elements that are present in both sets."""
a = set([1, 2, 3])
b = set([2, 3, 4])
c = a.intersection(b)
print(c) # 2,3

"""difference function"""
"""The difference() method returns a new set that contains the elements that are in the first set but not in the second set."""
a = set([1, 2, 3])
b = set([2, 3, 4])
c = a.difference(b)
print(c) # 1

"""symmetric_difference function"""
"""The symmetric_difference() method returns a new set that contains the elements that are in either of the sets but not in both."""
a = set([1, 2, 3])
b = set([2, 3, 4])
c = a.symmetric_difference(b)
print(c) # 1,4

"""issubset function"""
"""The issubset() method returns True if the set is a subset of another set, otherwise it returns False."""
a = set([1, 2])
b = set([1, 2, 3])
print(a.issubset(b))  # True

"""issuperset function"""
"""The issuperset() method returns True if the set is a superset of another set, otherwise it returns False."""
a = set([1, 2, 3])
b = set([1, 2])
print(a.issuperset(b))  # True

"""isdisjoint function"""
"""The isdisjoint() method returns True if the set has no elements in common with another set, otherwise it returns False."""
a = set([1, 2, 3])
b = set([4, 5, 6])
print(a.isdisjoint(b))  # True

"""update function"""
"""The update() method adds elements from another set to the current set."""
a = set([1, 2, 3])
b = set([3, 4, 5])
a.update(b)
print(a) # 1,2,3,4,5 remember no duplicates in sets

"""intersection_update function"""
"""The intersection_update() method updates the current set with the intersection of itself and another set."""
a = set([1, 2, 3])
b = set([2, 3, 4])
a.intersection_update(b)
print(a) # 2,3

"""difference_update function"""
"""The difference_update() method updates the current set by removing elements found in another set."""
a = set([1, 2, 3])
b = set([2, 3, 4])
a.difference_update(b)
print(a) # 1

"""symmetric_difference_update function"""
"""The symmetric_difference_update() method updates the current set with the symmetric difference of itself and another set."""
a = set([1, 2, 3])
b = set([2, 3, 4])
a.symmetric_difference_update(b)
print(a) # 1,4
