import random


def sort_by_selection(array):
    for j in range(len(array) - 1):
        minimum = array[j]
        min_index = j
        for k in range(len(array) - j - 1):
            if array[j + k + 1] < minimum:
                minimum = array[j + k + 1]
                min_index = j + k + 1
        array[j], array[min_index] = array[min_index], array[j]
    return array


def binary_search(array, number, index=0):
    if array[len(array)//2] == number:
        return f"Your element is in the array and his index is {index + len(array)//2}"
    elif len(array)//2 == 0:
        return "Your element is not in the array"
    elif array[len(array)//2] > number:
        return binary_search(array[:len(array) // 2], number, index)
    elif array[len(array)//2] < number:
        return binary_search(array[len(array) // 2:], number, index + len(array)//2)


numbers = []
size = int(input("Write size of the array: "))
search = int(input("Write element what are you looking for: "))
if size >= 0:
    for i in range(size):
        element = random.randint(0, 100)
        if element not in numbers:
            numbers.append(element)
    print("Origin", numbers)
    print("Sort", sort_by_selection(numbers))
    print(binary_search(sort_by_selection(numbers), search))
else:
    print("ERROR! Size of the array cannot be less then 0")

