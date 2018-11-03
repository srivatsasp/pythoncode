
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
    def countEmp(cls):
        cls.num_of_emps += 1

    @classmethod
    def raisePer(cls, raisePercent):
        cls.raisePercent = raisePercent


class Developer(Employee):
    raisePercent = 1.10

    def __init__(self, firstname, lastname, pay, progLang):
        super().__init__(firstname, lastname, pay)
        self.progLang = progLang


class Manager(Employee):
    raisePercent = 1.20

    def __init__(self, firstname, lastname, pay, directReports=None):
        super().__init__(firstname, lastname, pay)
        if directReports is None:
            self.directReports = []
        else:
            self.directReports = directReports

    def addDirectReport(self, emp):
        if emp not in self.directReports:
            self.directReports.append(emp)

    def removeDirectReports(self, emp):
        if emp in self.directReports:
            self.directReports.remove(emp)

    def printEmp(self):
        for emp in self.directReports:
            print('-->', emp.fullname())


dev1 = Developer('Srivatsa', 'Padakandla', 100000, 'Python')
dev2 = Developer('Shilpa', 'Srivatsa', 75000, 'Java')

mgr1 = Manager('Shreya', 'Padakandla', 200000, [dev1])
mgr1.printEmp()
print('----------------------------------')
mgr1.addDirectReport(dev1)
mgr1.printEmp()
print('----------------------------------')
mgr1.addDirectReport(dev2)
mgr1.printEmp()

print('----------------------------------')
mgr1.removeDirectReports(dev1)
mgr1.printEmp()
