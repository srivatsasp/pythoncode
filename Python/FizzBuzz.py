a = int(input("Enter a number : "))
i = 1
while i <= a:
    if i % 3 == 0 and i % 5 != 0:
        print('Fizz')
    elif i % 3 != 0 and i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    else:
        print(i)
    i += 1
