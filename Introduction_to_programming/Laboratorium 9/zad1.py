def bubble_sort(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - 1 - j):
            if array[i] > array[i + 1] and i + 1 < len(array):
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


arr = []
size = int(input("Write size of array: "))
if size >= 0:
    for i in range(size):
        number = int(input(f"Write the number that will be on the {i + 1} position in the array: "))
        arr.append(number)
    print(f"Your not sorted array is {arr}")
    print(f"Your sorted array is {bubble_sort(arr)}")
else:
    print("Error! The size of the array cannot be less then 0!")
