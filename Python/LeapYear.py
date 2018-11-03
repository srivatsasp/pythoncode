numOfdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    return year % 4 == 0


def daysinMonth(month, year):

    if month == 2 and isLeapYear(year):
        return 29
    elif month > 12 or month < 1:
        return "Invalid Month"
    else:
        return numOfdays[month]


print(isLeapYear(1900))
print(daysinMonth(1, 1900))
