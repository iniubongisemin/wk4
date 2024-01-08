# oop inheritance
class Human:

    # constructor
    def __init__(self, height): 
        self.height = height
        self.age = 0

    # instance method
    def growth(self, new_age:int):
        self.age = new_age
        return self.age

class Person:
    # class attribute
    leg = 'every normal human being has 2 legs'  

    # constructor
    def __init__(self, name, complexion): # self here refers to the person object
        # instance attribute
        self.name = name 
        self.skincolour = complexion 

    # instance method 1 
    def work(self): # NB: self here refers to the function itself/-> an instance of the class
        print('i can work')

    # instance method 2
    def code(self):
        print('i build softwares with code')

    # instance method 3
    def drive(self):
        print('i know how to drive manual and automatic cars')

# multiple inheritance
class Student(Person, Human):
    
    # constructor
    def __init__(self, name, complexion, gender, height):
        self.gender = gender
        # Person.__init__(self, name, color)
        super().__init__(name, complexion) # super() here refers to the first class i.e Person
        Human.__init__(self, height)

    # instance method 1
    def get_student_name(self):
        return self.name

    # instance method 2
    def isStudent(self):
        return True
    
    # instance method 3... notice the work() method is overridden     
    def work(self):
        print('i\'m a workaholic')       

first_student = Student('ini-ubong', 'dark_skinned', 'male', '1.78m')
# print(first_student.name, first_student.leg)
# print(first_student.gender)       
# print(first_student.height)
# print(first_student.growth(5))
# print(first_student.get_student_name())
first_student.code()
first_student.drive()
first_student.work()
first_student.get_student_name()