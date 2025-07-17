"""
classes
"""
"""class is a blueprint for creating objects"""
"""classes are used to create user-defined data structures"""
"""class is defined using the class keyword followed by the class name"""

"""a very important point to understand that if you want to access a object attribute or method you have to use the dot notation"""
"""the dot give you the ability to access the object things, just like structures in C or C++"""

"""but in depth when you define a class you are making a new object of type **type**"""
"""inside that object you have a dictionary that contains the class methods and attributes (the global ones)"""

"""and when you create an instance of that class you are creating a new object of type **class(the class name)**"""
"""and inside that object you have a dictionary that contains the instance methods and attributes (the local ones)"""
"""and also the instance has a reference to the class object so you can access the class methods and attributes"""

"""so for now we know that the class is a object and contains methods"""
"""and an object is a object that contains attributes and pointer to the class object so the object can access the class methods"""
"""let's imagine that im now have two instance one has the name 'sameer' and the other has the name 'mohamed'"""
"""and both objects have the same reference to the class object that contains the class methods"""
"""so now sameer and mohamed can access the class methods(both will access the same class methods)"""
"""but the same method should act differently for each object"""
"""so imagine that i have a method called get_info() that prints the name of the object"""
"""so when i call get_info() on sameer it will print 'sameer' and when i call it on mohamed it will print 'mohamed'"""
"""so the method get_info() is the same for both objects but it acts differently for each object"""
"""so the method get_info() need to has access to the object that called it atrtributes"""
"""and this is done by passing the object itself as the first argument to the method"""
"""self is the first argument to the method and it refers to the object that called the method"""

"""inheritance is just adding a reference to the parent class object in the child class object"""
"""so the child class **instance** didn't find the method in its own dictionary it will look for it in the parent class object"""
"""and the child class **object** can access the parent class methods using the super() function"""

"""the class **instance** object stores the class reference in its __class__ attribute"""
"""and the class **object** stores his parent class reference(if he inherits from one) in its __bases__ attribute"""

"""example:"""

class Explain:
    def explain(self):
        print("This is an explanation of classes.")

# print(Explain.__dict__)

a = Explain() 

# print(a.__dict__)



class employee:
    count = 0
    def __init__(self, id, name, salary, age, email):
        self.ID = id
        self.Name = name
        self.Salary = salary
        self.age = age
        self.email = email
        self.tax = 0.1
        employee.count += 1
    def set_data(self, id, name, salary, age, email):
        self.ID = id
        self.Name = name
        self.Salary = salary
        self.age = age
        self.email = email
    def get_info(self):
        print('name :', self.Name)
        print('id :', self.ID)
        print('salary :', self.Salary)
        print('age :', self.age)
        print('email :', self.email)
sameer = employee(20201, 'sameer', 1000, 2, 'sameer@gmail')
mohamed = employee(20202, 'mohamed', 2000, 3, 'mohamed@gmail')

class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
    def assign_department(self, emp_department):
        self.emp_department = emp_department 
    def print_employee_details(self):
        print("id :", self.emp_id)
        print("name :", self.emp_name)
        print("salary :", self.emp_salary)
        print("department :", self.emp_department)
    def  calculate_emp_salary(self, salary, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50 
            overtime_amount = (overtime * (self.emp_salary / 50))
        self.emp_salary += overtime_amount

list = [-25, -10 , -7, -3, 2, 4, 8, 10]
result = []

for x in list:
    for y in list:
        for z in list:
            if (x + y + z) == 0:
                    result.append([x, y, z])

class animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("i am an animal and my name is ",self.name)

class cat(animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def speak(self):
        print("i am a cat and my name is ", self.age)

class msh_darawsheh(cat):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color 
    def speak(self):
        super().speak()
        animal.speak(self)

bs = cat(name='om almsabeh', age='-1')

bs.is_dead = True
setattr(bs, 'has_children', True)

tt = msh_darawsheh('mohamemd', 100, 'ani msh pesseh')
tt.speak()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("person name :", self.name, "person age :", self.age)

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.subject_list = []
    def add_subject(self,subject):
        self.subject_list.append(subject)
    def show_subjects(self):
        print(self.subject_list)

class teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.schedule_list = {}

    def add_to_schedule(self, day, subject):
        self.schedule_list.update({day : subject}) 
    def show_schedule(self):
        for x, y in self.schedule_list.items():
            print(f"in day :{x}, you have :{y}")

class Classroom:
    def __init__(self):
        self.student_names = set()
    def add_student(self,name): 
        self.student_names.add(name)
    def show_students(self):
        print("the classroom students are:")
        for x, y in  enumerate(self.student_names):
            print(f"{x + 1}. {y}")
print("person class testing")
name = input("inter person name :")
age = input("inter person age :")
p = Person(name, age)
p.introduce()
print("student class testing")
name = input("inter Student name :")
age = input("inter Student age :")
s = Student(name, age)
sub = input("inter subject for the student :")
s.add_subject(sub)
s.show_subjects()
print("teacher class testing :")
name = input("inter teacher name :")
age = input("inter teacher age :")
t = teacher(name, age)
sub = input("inter teacher subject :")
day = input("inter subject day :")
t.add_to_schedule(day, sub)
t.show_schedule()
print("classroom class testing :")
c = Classroom()
student = input("inter student that need to be added to the classroom :")
c.add_student(student)
c.show_students()

