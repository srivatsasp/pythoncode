
class Employee:
    num_of_emps = 0
    raisePercent = 1.04

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + '.' + lastname + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def raiseAmount(self):
        self.pay = int(self.pay * self.raisePercent)

    @classmethod
    def countEmp(cls):
        cls.num_of_emps += 1

    @classmethod
    def raisePer(cls, raisePercent):
        cls.raisePercent = raisePercent

    def __len__(self):
        return len(self.fullname())

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def __add__(self, others):
        return self.firstname + others.lastname

    def __sub__(self, others):
        return self.pay - others.pay


emp1 = Employee('Srivatsa', 'Padakandla', 100000)
emp2 = Employee('Shilpa', 'Srivatsa', 75000)
print(emp1.fullname())
print(len(emp1))
print(str(emp1))

print(emp1 - emp2)
