firstWordLength = len(input("Write first word: "))
secondWordLength = len(input("Write second word: "))
if firstWordLength > secondWordLength:
    print("First word length is longer than second word length")
elif firstWordLength == secondWordLength:
    print("First word length is equal second word length")
else:
    print("Second word length is longer than word length")
