firstNumber = int(input("Write first number: "))
secondNumber = int(input("Write second number: "))
while firstNumber != 0 and secondNumber != 0:
    if firstNumber > secondNumber:
        firstNumber = firstNumber % secondNumber
    else:
        secondNumber = secondNumber % firstNumber
print(firstNumber + secondNumber)
