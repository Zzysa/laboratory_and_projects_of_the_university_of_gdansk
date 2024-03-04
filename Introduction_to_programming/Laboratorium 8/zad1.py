def exponentiation(number, power):
    if power == 0:
        return 1
    else:
        return number * exponentiation(number, power - 1)


print(exponentiation(3, 4))
