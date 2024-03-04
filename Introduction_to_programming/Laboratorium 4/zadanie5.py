sentence = input("Write sentence: ")
sentence += ' '
counterWords = 0
for i in range(len(sentence)):
    if sentence[i] == ' ' and sentence[i - 1] != ' ':
        counterWords += 1
print(counterWords)