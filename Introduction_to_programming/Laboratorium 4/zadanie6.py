string = input("Write string: ")

list = []
sum = ""

for i in range(len(string)): #robimy list z powtórzeniami
    for j in range(i, len(string), 1):
        sum += string[j]
        list.append(sum)
        if j == len(string) - 1:
            sum = ""

new_list = []

for i in list: #robimy nowy list, ale bez powtórzeń
    if i not in new_list:
        new_list.append(i)

print("All substrings of the string \"" + string + "\" are: ", end='')
print(new_list)
