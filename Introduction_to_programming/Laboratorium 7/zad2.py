numbers = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
userNumber = int(input("Write natural number in the range [1..10]: "))
if 0 < userNumber < 11:
    for i in range(userNumber):
        for j in range(10):
            if j == 9:
                print(numbers[0][i] * numbers[1][j], end="\n")
            else:
                print(numbers[0][i] * numbers[1][j], end="\t")
else:
    print("\n\n\nERROR! Your number is not in the range!")
