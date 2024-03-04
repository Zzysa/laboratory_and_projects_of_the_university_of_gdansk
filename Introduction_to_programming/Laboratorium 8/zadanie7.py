def sum_of_figures(number):
    if len(number) == 1:
        return int(number)
    return int(number[len(number) - 1]) + sum_of_figures(number[:-1])


print(sum_of_figures("054150657426"))
