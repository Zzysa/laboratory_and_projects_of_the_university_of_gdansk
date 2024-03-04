def int_to_binary(number):
    if number % 2 == 0:
        if number == 0:
            return "0"
        else:
            return int_to_binary(int(number / 2)) + "0"
    else:
        if number == 1:
            return "1"
        else:
            return int_to_binary(int(number / 2)) + "1"


print(int_to_binary(167))
