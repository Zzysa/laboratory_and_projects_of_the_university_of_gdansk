number = int(input("Write a size of side of square: "))
for i in range(number):
    for j in range(number):
        if j % 2 == 0:
            print(1, end='')
            if j == number - 1:
                print('\n', end='')
        else:
            print(0, end='')
            if j == number - 1:
                print('\n', end='')
