words = ('word1', 'wo', 'wor', 'pineapple')
tuple = ()
for i in range(len(words)):
    tuple += (words[i], )
    tuple += (len(words[i]), )
print(tuple)
