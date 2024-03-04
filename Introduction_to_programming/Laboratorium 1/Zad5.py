information = input("Here you have to write something: ")
try:
    int(information)
    print("Type of you data is integer")
except ValueError:
    try:
        float(information)
        print("Type of you data is float")
    except ValueError:
        print("Type of you data is string")
