import datetime


class Employee:
    num_of_emps = 0
    raisePercent = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + '.' + lastname + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {} - {}'.format(self.firstname, self.lastname, self.pay)

    def raiseAmount(self):
        self.pay = int(self.pay * self.raisePercent)

    @classmethod
    def countEmp():
        Employee.num_of_emps += 1

    @classmethod
    def raisePer(cls, raisePercent):
        cls.raisePercent = raisePercent

    @staticmethod
    def workingDay(myday):
        if (myday.weekday() == 5 or myday.weekday() == 6):
            return 'Holiday'
        return Employee.num_of_emps


emp1 = Employee('Srivatsa', 'Padakandla', 100000)
Employee.countEmp()
print(emp1.num_of_emps)

emp1.raiseAmount()
print(emp1.pay)
print('---------------------------')
emp2 = Employee('Shilpa', 'Srivatsa', 75000)
Employee.countEmp()

emp2.raiseAmount()
print(emp2.num_of_emps)
print(emp2.pay)

print('---------------------------')
Employee.raisePer(1.025)

myday = datetime.date(2018, 10, 23)
print(Employee.workingDay(myday))
