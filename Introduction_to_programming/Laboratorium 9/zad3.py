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


numbers = []
size = int(input("Write size of the array: "))
if size >= 0:
    for i in range(size):
        element = int(input(f"Write {i + 1} element of the array: "))
        numbers.append(element)
    print("Origin", numbers)
    print("Sort", sort_by_selection(numbers))
else:
    print("ERROR! Size of the array cannot be less then 0")

