def fibonacci_number(number):
    if number == 1:
        return 1
    elif number == 0:
        return 0
    else:
        return fibonacci_number(number - 1) + fibonacci_number(number - 2)


print(fibonacci_number(9))
