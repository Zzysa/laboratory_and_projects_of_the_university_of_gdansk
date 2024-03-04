with open("invocation.txt", encoding='utf-8') as file:
    lines = file.readlines()
    lines_D = []
    for i in range(len(lines)):
        if lines[i][0] == 'D':
            lines_D.append(lines[i])

print("Lines that starts with letter \'D\' in invocation \"Pan Tadeusz\" are: \n")
for i in range(len(lines_D)):
    print(f"{i + 1}. {lines_D[i]}")
