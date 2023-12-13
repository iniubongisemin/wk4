# polymorphism
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
        print('teacher create course curriculum')

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

    def __sub__(self, obj_1):
        pass

    def __mul__(self, obj):
        pass

    def __lt__(self, obj):
        pass

    def __gt__(self, obj):
        pass

obj = A(4)
obj_1 = A(5)
# print(obj + obj_1)
# print(obj > obj_1)
print(obj ** obj_1)
print(obj - obj_1)