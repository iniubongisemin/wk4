# static method is a general utility method that performs a task in isolation  

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
        self.profession = profession

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
        if cls.work_hours <= 2000:
            cls.pay_rate += 1000
            print(f'your compensation is {cls.pay_rate}')
        else:
            return f'your pay rate is still the same'
    
    # static method      
    @staticmethod
    def job_role(job):
        print(f'ini-ubong isemin, {job} devTech.io')
    
# creating objects of the Employee class    NB: object == instance
inie_obj = Employee('ini-ubong', 'male', '2x', 'fullstack_developer')
# emeka_obj = Employee('emeka', 'male', 23, 'frontend developer')
print(inie_obj.name)
inie_obj.job_role('chairman/ceo')
print(inie_obj.pay_rate)
print(inie_obj.salary(80))
inie_obj.increase_salary()
print(inie_obj.increase_salary())
# print(emeka_obj.name)
# emeka_obj.job_role('marketing executive')

