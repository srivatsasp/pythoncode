a = input("Enter the string : ")
maxLen = 0
wordList = a.split(" ")
for i in wordList:
    if maxLen < len(i):
        maxLen = len(i)
        word = i
print ("Longest Word is: " + word)
