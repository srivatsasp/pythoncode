a = 2112
i = 1
while a >= 0:
    val1 = ''.join(sorted(str(a), reverse = True))
    val2 = ''.join(sorted(str(a), reverse = False))
    if int(val1) - int(val2) == 6174:
        print(val1 + " - " + val2 + " = 6174")
        print("Found it in " +  str(i)  + " tries")
        break
    else:
        a = int(val1) - int(val2)
    i += 1