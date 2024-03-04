firstNumber = int(input("Write first natural number: "))
secondNumber = int(input("Write second natural number: "))
firstNumberDivisors = []
secondNumberDivisors = []
startNumber = 2  # na co dzielimy najpierw
LCM = 1  # Least Common Multiple

while True:  # szukamy wszystkie proste dzielniki "firstNumber"
    if firstNumber % startNumber == 0:
        if firstNumber / startNumber == 1:
            firstNumberDivisors.append(startNumber)
            startNumber = 2
            break
        else:
            firstNumber /= startNumber
            firstNumberDivisors.append(startNumber)
    else:
        startNumber += 1

while True: # szukamy wszystkie proste dzielniki "secondNumber"
    if secondNumber % startNumber == 0:
        if secondNumber / startNumber == 1:
            secondNumberDivisors.append(startNumber)
            break
        else:
            secondNumber /= startNumber
            secondNumberDivisors.append(startNumber)
    else:
        startNumber += 1

print("Divisors of first number: ", firstNumberDivisors)
print("Divisors of second number: ", secondNumberDivisors)

for i in range(len(firstNumberDivisors)):  # szukamy powtorzenia w "firstNumberDivisors" i "secondNumberDivisors"
    if firstNumberDivisors[i] in secondNumberDivisors:
        LCM *= firstNumberDivisors[i]  # pomnażamy LCM na powtórzenie
        secondNumberDivisors.remove(firstNumberDivisors[i])
    else:
        LCM *= firstNumberDivisors[i]  # pomnażamy jeżeli prosta liczba jest tylko dla pierwszej liczby

for i in range(len(secondNumberDivisors)):
    LCM *= secondNumberDivisors[i]  # pomnażamy jeżeli prosta liczba jest tylko dla drugiej liczby

print("Least Common Multiple: ", LCM)
