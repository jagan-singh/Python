# Object Oriented Programming
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

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullName(), self.email)



# print(Employee.num_of_emps)

# Employee.set_raise_amt(1.05)

emp1 = Employee('John', 'Doe', 50000 )
# emp2 = Employee('j','d',9000)
# emp3 = Employee('Test','T',8000)

# emp_str1 = 'Steven-Smith-80000'
# emp_str2 = 'Jane-Doe-90000'

# emp4 = Employee.from_string(emp_str1)

print(emp1.__repr__())
print(emp1)

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)
# print(Employee.num_of_emps)

# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(emp3.raise_amount)
# print(emp4.email)

# import datetime
# my_date = datetime.date(2020,06,15)

# print(Employee.is_workday(my_date))

#Inheritance
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        #Employee.__init__(self, first, last , pay) works just as the one above



class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullName())


dev  = Developer('H', 'j',10000, 'Python')
dev2 = Developer("Ja", "Jsid", 120000, 'Java')

mgr1  = Manager('Sue', 'Smith', 90000, [dev])

# print(isinstance(mgr1, Employee))
# print(issubclass(Manager, Employee))
#
# print(dev.email)
