b = ""
wordlist = list(input("Enter: "))
for i in range(len(wordlist)):
    b = b + wordlist[(len(wordlist) -1) - i]
print(b)