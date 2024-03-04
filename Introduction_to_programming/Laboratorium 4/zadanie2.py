sentence = input("Write sentence: ")
if sentence[0] >= chr(65) and sentence[0] <= chr(90):
    print("Sentence starts with uppercase letter")
else:
    print("Sentence doesn't start with an uppercase letter")
if sentence[len(sentence) - 1] == '.':
    print("Sentence ends with a dot")
else:
    print("Sentence doesn't end with a dot")
