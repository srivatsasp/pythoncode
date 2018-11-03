

def remDupChars(inputString):
    checkChar = set()
    outString = ''
    for char in inputString:
        if char not in checkChar:
            checkChar.add(char)
            outString += char
    return outString


print(remDupChars('aacccc6yyu7'))
