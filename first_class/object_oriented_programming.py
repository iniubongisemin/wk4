# classes must start with capital letters 
# instance attribute is bound to the class object 
# instance attribute is created in the "constructor"
class Person:
    leg = 2 # class attribute 
    def __init__(self, name, color): # self here refers to the person object
        self.name = name # instance attribute
        self.color = color # instance attribute

    def work(self): # NB: self refers to the function itself/-> an instance of the class
        print('i can work')

    

john = Person('inie', 'chocolate') # object one of Person
mike = Person('success', 'fair') # object one of Person
alex = Person('peter', 'blond') # object one of Person

# print(Person.leg)
# print(Person.work('ise'))
# print(john.leg)
# print(john.name)
# print(mike.leg)
# print(mike.name)
# print(mike.work())

class Phone:

    # declaring the class attribute 
    camera = "front_camera:100MP & back_camera:128MP" # class attribute

    # declaring the instance attributes
    def __init__(self, provider, charging_method, model) -> None:
        self.network_provider = provider    # instance attribute          
        self.charging = charging_method     #         ''
        self.phone_model = model            #         ''

iPhone = Phone('mtn', 'wireless_charging', 'iPhone-X')
samsung = Phone('airtel', 'cable_charging', 'galaxy A32')

# print(iPhone.phone_model, iPhone.camera, iPhone.charging)
# print(samsung.phone_model, samsung.camera, samsung.charging)


# constructors in python
# NB: your class can take as many instance methods as possible 
# NB: creating attributes is the same thing as creating variables in python just that they start with self!
class School:
    # declaring the class attribute
    location = 'lagos'

    # declaring the instance attribute
    def __init__(self, name, addr) -> None: # NB: name is just a parameter
        self.school_name = name
        self.address = addr
        self.courses = ['backend', 'frontend', 'product design', 'data science', 'machine learning']

    # declaring an instance method
    def admission(self, student): 
        students = []
        students.append(student)
        return students
    
    # declaring another instance method 
    def course_option(self, course):
        for c in self.courses:
            if course == c:
                print(f'congratulations you\'ve been admitted into the {c} course')
            else:
                print(f'sorry we do not have {c} course in our program yet')

univel = School('univelcity', '42 montgomery road, yaba')
gomycode = School('gomycode', '230 Herbert Macaulay way, alagomeji')
decagon = School('decagon', 'orchid road, lekki peninsula II')
# print(univel.address)
# print(univel.admission('john'))
# print(univel.course_option('backend'))
# print(gomycode.address)
# print(gomycode.admission('stacy'))
# print(gomycode.course_option('frontend'))
# print(decagon.address)
# print(decagon.admission('kazeem'))
# print(decagon.course_option('software engineering'))

# example
class Customer:
    # declaring the class attribute
    all_products = ['drinks', 'pasta', 'burgers']

    # declaring the instance attribute 
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
    # declaring the first instance method
    def place_order(self, what_you_want_to_buy):
        self.order = what_you_want_to_buy
        self.cart = [].append(self.order)
    # declaring the second instance method
    def cancel_order(self):
        self.cart = []
    # declaring the third instance method 
    def __str__(self) -> str:
        return f'my name is {self.name} i\'m learning object oriented programming'
    
# assigning the object to a variable 
customer_one = Customer('inie', 'eugeneinie@outlook.com')
customer_one.place_order('1 carton of malteasers, mars, bounty, sneakers and toblerone milk chocolates each')
print(customer_one)
print(customer_one.name)
print(customer_one.order)
print(customer_one.email)

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
# print(inies_score.course_grade(80))

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