word = ''
list = []

while word != '0':
    word = input("Write word to list or write '0' if you want to see the result: ")
    if word != '0':
      list.append(word)

list.sort()
print(list)


