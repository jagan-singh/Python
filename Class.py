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

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp1 = Employee('John', 'Doe', 50000 )
emp2 = Employee('j','d',9000)
emp = Employee('Test','T',8000)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(Employee.num_of_emps)
