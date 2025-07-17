"""
exception: exception handling
"""
"""exception: a problem that occurs during the execution of a program"""
"""exception handling: a way to respond to exceptions without crashing the program"""



data = list(range(5))
print(data)  # → [0, 1, 2, 3, 4]
try : 
    index = input("Enter an index to access data: ")
    index = int(index)
    print(data[index])
except IndexError as x1:
    print("IndexError:", x1)
except ValueError as x2:
    print("ValueError:", x2)
except KeyboardInterrupt as x3:
    print("KeyboardInterrupt:", x3)
except :
    print('error')

try : 
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print(int(num1) / int(num2))
except ZeroDivisionError as x1:
    print("ZeroDivisionError:", x1)
except ValueError as x2:
    print("ValueError:", x2)