number = int(input("Write number: "))
factorial = 1
if number >= 0:
    while True:
        if number == 0:
            print("The factorial of ", number, " equals: ", factorial)
            break
        else:
            factorial *= number
            number -= 1
else:
    print("Your number isn't natural")
