number = int(input("Write natural number: "))
sum = 0
if number >= 0:
    for i in range(number + 1):
        sum += i
        i += 1
    print("The sum of numbers equals: ", sum)
else:
    print("Your number isn't natural")
