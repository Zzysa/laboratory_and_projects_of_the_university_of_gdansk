firstList = input("Write first word: ")
secondList = input("Write second word: ")
thirdList = []

for j in range(len(firstList) - 1):
    if firstList[j] in secondList and firstList[j] not in thirdList:
            thirdList.append(firstList[j])

print(thirdList)
