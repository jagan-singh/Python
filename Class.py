#Object Oriented Programming
class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@company.com'
        Employee.num_of_emps +=1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)


    #instance method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    #class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True





print(Employee.num_of_emps)

Employee.set_raise_amt(1.05)

emp1 = Employee('John', 'Doe', 50000 )
emp2 = Employee('j','d',9000)
emp3 = Employee('Test','T',8000)

emp_str1 = 'Steven-Smith-80000'
emp_str2 = 'Jane-Doe-90000'

emp4 = Employee.from_string(emp_str1)



print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(Employee.num_of_emps)

print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp3.raise_amount)
print(emp4.email)

import datetime
my_date = datetime.date(2020,06,15)

print(Employee.is_workday(my_date))







