userWord = input("Write one word: ")
userChar = input("Write one symbol from your word: ")
counter = 0
for i in userWord:
    if i == userChar:
        counter += 1
print("In the word ", userWord, "character ", userChar, "appears ",  counter, "times.")