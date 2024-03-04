string = input("Write string: ")
stringLength = len(string)

aCounter = 0
eCounter = 0
iCounter = 0
oCounter = 0
uCounter = 0
yCounter = 0

for i in range(len(string)):
    if string[i] == 'a':
        aCounter += 1
    elif string[i] == 'e':
        eCounter += 1
    elif string[i] == 'i':
        iCounter += 1
    elif string[i] == 'o':
        oCounter += 1
    elif string[i] == 'u':
        uCounter += 1
    elif string[i] == 'y':
        yCounter += 1

print("The number of characters 'a' in this string is ", aCounter)
print("The number of characters 'e' in this string is ", eCounter)
print("The number of characters 'i' in this string is ", iCounter)
print("The number of characters 'o' in this string is ", oCounter)
print("The number of characters 'u' in this string is ", uCounter)
print("The number of characters 'y' in this string is ", yCounter)