with open("text.txt", 'w', encoding='utf-8') as file:
    while True:
        option = input("Do you want to add a word for file? Y/N")
        if option == 'Y':
            word = input("What word do you want to add?")
            file.write(word + ' ')
        elif option == 'N':
            break
        else:
            print("You chose wrong option!")
            break

with open("text.txt", 'r') as file:
    quantity = 0
    lines = file.readlines()
    letter = input("Write the letter that quantity you are looking for: ")
    for i in range(len(lines[0])):
        if lines[0][i] == letter:
            quantity += 1
    print(lines)
    print(f"Letter \'{letter}\' appeared {quantity} times in words")

