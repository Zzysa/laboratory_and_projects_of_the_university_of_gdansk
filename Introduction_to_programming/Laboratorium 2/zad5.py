print("""What do you want to do with two numbers:
1. Sum
2. Subtraction
3. Multiplication""")
option = int(input("You can write 1,2 or 3 to choose an option: "))
firstNumber = float(input("Write first number: "))
secondNumber = float(input("Write second number: "))
if option == 1 or option == 2 or option == 3:
    if option == 1:
        print("Result of sum is: ", firstNumber + secondNumber)
    elif option == 2:
        print("Result of subtraction is: ", firstNumber - secondNumber)
    elif option == 3:
        print("Result of multiplication is: ", firstNumber * secondNumber)
else:
    print("You chose wrong option")
