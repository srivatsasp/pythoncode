class Employee:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def email(self):
        return "{}.{}@email.com".format(self.firstname, self.lastname)

    @property
    def fullname(self):
        return "{}-{}".format(self.firstname, self.lastname)

    # @fullname.setter
    # def fullname(name):
    #    firstname, lastname = name.split(' ')


emp1 = Employee('Srivatsa', 'Padakandla')
emp1.fullname = 'Shilpa SSrivatsa'

print(emp1.firstname)
print(emp1.email)
print(emp1.fullname)
