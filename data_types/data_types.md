# 🐍 What is Anaconda?

**Anaconda is a free and open-source distribution of Python (and also R), designed especially for:**

* Data science
* Machine learning
* Scientific computing
* Python development in general

##  🔧 What does Anaconda include?
1. `Python` itself (the programming language).

2. Conda – a tool for managing packages and environments.

3. Many preinstalled libraries like NumPy, Pandas, Matplotlib, etc.

4. Optional GUI apps like:

    - Anaconda Navigator (a point-and-click interface)

    - Jupyter Notebook (a coding notebook)

    - `Spyder` (a Python IDE)

**So instead of installing Python and every library one by one, Anaconda gives you everything in one setup.**

### Python Variables - (Key Differences between python and other languages  )

1. `Dynamic Typing`: Unlike statically typed languages, Python variables don't need type declarations. The interpreter determines types at runtime:
    * بعرف لحاله شو نوع الداتا

2. `Everything is an Object`: In Python, even basic types like integers are objects with methods.
    * مش زي c بحط الرقم جوا بايتس بالميموري , لا بروح بعمل اوبجيكت
3. `Reference Semantics`: Python variables are references to objects, not memory locations holding values directly:
    اسم المتغير ما راح يكون مكان في الميموري , لا راح يكون مؤشر على اوبجيكت

## Core Data Types

# Numeric Types: (`immutable`)
1. int: Arbitrary precision integers (no overflow like in C)
2. float: Double precision floating point
3. complex: Built-in complex numbers
# Text: str - Unicode strings, (`immutable`)

# Collections:

1. list: Mutable, ordered sequences
2. tuple: Immutable, ordered sequences
3. dict: Hash tables (key-value pairs)

**What does "immutable" mean? It means once a numeric object is created, its value cannot be changed. Instead, if you change it, Python creates a new object in memory.**

### more differences between python and other languages  

## No Explicit Pointers

* You don't use pointers like in C/C++, in Python, you never write &x or *ptr.

### the difference between list, tuple, dict
## list
1. [1, 3, t]
2. mutable
3. indexed
4. slow
5. lot of memory
6. can be duplicate
## tuple
1. (1, 3, t)
2. immutable
3. indexed 
4. fast
5. less memory (because can't be changed)
6. can be duplicate
## dict
1. {1:'t', 3:'s' ,t:5}
2. mutable
3. indexed by the key
4. the slowest
5. allllot of memory
6. can't be duplicate
##  set
1. set([1,2,3,4])
2. mutable
3. unindex
## array (import array)
1. array.array('i', [20,20,20])
2. mutable
3. indexed 
4. very fast