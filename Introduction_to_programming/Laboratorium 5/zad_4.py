firstList = []
secondList = []

for i in range(1, 101):
    firstList.append(i)

for i in range(len(firstList)):
    if i % 3 == 0:
        secondList.append(i)

print(secondList)


