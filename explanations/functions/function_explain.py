"""
functions
"""
"""to define a function, use the def keyword followed by the function name and parentheses."""
"""the parentheses can contain parameters, which are variables that the function can accept as input."""
"""the parameters can have a default value"""
"""when calling a function, you can use keyword arguments to specify the parameter names."""
"""the return statement is used to return a value from the function,
and if no return statement is used, the function returns None by default."""
"""*args and **kwargs are used to pass a variable number of arguments to a function."""
"""the global keyword is used to access a global variable inside a function."""
"""lambda functions are anonymous functions that can take any number of arguments but can only have one expression."""
"""they are defined using the lambda keyword followed by the arguments and a colon, then the expression"""


"""Arguments are passed by reference (like passing a pointer to the object).
Immutable types (like int, str) behave like pass-by-value (since you can't change them).
Mutable types (list, dict) can be modified inside the function."""


"""examples :"""
def foo(a, b=2):
    print(a, b)

foo(1, 2)  # → 1 2
foo(1)  # → 1 2
foo(b=1, a=2)  # → 2 1

def bar(*args, **kwargs):
    print(args, kwargs)

bar(1, 2, 3, a=4, b=5)  # → (1, 2, 3) {'a': 4, 'b': 5}

a = 10

def foo1():
    a = 5  
    print(a)

def foo2():
    global a  
    a = 20  
    print(a)
foo1()
print(a)  # This will print 10, as foo1() does not modify the global variable a
foo2()
print(a)  # This will print 20, as foo2() modifies the global variable a

a = 5
b = lambda x: x + 1
b = b(a)
print(b)  # → 6
print(a)  # → 5


a = 'c'
print(type(a))
def count_lower_and_upper(str):
    l = 0
    u = 0
    for x in str:
        if x.islower():
            u += 1
        elif x.isupper():
            l += 1
    return ('u=', u, 'l=', l)
d = count_lower_and_upper("Hello, WoRld!")
print(d)

def get_user_input_and_find_number_of_odd_and_even():
    while True:
        try:
            user_input = input("give me the number of list count:")
            user_input_int = int(user_input)
        except ValueError as error:
            print("the input most be only number")
            continue
        break
    i = 0
    list = [] 
    while i < user_input_int:
        while True:
            try :
                input_number = input("give me the number that has to be added to the list:")
                input_number_int = int(input_number)
            except ValueError as error:
                print("the input most be only number")
                continue
            break
        list.append(input_number_int)
        i += 1
    odd = 0
    even = 0
    print(list)
    for x in list:
        if x % 2 == 0:
            even += 1
        else: 
            odd += 1
    return ('even=', even, 'odd=', odd)

# print(get_user_input_and_find_number_of_odd_and_even())

def get_character_frequency(str):
    dict = {}
    for x in str:
        dict[x] = str.count(x)
    return dict
print(get_character_frequency("google.com"))
