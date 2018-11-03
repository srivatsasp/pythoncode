num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mylist = []
# for i in num:
#     mylist.append(i)
# print(mylist)

# mylist = [i for i in num if i % 2 != 0]
# print(mylist)

string = 'abcd'

# for i in string:
#     for j in range(4):
#         mylist.append((i, j))
# print(mylist)

# mylist = [(i, j) for i in string for j in range(4)]
# print(mylist)

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

mydict = {}

# for i, j in zip(names, heros):
#     mydict[i] = j
# print(mydict)

# mydict = {i: j for i, j in zip(names, heros)}
# print(mydict)

# num = [0, 1, 2, 2, 3, 4, 4, 3, 4, 4, 5, 6, 7, 7, 6, 7, 8, 9]
# myset = set()
# for i in num:
#     myset.add(i)
# print myset

# myset = {i for i in num}
# print(myset)


# def genNum(num):
#     for i in num:
#         yield i*i
#
#
# mygen = genNum(num)
#
# for i in mygen:
#     print i


def genNum(val):
    return val*val


for i in num:
    mylist.append(genNum(i))
print(mylist)
