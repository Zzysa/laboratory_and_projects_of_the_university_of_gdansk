import random


def insertion_sort(array):
    for j in range(1, len(array)):
        while array[j] < array[j - 1] and j != 0:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
        print(array)
    return array


arr = []
size = int(input("Write size of array: "))
if size >= 0:
    for i in range(size):
        number = int(input(f"Write the number that will be on the {i + 1} position in the array: "))
        arr.append(number)
    print(f"Your not sorted array is {arr}")
    print(f"Your sorted array is {insertion_sort(arr)}")
else:
    print("Error! The size of the array cannot be less then 0!")
