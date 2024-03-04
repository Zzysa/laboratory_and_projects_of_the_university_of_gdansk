def caesar_cipher(word, key):
    new_word = ""
    for i in word:
        if ord(i) > 90:
            new_word += chr((ord(i) + key) % 90 + 66)
        else:
            new_word += chr(ord(i) + key)
    return new_word


userWord = input("Write the word: ")
key = int(input("Write the key: "))

encryptedWord = caesar_cipher(userWord, key)
print(encryptedWord)
