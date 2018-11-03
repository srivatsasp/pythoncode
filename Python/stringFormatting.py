import datetime

employee = {"name": "Srivatsa", "age": 34, "pay": 150000}

# text = "Salary paid to {0}, age {1} is {2}".format(
# employee["name"], employee["age"], employee["pay"])

# text = "Salary paid to {name}, age {age} is {pay}".format(**employee)
# print(text)

# for i in range(11):
#     text = 'The value of number is {:03}'.format(i)
#     print(text)

# pi = 3.142678909
# text = 'The value of Pi is {:.3f}'.format(pi)
# print(text)

# text = "1MB can also be represented by {:,.2f}".format(1000**2)
# print(text)


myDate = datetime.datetime(2018, 11, 01, 16, 59, 00)
print(myDate)

text = "Today is {0:%B %d, %Y} which is a {0:%A}, {0:%j}th day of the year".format(myDate)
print(text)
