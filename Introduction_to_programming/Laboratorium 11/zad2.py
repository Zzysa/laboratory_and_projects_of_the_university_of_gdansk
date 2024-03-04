import numpy as np

n = int(input("Podaj rozmiar tablicy: "))
elements = []

for i in range(n):
    element = int(input(f"Wpisz element {i + 1}: "))
    elements.append(element)

array = np.array(elements)
print(f"Jednowymiarowa tablica: {array}")

for i in range(1, n + 1):
    if n % i == 0:
        reshaped_array = array.reshape(i, -1)
        print(f"Macierz {i}x{n // i}:\n{reshaped_array}\n")
