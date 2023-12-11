# classes must start with capital letters 
class Person:
    leg = 2 # class attribute 
    def __init__(self, name, color): # self here refers to the person object
        self.name = name # instance attribute
        self.color = color # instance attribute

    def walk(self): # NB: self refers to the function itself/an instance of the class
        print('i can work')

class School:
    location = True
    def __init__(self, name, addr) -> None: # NB: name is just a parameter
        self.school_name = name
        self.address = addr

# univel = School('univelcity', '42 montgomery street')
# gomycode = School('gomycode', 'alagomeji')
# print(univel.admission('john'))
# print(univel. choose_course('backend'))

class Phone:
    camera = "front&back" # class attribute
    def __init__(self, provider, charging, model) -> None:
        self.charging_method = charging
        self.network_provider = provider
        self.phone_model = model 


iPhone = Phone('mtn', 'wireless', 'iPhone-X')
samsung = Phone('airtel', 'cable_charging', 'galaxy')

# print(iPhone.camera, iPhone.phone_model)
# print(samsung.charging_method)


# print(Person.leg)
# print()

john = Person('inie', 'chocolate') # object one of Person
mike = Person('success', 'fair') # object one of Person
a = Person('peter', 'blond') # object one of Person
# print(john.leg)
# print(john.name)
# print(mike.leg)
# print(mike.name)
# print(mike.walk())

# constructors in python
# NB: your class can take as many instance methods as possible 
# attributes is the same thing as creating variables in python just that they start with self!
class School:
    location = True
    def __init__(self, name, addr) -> None: # NB: name is just a parameter
        self.school_name = name
        self.address = addr
        self.courses = ['backend', 'frontend', 'product design', 'data science', 'machine learning']

    def admission(self, student): # instance method
        students = []
        students.append(student)
        return students
    
    def choose_course(self, course):
        for c in self.courses:
            if course == c:
                print(f'you are admitted into the {c} course')
            else:
                print('sorry we do not have that course in our program yet')

univel = School('univelcity', '42 montgomery street')
gomycode = School('gomycode', 'alagomeji')
# print(univel.admission('john'))
# print(univel.choose_course('backend'))

# exercise 1
# give the class two instance attributes, two instance methods, class attributes 
class Course:
    # creating the class attribute 
    location = '42 montgomery road'
    programme = 'electrical electronics engineering'
    level = 300

    # creating the instance attribute
    def __init__(self, lab) -> None:
        self.controlengineering = lab
        self.scores = [99, 80, 45, 20, 70, 75, 56, 49, 30]

    # creating the instance method  NB: your function must not have parameters if it doesnt need to
    def course_grade(self, grade): 
        # scores = []
        # for score in self.scores:
        if grade >= 75:
            print(f'your grade is A')
            # scores.append(grade)
            # print(f'the scores for those that got A are {score}')
        # else:
        #     print()
        return grade
    
    # class method
    @classmethod
    def get_location(cls):
        return cls.location
    
# calling the class method NB:you can call the class method directly from the class
Course.get_location()
    
inies_score = Course('electric machines')
print(inies_score.course_grade(80))

# exercise 2
# create a class called shop, it should have at least 2 instance attributes and at least two instance methods 

class Shop:
    shop_name = 'supermarket'

    # creating the instance attribute
    def __init__(self, drinks, chocolates) -> None:
        self.coke = drinks    
        self.bounty = chocolates

    # creating the instance methods
    def purchase(self, drink):
        if drink == 'coke':
            print('thanks for your purchase')
        else:
            print('we\'re sorry coke is out of stock')

    # creating the second instance method
    def order(self, chocolate):
        if chocolate == "sneakers":
            print('thanks for buying')
        else:
            print('we\'re sorry ndneakers is out of stock')

shop = Shop('drink', 'chocolate')
shop.purchase('fanta') 
shop.order('sneakers')