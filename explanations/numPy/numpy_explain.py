"""
numpy
"""

"""numpy is a fundamental package for scientific computing in Python.
It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
NumPy is widely used for numerical computations and serves as the foundation for many other scientific libraries in Python."""

"""NumPy arrays are much faster and more memory-efficient than Python lists for numerical tasks."""
"""So NumPy array is more like a C array or malloc() block with a known type (int32, float64, etc)."""
"""numPy array is mutable, meaning you can change its contents without creating a new array."""
"""but not dynamic, meaning you cannot change its size after creation."""
"""np.append(a, 4)  # returns a new array, does not modify `a`"""

import numpy as np

np.array([1.0, 2.0], dtype=np.float64)
np.array(['a', 'b'], dtype=np.str_)

a = np.array([[1, 2, 3],
              [4, 5, 6]])
a.shape     # → (2, 3)
a.ndim      # → 2 (2D array)
a.size      # → 6 (total elements)


