# oop is a way of writing code in python that's heavy on the concepts of classes and objects 
# main benefit: helps to structure your program into simple reusable pieces of code 
# goal: cleaner code 
# e.g 
# soldier_one_dps = soldier_one['damage'] * soldier_one['attacks_per_second']
# soldier_two_dps = soldier_one['damage'] * soldier_one['attacks_per_second']

# using a function to refactor the code a bit;
def get_soldier_dps(soldier):
    return soldier['damage'] * soldier['attacks_per_second']

# soldier_one_dps = get_soldier_dps(soldier_one)
# soldier_two_dps = get_soldier_dps(soldier_one)

# object: an instance of a class type 
# e.g health = 50 NB: here health is an instance of integer type

# creating classes 
class Soldier:
    health = 5

# to create an instance of a Soldier, we simply call the class 
# NB: a class isn't a function, hence it doesn't take input parameters directly 

first_soldier = Soldier()
# print(first_soldier.health)  

# methods on a class
# a method is a function that is associated with a class and it has access to all the properties of the object

class Soldier:
    health = 5

    def take_damage(self, damage):
        self.health -= damage

soldier_one = Soldier()
soldier_one.take_damage(2)
# print(soldier_one.health)

# the special self value
# NB: methods always take a special parameter as their first argument called self. 
# the self variable is a reference to the object itself 
# by using it, you can read and update properties of the object
# methods are called directly on an object using the dot operator e.g
# object.method()

# NB: methods can return values and also change the properties of the object 
class Soldier: 
    armor = 2
    num_of_weapons = 2

    def get_speed(self):
        speed = 10 
        speed -= self.armor
        speed -= self.num_of_weapons
        return speed 
    
soldier_one = Soldier()
# print(soldier_one.get_speed())

# methods vs functions 
# method: piece of code that is called by a name that is associated with an object
# NB: methods and functions are similar but they have two key differences      
#1. a method is implicitly passed to the object on which it was called i.e you won't see all the inputs in the parameter list
#2. a method is able to operate on data that is contained within the class i.e you won't see all the outputs in the return statement 

# constructors in python 
# NB: in practice you rarely see a class define properties in the format given below i.e using class attributes;
class Soldier:
    armor = 2
    num_weapons = 2 

# in python, a constructor is made with the __init__() method!
# NB: it is automatically called when a new object is created 
# with a constructor the code block above would look like this:
class Soldier:
    def __init__(self):
        self.armour = 2
        self.num_of_weapons = 2

# because the constructor is also a method, we can make the starting armor and number of weapons configurable with some parameters 
# e.g
class Soldier:
    def __init__(self, armour, num_of_weapons):
        self.armour = armour
        self.num_of_weapons = num_of_weapons

soldier = Soldier(5, 10)
print(soldier.armour)
print(soldier.num_of_weapons)

