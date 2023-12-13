# # oop inheritance
# class Human:

#     # constructor
#     def __init__(self, height):
#         self.height = height
#         self.age = 0

#     # instance method
#     def growth(self, new_age):
#         self.age = new_age
#         return self.age

# class Person:
#     leg = '2 legs' # class attribute 

#     # constructor
#     def __init__(self, name, complexion): # self here refers to the person object
#         # instance attribute
#         self.name = name 
#         self.color = complexion 

#     # instance method 1 
#     def work(self): # NB: self refers to the function itself/-> an instance of the class
#         print('i can work')

#     # instance method 2
#     def code(self):
#         print('i can build softwares with code')

#     # instance method 3
#     def drive(self):
#         print('i know how to drive manual and automatic cars')

# # multiple inheritance
# class Student(Person, Human):
    
#     # constructor
#     def __init__(self, name, complexion, gender, height):
#         self.gender = gender
#         # Person.__init__(self, name, color)
#         super().__init__(name, complexion)
#         Human.__init__(self, height)

#     # instance method 1
#     def get_student_name(self):
#         return self.name

#     # instance method 2
#     def isStudent(self):
#         return True
    
#     # instance method 3... notice the work() method is overidden 
#     def work(self):
#         print('i\'m a workaholic')       

# first_student = Student('ini-ubong', 'dark_skinned', 'male', '1.78m')
# print(first_student.name, first_student.leg)
# print(first_student.gender)
# print(first_student.height)
# print(first_student.growth(5))
# print(first_student.get_student_name())
# first_student.code()
# first_student.drive()
# first_student.work()
# first_student.get_student_name()

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
