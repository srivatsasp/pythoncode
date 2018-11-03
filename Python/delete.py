
def delDupChars(inputString):
    compareChar = set()
    outString = ''
    for char in inputString:
        if char not in compareChar:
            compareChar.add(char)
            outString += char
    print(outString)
    print(compareChar)


delDupChars('HappyBirthday')
