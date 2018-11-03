sum1 = 0
sum2 = 0
a = 'LISTEN'
b = 'NETLIS'
if len(a) == len(b):
    wordlist1 = list(a)
    wordlist2 = list(b)
    for i in range(len(wordlist1)):
        sum1 = sum1 + ord(wordlist1[i])
        sum2 = sum2 + ord(wordlist2[i])
    if sum1 == sum2:
        print("Vales are good")
    else:
        print("Not good")
else:
    print("Really not good")
