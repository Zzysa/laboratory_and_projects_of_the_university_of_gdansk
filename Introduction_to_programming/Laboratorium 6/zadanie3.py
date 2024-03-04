# kożystałem metodem bitowych masek, żeby zrobić to zadanie
# https://ru.wikipedia.org/wiki/%D0%91%D0%B8%D1%82%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BC%D0%B0%D1%81%D0%BA%D0%B0

elementsAmount = int(input("Write amount of elements in an array: "))
array = []  # lista zawierająca wszystkie elementy zbiora
substringAmount = 2 ** elementsAmount  # ilość możliwych podzbiorów
binaryArray = []  # lista która zawiera wszystkie binarne maski
binaryArrayWithKeys = {}
binaryNumber = ""
substringArray = []  # list z podzbiorami, ale z powtórzeniami
sortBinaryArray = []  # sortowany list masek po ilośći jedynek
finalSubstringArray = []  # finalny sortowany list bez powtórzeń

for i in range(elementsAmount):
    print("Write ", i + 1, " element in array: ", end=" ")
    userElement = input()
    array.append(userElement)

for i in range(substringAmount):  # robimy wszystkie możliwe bitowe maski
    for j in range(elementsAmount):
        if i % 2 == 0:
            if i == 1:
                binaryNumber = '1' + binaryNumber
                i = 0
            else:
                binaryNumber = '0' + binaryNumber
                i = int(i / 2)
        else:
            if i == 1:
                binaryNumber = '1' + binaryNumber
                i = 0
            else:
                binaryNumber = '1' + binaryNumber
                i = int(i / 2)
    binaryArray.append(binaryNumber)
    binaryNumber = ''

for i in range(len(binaryArray)):  # do każdej liczby robimy klucz w którym zapisano ilość jedynek
    oneArray = 0
    for j in range(elementsAmount):
        if binaryArray[i][j] == '1':
            oneArray += 1
    binaryArrayWithKeys.update({binaryArray[i]: oneArray})

for i in range(elementsAmount + 1):  # sortujemy listę według ilośći jedynek, żeby wygodniej było widać w końcu
    for j in range(len(binaryArray)):
        if binaryArrayWithKeys[binaryArray[j]] == i:
            sortBinaryArray.append(binaryArray[j])

for i in range(len(binaryArray)):  # zmieniamy binarne maski na elementy zbioru
    substringArray.append([])
    for j in range(elementsAmount):
        if sortBinaryArray[i][j] == '1':
            substringArray[i].append(array[j])

for i in range(len(substringArray)):  # sortujemy, żeby nie było powtorzeń
    if substringArray[i] not in finalSubstringArray:
        finalSubstringArray.append(substringArray[i])

for i in range(len(finalSubstringArray)):  # printujemy wzsystkie podzbiory
    print(i + 1, end='')
    print(".", finalSubstringArray[i])
