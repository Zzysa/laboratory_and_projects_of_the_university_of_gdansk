sentence = input("Write sentence: ")
upperSentence = sentence.upper()
sentenceLength = len(sentence)
j = 0
for i in range(int(len(sentence)/2 + 1)): #bierzemy połowę zdania, aby porównać dwie połowy, a +1, aby sprawdzić, czy jest palindromem
    if i == int(len(sentence)/2) or j == int(len(sentence)/2):
        print("The sentence is a palindrome")
    elif upperSentence[i] == '.' or upperSentence[i] == ' ': #w pierwszej połowie szukamy kropek i spacji, jeśli jest to zmieniamy na jeden znak w prawo
        i += 1
    elif upperSentence[len(upperSentence) - j - 1] == '.' or upperSentence[len(upperSentence) - j - 1] == ' ': #w drugiej połowie szukamy kropek i spacji, jeśli jest to zmieniamy na jeden znak w w lewo
        j += 1
    elif upperSentence[i] == upperSentence[len(upperSentence) - j - 1]: #porównujemy dwa symbola z lewej i prowej strony, jeżeli poprawnie, to zmieniamy na jaden znak w prawo i na jeden znak w lewo
        i += 1
        j += 1
    else:
        print("The sentence isn't a palindrome")
        break
