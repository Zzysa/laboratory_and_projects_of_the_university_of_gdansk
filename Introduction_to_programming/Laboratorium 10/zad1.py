try:
    print("Hello," + name)
except NameError:
    print("1. Missing a value for \"name\"! (NameError)")

try:
    x = 1 / 0
except ZeroDivisionError:
    print("2. We can't divide by zero! (ZeroDivisionError)")

try:
    x = int("Eleven")
except ValueError:
    print("3. We can't make integer from string \"Eleven\"! (ValueError)")

try:
    array = []
    print(array[0])
except IndexError:
    print("4. We can't print 1 element, because array is empty! (IndexError)")

try:
    file1 = open("zadanie2.py")
except FileNotFoundError:
    print("5. We can't open file that doesn't exist! (FileNotFoundError)")

try:
    with open("file.txt", 'w') as f:
        f.write("Hello, world!")
    with open("file.txt", 'x') as f:
        f.write("Hello, world, again!")
except FileExistsError:
    print("6. We can't make same file twice! (FileExistsError)")

try:
    number = 13
    print(number + "13")
except TypeError:
    print("7. We can't work with variables if they have different types! (TypeError)")

try:
    string = "abc"
    string.append("def")
except AttributeError:
    print("8. We can't use append for string and add \"def\"! (AttributeError)")

try:
    numbers = {'One': 1, 'Two': 2, 'Three': 3}
    print(numbers['Four'])
except KeyError:
    print("9. There is no key \"Four\"! (KeyError)")
