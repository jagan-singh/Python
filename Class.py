#Object Oriented Programming
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@company.com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('John', 'Doe', 50000 )
emp2 = Employee('j','d',9000)

print(emp1.first)
print(emp1.last)
print(emp1.pay)
print(emp1.email)
print(emp1.fullName())
print(emp2.fullName())
