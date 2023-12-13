class Employee:
    # class attribute
    company = 'devTech.io' 
    pay_rate = 100000
    work_hours = 0

    # constructor
    def __init__(self, name, gender, age, profession):
        # instance attribute
        self.name = name
        self.gender = gender
        self.age = age
        self.age = profession

    # instance method
    def salary(self, work_exp):
        return Employee.pay_rate * work_exp
    
    # instance method
    def work_duration(self, hours):
        Employee.work_hours = hours
        print(f'you have worked for {hours} hours')

    # class method
    @classmethod
    def increase_salary(cls):
        if cls.work_hours >= 2000:
            cls.pay_rate += 1000
            print(f'your new pay rate is {cls.pay_rate}')
        else:
            return f'your pay rate is still the same'
    
    # static method      
    @staticmethod
    def receive_dept(new_dept):
        print(f'your new department is {new_dept}')
    
# creating objects of the Employee class    NB: object == instance
emeka_obj = Employee('emeka', 'male', 23, 'frontend developer')
inie_obj = Employee('ini-ubong', 'male', '2x', 'fullstack_developer')
print(emeka_obj.gender)
print(inie_obj.pay_rate)
print(inie_obj.salary(8))
inie_obj.increase_salary()
inie_obj.receive_dept('executive')
emeka_obj.receive_dept('marketing')

