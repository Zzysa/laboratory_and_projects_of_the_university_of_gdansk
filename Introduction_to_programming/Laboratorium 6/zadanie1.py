naturalNumbers = []
middleList = []  # zbiór wszystkich liczb nie prostych
finalList = []  # zbiór wszystkich liczb prostych
startNumber = 0
divider = 2
number = 1

userNumber = int(input("Write the border natural number that less then 1000: "))

if userNumber <= 1000 and userNumber > 1:  # obramowanie liczb, aby użytkownik nie przekroczył granic
    for i in range(2, userNumber + 1):
        naturalNumbers.append(i)

    while True:  # zmienna "number" pokazuje, ile razy pętla for przejdzie
        if number ** 2 <= userNumber:
            number += 1
        else:
            break

    for j in range(1, number):
        for i in range(len(naturalNumbers)):
            if naturalNumbers[i] % divider == 0 and i != startNumber: # sparwdamy czy możemy dodać liczbe w "middleList"
                if naturalNumbers[i] not in middleList:  # sprawdzamy, żeby liczba nie było w "middleList"
                    middleList.append(naturalNumbers[i])
        startNumber += 1
        divider += 1

    for i in range(len(naturalNumbers)):  # elementy co znajdują się w "middleList" nie są proste dlatego wyrzucamy ich
        if not naturalNumbers[i] in middleList:
            finalList.append(naturalNumbers[i])

else:
    print("Your number is not natural")

print(finalList)
