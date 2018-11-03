# num = [4, 5, 1, 3, 9, 1, 0, 3, 7, 6]
# num = (4, 5, 1, 3, 9, 1, 0, 3, 7, 6)
#
# sNum = sorted(num, reverse=False)
# # num.sort()
# print sNum
# print num

from operator import attrgetter


class Employee:

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay

    def __repr__(self):
        return "{} {} ${}".format(self.firstname, self.lastname, self.pay)

    def sortBy(self):
        return self.pay


emp1 = Employee('Srivatsa', 'Padakandla', 150000)
emp2 = Employee('Praveen', 'Gupta', 200000)


emp = [emp1, emp2]

# sEmp = sorted(emp, key=Employee.sortBy, reverse=True)
# print(sEmp)

sEmp = sorted(emp, key=attrgetter('pay'), reverse=True)
print(sEmp)
