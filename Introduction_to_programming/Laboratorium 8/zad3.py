def reflection(word):
    if len(word) == 1:
        return word[0]
    else:
        return word[len(word) - 1] + reflection(word[:-1])


print(reflection("Hello, World!"))
