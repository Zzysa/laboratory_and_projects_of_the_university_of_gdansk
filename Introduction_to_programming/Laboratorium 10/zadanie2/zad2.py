with open("numbers.txt") as file:
    lines = file.readlines()
    sum = 0
    for i in range(len(lines)):
        sum += int(lines[i])

print(f"The sum of numbers in file is {sum}")
