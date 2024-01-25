# polymorphism
# it refers to a subclass's ability to adapt a method that already exists in its superclass to meet its needs
# e.g 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book: {self.title}"
    
class Fiction(Book):
    def __init__(self, title, author, branch):
        super().__init__(title, author)
        self.branch = branch

    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Author: {self.author}"
    
author_Object = Fiction('Splinter Cell', 'Tom Clancy', 'Tel Aviv')
print(author_Object)

# OPERATOR OVERLOADING
# it means changing the way operators work for user-defined types or a feature that allows the same operator to have a different meaning depending on the context in which it is called 
# e.g 

# class A:
#     def __init__(self, a):
#         self.a = a

# obj1 = A(1)
# obj2 = A(2)
# print(obj1 + obj2)

# ex 2
class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age

# creating two Dog objects;
scott = Dog('Scott', 8)
max = Dog('Max', 7)

# we can use operator overloading to add a way to compare these two objects based on the age property:
# e.g
class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False
    
# creating two Dog objects;
scott = Dog('Scott', 8)
max = Dog('Max', 7)
print(scott > max)

class A:
    def __init__(self, a):
        self.a = a
        # adding two objects
        def __add__(self, o):
            return self.a + o.a
        
class Complex: 
    def __init__(self, a, b):
        self.a = a 
        self.b = b
        
    # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
    
    def __sub__(self, other):
        print('i am performing subtraction')
        return 

    def __gt__(self, other):
        if(self.a > other.a):
            return True
        else:
            return False
        
ob1 = Complex(1, 2)
ob2 = Complex(2, 3)
ob3 = ob1 + ob2
# print(ob1)
# print(ob2)
print(ob3)

class Novel(Book):

    def __init__(self, title, quantity, author, pages):
        super().__init__(title, quantity, author)
        self.pages = pages

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x 
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1 + p2)

# parent class 
class Human:
    def __init__(self, height):
        self.height = height
        self.age = 0

    def growth(self, new_age):
        self.age = new_age
        return self.age
    
    def __str__(self) -> str:
        return f'human obj with height {self.height}'
    
# child class one
class Student(Human):
    def __init__(self, height, name, gender):
        self.name = name
        self.gender = gender
        super().__init__(height)

    def isStudent(self):
        return True
    
    def __str__(self) -> str:
        return f'student obj with name {self.name}'

# child class two
class Manager(Human):
    def __init__(self, height, company):
        self.company = company
        super().__init__(height)

    def emp_staff(self):
        print('i employ new staff')
        
    def __str__(self) -> str:
        return f'manager obj at {self.company}'
    
# child class three
class Teacher(Human):
    def __init__(self, height, course):
        self.course = course
        super().__init__(height)

    def create_curriculum(self):
        print('the teacher is responsible for creating course curriculum')

    def __str__(self) -> str:                  
        return f'teacher obj for course {self.course}'
    
student_obj = Student(5.7, 'john', 'male')
manager_obj = Manager(6.0, 'univelcity')
teacher_obj = Teacher(5.8, 'backend')
print(student_obj)
print(manager_obj)
print(teacher_obj)


# operator overloading 
class A:
    def __init__(self, a:int):
        self.a = a

    def __add__(self, obj):
        return self.a + obj.a
    
    def __sub__(self, obj):
        return self.a - obj.a

    def __sub__(self, obj_1):
        pass

    def __mul__(self, obj):
        pass

    def __lt__(self, obj):
        pass

    def __gt__(self, obj):
        pass

obj = A(6)
obj_1 = A(5)
# print(obj + obj_1)
# print(obj > obj_1)
# print(obj ** obj_1)
# print(obj - obj_1)